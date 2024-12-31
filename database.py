import os
from PySide6 import QtCore, QtSql, QtGui
from pathlib import Path
from note_data import NoteData, NOTE_ID, TOPIC_ID
from note_style import ENoteBackground
from topic import TopicData, Topic
from util import bytesToQByteArray
import datetime
import logging

# In version 2, the note's position and size was explicitly stored.
kCurrentDatabaseVersion = 2

# Global value data type constants
kDataTypeInteger = 0
kDataTypeString = 1
kDataTypeBlob = 2

# Global value keys
kDatabaseVersionKey = "databaseVersion"

class Database:
  def __init__(self):
    super(Database, self).__init__()

  def openDatabase(self, pathName) -> bool:
    return self.open(pathName)

  def open(self, pathName: str) -> bool:
    self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    p = Path(pathName)

    dbExists = p.is_file()
    if not dbExists:
      # The database does not exist.  Before creating, verify that the parent directory exists.
      # Database creation will fail if the parent directory does not exist.
      if not p.parent.exists():
        p.parent.mkdir(parents=True)

    self.db.setDatabaseName(pathName)

    if self.db.open():
      if dbExists:
        logging.info("Database open")
        self.updateDatabase()
      else:
        # Create the database, and all tables
        self.createNewDatabase()
        logging.info(f'Created notes file at: {pathName}')
      return True
    else:
      logging.error(f"Could not open notes file: {pathName}")
      return False

  def isDatabaseOpen(self):
    if self.db is not None:
      return self.db.isOpen()
    else:
      return False

  def closeDatabase(self):
    self.close()

  def close(self):
    if self.db is not None:
      self.db.close()

  def reportError(self, errorMessage):
    logging.error(errorMessage)

  def updateDatabase(self):
    """ Updates the database to the current version. """
    # Read database version (stored as a global value).  If there is no database
	  # version in the globals, then it is version 1.
    databaseVersion = 1     # Default to version 1

    if self.globalsTableExists():
      databaseVersion = self.getGlobalValue("databaseVersion")
      if databaseVersion is None:
        # There is no database version, so this is a version 1 database.
        databaseVersion = 1
    else:
      # There is no globals table, so this is a version 1 database.
      self.createGlobalsTable()
      self.setGlobalValue("databaseVersion", 1)
      databaseVersion = 1

    # Update the database to the current version
    if databaseVersion == 1:
      success = self.updateDatabaseToVersion2()
      if not success:
        self.reportError("Error when attempting to update the database to version 2")

  def updateDatabaseToVersion2(self):
    """ Updates the database to version 2. """
    self.setGlobalValue("databaseVersion", 2)

    # Add the x, y, width, and height fields to the notes table
    resultX = self.addColumnToTable("notes", "x", "integer")
    resultY = self.addColumnToTable("notes", "y", "integer")
    resultWidth = self.addColumnToTable("notes", "width", "integer")
    resultHeight = self.addColumnToTable("notes", "height", "integer")

    return resultX and resultY and resultWidth and resultHeight

  def addColumnToTable(self, tableName: str, columnName: str, columnType: str, defaultValue = None) -> bool:
    """ Adds a column to a table. """
    queryObj = QtSql.QSqlQuery()
    queryStr = f"alter table {tableName} add column {columnName} {columnType}"

    if defaultValue is not None:
      queryStr += f" default {defaultValue}"

    queryObj.prepare(queryStr)
    queryObj.exec()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f"Error when attempting to add a column ({columnName}) to table {tableName}: {sqlErr.text()}")
      return False
    else:
      return True

  def createNewDatabase(self):
    # Create database tables
    self.createNotesTable()
    self.createTopicsTable()
    self.createGlobalsTable()

  def createNotesTable(self):
    createStr = """create table notes (
            noteid integer primary key,
            title text,
            notetext text,
            geometry blob,
            added integer,
            lastupdated integer,
            topicid integer,
            usesowncolors integer,
            alwaysontop integer,
            textcolor integer,
            bgcolor integer,
            bgtype integer,
            transparency integer,
            x integer,
            y integer,
            width integer,
            height integer
            )"""

    queryObj = QtSql.QSqlQuery()

    if not queryObj.exec_(createStr):
      self.reportError(f'[createNotesTable]: {queryObj.lastError().text()}')
      return False

    return True

  def createTopicsTable(self):
    createStr = """create table topics (
            id integer primary key,
            name text,
            textcolor integer,
            bgcolor integer,
            bgtype integer,
            transparency integer)"""

    queryObj = QtSql.QSqlQuery()

    if not queryObj.exec_(createStr):
      self.reportError(f'[createTopicsTable]: {queryObj.lastError().text()}')
      return False

    return True

  def createGlobalsTable(self):
    """ Creates the globals table. """
    queryObj = QtSql.QSqlQuery(self.db)

    createStr = "create table globals ("
    createStr += "key text UNIQUE, "
    createStr += "datatype int, "
    createStr += "intval int, "
    createStr += "stringval text, "
    createStr += "blobval blob"
    createStr += ")"

    queryObj.prepare(createStr)

    queryObj.exec()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError( f"Error when attempting to the globals table: {sqlErr.text()}")

  def globalsTableExists(self) -> bool:
    """ Checks if the globals table exists. """
    queryObj = QtSql.QSqlQuery(self.db)

    queryObj.prepare("select name from sqlite_master where type='table' and name='globals'")

    queryObj.exec()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f"Error when attempting to determine if the globals table exists: {sqlErr.text()}")
      return False

    if queryObj.next():
      return True
    else:
      return False

  def getGlobalValue(self, key: str) -> int | str | bytes | None:
    """ Returns the value of a 'global value' for the given key. """
    queryObj = QtSql.QSqlQuery(self.db)
    queryObj.prepare("select datatype from globals where key = ?")
    queryObj.bindValue(0, key)

    queryObj.exec()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError("Error when attempting to retrieve a global value key: {}".format(sqlErr.text()))
      return None

    if queryObj.next():
      typeField = queryObj.record().indexOf("datatype")

      dataType = queryObj.value(typeField)
    else:
      # key not found
      return None

    if dataType == kDataTypeInteger:
      createStr = "select intval from globals where key=?"
    elif dataType == kDataTypeString:
      createStr = "select stringval from globals where key=?"
    elif dataType == kDataTypeBlob:
      createStr = "select blobval from globals where key=?"
    else:
      # Unknown data type
      self.reportError("getGlobalValue: unknown data type: {}".format(dataType))
      return None

    # Now that the data type is known, retrieve the data itself.
    queryObj.prepare(createStr)
    queryObj.bindValue(0, key)

    queryObj.exec()

    # Check for errors
    sqlErr = queryObj.lastError()
    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError("Error when attempting to retrieve a page: {}".format(sqlErr.text()))
      return None

    if queryObj.next():
      if dataType == kDataTypeInteger:
        valueField = queryObj.record().indexOf("intval")
      elif dataType == kDataTypeString:
        valueField = queryObj.record().indexOf("stringval")
      elif dataType == kDataTypeBlob:
        valueField = queryObj.record().indexOf("blobval")
      else:
        return None

      value = queryObj.value(valueField)

      if isinstance(value, QtCore.QByteArray):
        value = bytes(value)

      return value

  def setGlobalValue(self, key: str, value: int | str | bytes):
    """ Sets the value of the given key to the given value. """

    # See if the key exists
    queryObj = QtSql.QSqlQuery(self.db)
    queryObj.prepare("select datatype from globals where key = ?")
    queryObj.bindValue(0, key)

    queryObj.exec()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError("Error when attempting to determine if a global value exists: {}".format(sqlErr.text()))
      return

    if queryObj.next():
      # Key exists; update its value
      if isinstance(value, int):
        createStr = "update globals set intval=? where key=?"
      elif isinstance(value, str):
        createStr = "update globals set stringval=? where key=?"
      elif isinstance(value, bytes):
        createStr = "update globals set blobval=? where key=?"

        # Must convert to a QByteArray
        value = bytesToQByteArray(value)
      else:
        self.reportError("setGlobalValue: invalid data type")
        return

      queryObj.prepare(createStr)

      queryObj.addBindValue(value)
      queryObj.addBindValue(key)
    else:
      if isinstance(value, int):
        createStr = "insert into globals (key, datatype, intval) values (?, ?, ?)"
        dataType = kDataTypeInteger
      elif isinstance(value, str):
        createStr = "insert into globals (key, datatype, stringval) values (?, ?, ?)"
        dataType = kDataTypeString
      elif isinstance(value, bytes):
        createStr = "insert into globals (key, datatype, blobval) values (?, ?, ?)"
        dataType = kDataTypeBlob

        # Must convert to a QByteArray
        value = bytesToQByteArray(value)
      else:
        self.reportError("setGlobalValue: invalid data type")
        return

      queryObj.prepare(createStr)

      queryObj.addBindValue(key)
      queryObj.addBindValue(dataType)
      queryObj.addBindValue(value)

    queryObj.exec()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError("Error when attempting to set a global value: {}".format(sqlErr.text()))

  def globalValueExists(self, key):
    """ Checks if a global value exists. """
    queryObj = QtSql.QSqlQuery(self.db)
    queryObj.prepare("select datatype from globals where key=?")
    queryObj.addBindValue(key)

    queryObj.exec()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      return False
    else:
      atLeastOne = queryObj.next()
      return atLeastOne

  def getQueryField(self, queryObj: QtSql.QSqlQuery, fieldName: str, defaultValue: int | str | bytes | None) -> int | str | bytes | None:
    fieldIndex = queryObj.record().indexOf(fieldName)

    if queryObj.isNull(fieldIndex):
      return defaultValue

    fieldValue = queryObj.value(fieldIndex)
    return fieldValue

  def addNote(self, noteData: NoteData) -> bool:
    """Adds a new note to the database.

    Args:
        noteData (NoteData): NoteData describing the note

    Returns:
        bool: True if successful, False otherwise
    """
    queryObj = QtSql.QSqlQuery()
    queryObj.prepare("""insert into notes (noteid, title, notetext, geometry, added,
                     lastupdated, topicid, usesowncolors, alwaysontop,
                     textcolor, bgcolor, bgtype, transparency)
                     values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")

    queryObj.addBindValue(noteData.noteId)
    queryObj.addBindValue(noteData.title)
    queryObj.addBindValue(noteData.contentsData)
    queryObj.addBindValue(noteData.geometryData)
    queryObj.addBindValue(noteData.addedTime.timestamp())
    queryObj.addBindValue(noteData.lastModifiedTime.timestamp())
    queryObj.addBindValue(noteData.topicId)
    queryObj.addBindValue(noteData.usesOwnColors)
    queryObj.addBindValue(noteData.alwaysOnTop)
    queryObj.addBindValue(noteData.textColor.rgba())
    queryObj.addBindValue(noteData.bgColor.rgba())
    queryObj.addBindValue(noteData.bgType.value)
    queryObj.addBindValue(noteData.transparency)

    queryObj.exec_()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f'addNote error: {sqlErr.text()}')
      return False
    else:
      return True

  def updateNote(self, noteData: NoteData) -> bool:
    """Saves a note to the database.

    Args:
        noteData (NoteData): NoteData describing the note

    Returns:
        bool: True if successful, False otherwise
    """
    queryObj = QtSql.QSqlQuery()
    queryObj.prepare("""update notes set title=?, notetext=?, geometry=?, added=?,
		                          lastupdated=?, topicid=?, usesowncolors=?, alwaysontop=?, textcolor=?,
                              bgcolor=?, bgtype=?, transparency=?, x=?, y=?, width=?, height=? where noteid=?""")

    queryObj.addBindValue(noteData.title)
    queryObj.addBindValue(noteData.contentsData)
    queryObj.addBindValue(noteData.geometryData)
    queryObj.addBindValue(noteData.addedTime.timestamp())
    queryObj.addBindValue(noteData.lastModifiedTime.timestamp())
    queryObj.addBindValue(noteData.topicId)
    queryObj.addBindValue(noteData.usesOwnColors)
    queryObj.addBindValue(noteData.alwaysOnTop)
    queryObj.addBindValue(noteData.textColor.rgba())
    queryObj.addBindValue(noteData.bgColor.rgba())
    queryObj.addBindValue(noteData.bgType.value)
    queryObj.addBindValue(noteData.transparency)
    queryObj.addBindValue(noteData.x)
    queryObj.addBindValue(noteData.y)
    queryObj.addBindValue(noteData.width)
    queryObj.addBindValue(noteData.height)
    queryObj.addBindValue(noteData.noteId)

    queryObj.exec_()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f'updateNote error: {sqlErr.text()}')
      return False
    else:
      return True

  def deleteNote(self, noteId: NOTE_ID) -> bool:
    """Deletes a note from the database.

    Args:
        noteId (NOTE_ID): ID of the note to delete

    Returns:
        bool: True if successful, False otherwise
    """
    queryObj = QtSql.QSqlQuery()
    queryObj.prepare("delete from notes where noteid=?")

    queryObj.addBindValue(noteId)

    queryObj.exec_()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f'deleteNote error: {sqlErr.text()}')
      return False
    else:
      return True

  def getNotes(self) -> tuple[bool, list[NoteData]]:
    """ Retrieves notes from the database.
        Returns a tuple consisting of a boolean, indicating success or failure,  and a list of NoteData.
    """
    queryObj = QtSql.QSqlQuery()
    queryObj.prepare("""select noteid, title, notetext, geometry, added,
                        lastupdated, topicid, usesowncolors, alwaysontop, textcolor, bgcolor, bgtype,
                        transparency, x, y, width, height from notes""")

    queryObj.exec_()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f'getNotes error: {sqlErr.text()}')
      return (False, [])

    notes = []

    while queryObj.next():
      noteData = NoteData()

      noteData.noteId = self.getQueryField(queryObj, 'noteid', -1)
      noteData.title = self.getQueryField(queryObj, 'title', '')
      noteData.geometryData = self.getQueryField(queryObj, 'geometry', QtCore.QByteArray())
      noteData.contentsData = self.getQueryField(queryObj, 'notetext', '')
      noteData.addedTime = datetime.datetime.fromtimestamp(self.getQueryField(queryObj, 'added', 0))
      noteData.lastModifiedTime = datetime.datetime.fromtimestamp(self.getQueryField(queryObj, 'lastupdated', 0))
      noteData.topicId = self.getQueryField(queryObj, 'topicid', 0)
      noteData.usesOwnColors = True if self.getQueryField(queryObj, 'usesowncolors', 0) == 1 else False
      noteData.alwaysOnTop = True if self.getQueryField(queryObj, 'alwaysontop', 0) == 1 else False
      noteData.textColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'textcolor', 0))
      noteData.bgColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'bgcolor', 0))
      noteData.bgColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'bgcolor', 0))
      noteData.bgType = ENoteBackground(self.getQueryField(queryObj, 'bgtype', 0))
      noteData.transparency = self.getQueryField(queryObj, 'transparency', 100)
      noteData.x = self.getQueryField(queryObj, 'x', None)
      noteData.y = self.getQueryField(queryObj, 'y', None)
      noteData.width = self.getQueryField(queryObj, 'width', None)
      noteData.height = self.getQueryField(queryObj, 'height', None)

      notes.append(noteData)

    return (True, notes)

  def getTopics(self) -> tuple[bool, list[TopicData]]:
    """ Retrieves topics from the database.

    Returns:
        tuple[bool, list[]]: Success, List of topics
    """
    queryObj = QtSql.QSqlQuery()
    queryObj.prepare("select id, name, textcolor, bgcolor, bgtype, transparency from topics")

    queryObj.exec_()

    # Check for errors
    sqlErr = queryObj.lastError()

    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f'getTopics error: {sqlErr.text()}')
      return (False, [])

    topics = []

    while queryObj.next():
      topicData = TopicData()

      topicData.id = self.getQueryField(queryObj, 'id', -1)
      topicData.name = self.getQueryField(queryObj, 'name', '')
      topicData.textColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'textcolor', 0))
      topicData.bgColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'bgcolor', 0))
      topicData.bgType = ENoteBackground(self.getQueryField(queryObj, 'bgtype', 0))
      topicData.transparency = self.getQueryField(queryObj, 'transparency', 100)

      topics.append(topicData)

    return (True, topics)

  def addTopic(self, topic: Topic) -> bool:
    """Adds a topic to the database.
      Returns:
        True if successful, False if not.
    """
    queryObj = QtSql.QSqlQuery()
    queryObj.prepare("""insert into topics (id, name, textcolor, bgcolor, bgtype, transparency)
                              values (?, ?, ?, ?, ?, ?)""")

    queryObj.addBindValue(topic.id)
    queryObj.addBindValue(topic.topicName)
    queryObj.addBindValue(topic.textColor.rgba())
    queryObj.addBindValue(topic.backgroundColor.rgba())
    queryObj.addBindValue(topic.backgroundType.value)
    queryObj.addBindValue(topic.transparency)

    queryObj.exec_()

    # Check for errors
    sqlErr = queryObj.lastError()
    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f'[addTopic]: {sqlErr.text()}')
      return False
    else:
      return True

  def updateTopic(self, topic: Topic) -> bool:
    """Updates a topic

    Args:
        topic (Topic): Topic to update

    Returns:
        bool: True if successful, False if not
    """
    queryObj = QtSql.QSqlQuery()
    queryObj.prepare("update topics set name=?, textcolor=?, bgcolor=?, bgtype=?, transparency=? where id=?")

    queryObj.addBindValue(topic.topicName)
    queryObj.addBindValue(topic.textColor.rgba())
    queryObj.addBindValue(topic.backgroundColor.rgba())
    queryObj.addBindValue(topic.backgroundType.value)
    queryObj.addBindValue(topic.transparency)
    queryObj.addBindValue(topic.id)

    queryObj.exec_()

    # Check for errors
    sqlErr = queryObj.lastError()
    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f'[updateTopic]: {sqlErr.text()}')
      return False
    else:
      return True

  def deleteTopic(self, topicId: TOPIC_ID) -> bool:
    """Deletes a topic.

    Args:
        topic (Topic): Topic to delete

    Returns:
        bool: True if successful, False otherwise.
    """
    queryObj = QtSql.QSqlQuery()
    queryObj.prepare("delete from topics where id=?")

    queryObj.addBindValue(topicId)

    queryObj.exec_()

    # Check for errors
    sqlErr = queryObj.lastError()
    if sqlErr.type() != QtSql.QSqlError.ErrorType.NoError:
      self.reportError(f'[deleteTopic]: {sqlErr.text()}')
      return False
    else:
      return True
