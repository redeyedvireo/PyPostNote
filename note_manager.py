from PySide6 import QtCore, QtWidgets, QtGui
from note_data import TOPIC_ID, NoteData, NOTE_ID, ENoteSizeEnum
from note_exporter import NoteExporter
from note_wnd import NoteWnd
from preferences import Preferences
from topic import Topic, kDefaultTopicId
from topic_manager import TopicManager
import logging

"""List of note sizes (tuples of width, height)
"""
NoteSizeList= [
  (125, 75),
  (200, 203),
  (350, 250),
  (305, 413)
]

class NoteManager(QtCore.QObject):
  saveNote = QtCore.Signal(NoteData)

  def __init__(self, topicManager: TopicManager, preferences: Preferences):
    super().__init__()

    self.noteWndDict: dict[NOTE_ID, NoteWnd] = {}     # Maps NOTE_IDs to NoteWnds
    self.topicManager = topicManager
    self.preferences = preferences

    self.defaultNoteFontSize = self.preferences.defaultFontSize

  @property
  def defaultNoteFontFamily(self) -> str:
    return self.preferences.defaultFontFamily

  @defaultNoteFontFamily.setter
  def defaultNoteFontFamily(self, fontFamily: str):
    self.preferences.defaultFontFamily = fontFamily

  @property
  def defaultNoteFontSize(self) -> int:
    return self.preferences.defaultFontSize

  @defaultNoteFontSize.setter
  def defaultNoteFontSize(self, size: int):
    self.preferences.defaultFontSize = size

  def allNoteIds(self) -> list[NOTE_ID]:
    """Returns a list of all note IDs

    Returns:
        list[NOTE_ID]: List of note IDs
    """
    return self.noteWndDict.keys()

  def getNote(self, noteId: NOTE_ID) -> NoteWnd | None:
    return self.noteWndDict[noteId] if noteId in self.noteWndDict else None

  def showNote(self, noteId: NOTE_ID):
    if noteId in self.noteWndDict:
      note = self.noteWndDict[noteId]
      note.showNote()

  def showAllNotes(self):
    for note in self.noteWndDict.values():
      note.showNote()

  def hideAllNotes(self):
    for note in self.noteWndDict.values():
      note.hideNote()

  def saveAllNotes(self):
    for note in self.noteWndDict.values():
      self.saveNote.emit(note.noteData)
      note.dirty = False

  def saveDirtyNotes(self):
    for note in self.noteWndDict.values():
      if note.dirty:
        self.saveNote.emit(note.noteData)
        note.dirty = False

  def onTopicChanged(self, topic: Topic):
    """Refreshes all notes with the given topic.  This must be called whenever a
       topic has changed.

    Args:
        topic (Topic): Topic that was changed
    """
    for noteWnd in self.noteWndDict.values():
      if noteWnd.topicId == topic.id:
        # This note uses the topic, so refresh it.
        noteWnd.updateNote()

  def onTopicDeleted(self, topicId: TOPIC_ID):
    """Scans through the notes, and changes any note that was using the given topic
       to instead use the default topic.

    Args:
        topicId (TOPIC_ID): Topic ID
    """
    for noteWnd in self.noteWndDict.values():
      if noteWnd.topicId == topicId:
        noteWnd.topicId = kDefaultTopicId

  def createNote(self, noteId: NOTE_ID, useNewId = False) -> NoteWnd:
    """Creates a new note with the given ID.  If useNewId is True, a new ID will be generated
       if the given ID is already in use.

    Args:
        noteId (NOTE_ID): ID of the note to create
        useNewId (bool, optional): If True, a new ID will be created if the given ID is
                                   already in use. Defaults to False.

    Returns:
        NoteWnd: Created note window, or None if the note ID is already in use
    """
    # First, check that noteId is not already being used
    if noteId in self.noteWndDict:
      if not useNewId:
        # If noteId does already exist, this is an error condition
        logging.error(f'[NoteManager.createNote] Note ID {noteId} already exists in the noteWndDict')
        return
      else:
        # Generate a new ID
        noteId = self.getFreeId()

    noteWnd = NoteWnd(self.topicManager)
    noteWnd.noteId = noteId

    noteWnd.setDefaultFont(self.defaultNoteFontFamily, self.defaultNoteFontSize)

    # Add to noteWndDict
    self.noteWndDict[noteId] = noteWnd

    return noteWnd

  def createPopulatedNote(self, noteData: NoteData, useNewId = False):
    """ Creates a fully-populated note.  Used when loading notes from the database.
        If useNewId is True, a new ID will be generated if the given ID is already in use.
    """
    newNote = self.createNote(noteData.noteId, useNewId)

    if newNote is not None:
      noteData.noteId = newNote.noteId    # createNote may have generated a new ID
      newNote.noteData = noteData
      newNote.dirty = False

      newNote.showNote()

      return newNote
    else:
      logging.error(f'[NoteManager.createPopulatedNote] Error creating note - ID already exists: {noteData.noteId}')
      return None

  def createBlankNote(self, noteSize: ENoteSizeEnum) -> NoteWnd:
    noteId = self.getFreeId()

    newNote = self.createNote(noteId)

    noteSizeTuple = NoteSizeList[noteSize.value]

    newNote.resize(QtCore.QSize(noteSizeTuple[0], noteSizeTuple[1]))
    newNote.showNote()

    return newNote

  def deleteNote(self, noteId: NOTE_ID):
    """Deletes the note with the given ID

       To delete a note, several steps are performed:
        1. Immediately hide the note
        1. Remove the note from noteWndDict

    Args:
        noteId (NOTE_ID): ID of the note to delete
    """
    if noteId in self.noteWndDict:
      noteWnd = self.noteWndDict[noteId]
      noteWnd.hideNote()
      noteWnd.deleteLater()
      del self.noteWndDict[noteId]
    else:
      logging.error(f'[NoteManager.deleteNote] Note ID {noteId} not found in noteWndDict')

  def updateTopicsForANote(self, noteId: NOTE_ID):
    """Causes a note to update the topic list.  This is generally used when a note invokes
        the Edit Topics dialog, and the topics have changed.

    Args:
        noteId (NOTE_ID): Note ID
    """
    if noteId in self.noteWndDict:
      noteWnd = self.noteWndDict[noteId]
      noteWnd.updateTopics()

  def getFreeId(self, addToDatabase = False):
    """Returns the next free ID to use when creating a new note.
    """
    keysInUse = self.noteWndDict.keys()

    highestKey = max(keysInUse) if len(keysInUse) > 0 else 0

    return highestKey + 1

  def addNotesToExporter(self, noteExporter: NoteExporter):
    for noteWnd in self.noteWndDict.values():
      noteExporter.addNote(noteWnd.noteData)
