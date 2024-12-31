import os
from PySide6 import QtCore, QtSql, QtGui
from pathlib import Path
from note_data import NoteData, NOTE_ID, TOPIC_ID
from note_style import ENoteBackground
from topic import TopicData, Topic
import datetime
import logging

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
    # Nothing to do at this point.
    pass

  def createNewDatabase(self):
    # Create database tables
    self.createNotesTable()
    self.createTopicsTable()

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

  def getQueryField(self, queryObj, fieldName) -> int | str | bytes | None:
    fieldIndex = queryObj.record().indexOf(fieldName)

    return queryObj.value(fieldIndex)

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

      noteData.noteId = self.getQueryField(queryObj, 'noteid')
      noteData.title = self.getQueryField(queryObj, 'title')
      noteData.geometryData = self.getQueryField(queryObj, 'geometry')
      noteData.contentsData = self.getQueryField(queryObj, 'notetext')
      noteData.addedTime = datetime.datetime.fromtimestamp(self.getQueryField(queryObj, 'added'))
      noteData.lastModifiedTime = datetime.datetime.fromtimestamp(self.getQueryField(queryObj, 'lastupdated'))
      noteData.topicId = self.getQueryField(queryObj, 'topicid')
      noteData.usesOwnColors = True if self.getQueryField(queryObj, 'usesowncolors') == 1 else False
      noteData.alwaysOnTop = True if self.getQueryField(queryObj, 'alwaysontop') == 1 else False
      noteData.textColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'textcolor'))
      noteData.bgColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'bgcolor'))
      noteData.bgColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'bgcolor'))
      noteData.bgType = ENoteBackground(self.getQueryField(queryObj, 'bgtype'))
      noteData.transparency = self.getQueryField(queryObj, 'transparency')
      noteData.x = self.getQueryField(queryObj, 'x')
      noteData.y = self.getQueryField(queryObj, 'y')
      noteData.width = self.getQueryField(queryObj, 'width')
      noteData.height = self.getQueryField(queryObj, 'height')

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

      topicData.id = self.getQueryField(queryObj, 'id')
      topicData.name = self.getQueryField(queryObj, 'name')
      topicData.textColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'textcolor'))
      topicData.bgColor = QtGui.QColor.fromRgba(self.getQueryField(queryObj, 'bgcolor'))
      topicData.bgType = ENoteBackground(self.getQueryField(queryObj, 'bgtype'))
      topicData.transparency = self.getQueryField(queryObj, 'transparency')

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
