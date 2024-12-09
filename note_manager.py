from PySide6 import QtCore, QtWidgets, QtGui
from note_data import NoteData, NOTE_ID
from note_wnd import NoteWnd
from preferences import Preferences
from topic_manager import TopicManager
import logging

class NoteManager:
  def __init__(self, topicManager: TopicManager, preferences: Preferences):
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
    # TODO: Save preferences?

  @property
  def defaultNoteFontSize(self) -> int:
    return self.preferences.defaultFontSize

  @defaultNoteFontSize.setter
  def defaultNoteFontSize(self, size: int):
    self.preferences.defaultFontSize = size
    # TODO: Save preferences?

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

  def createNote(self, noteId: NOTE_ID) -> NoteWnd:
    # First, check that noteId is not already being used
    if noteId in self.noteWndDict:
      # If noteId does already exist, this is an error condition
      logging.error(f'[NoteManager.createNote] Note ID {noteId} already exists in the noteWndDict')
      return

    noteWnd = NoteWnd(self.topicManager)
    noteWnd.noteId = noteId

    # Add to noteWndDict
    self.noteWndDict[noteId] = noteWnd

    # TODO: Figure out how to set transparency (should this be done in NoteWnd?)

    return noteWnd

  def createPopulatedNote(self, noteData: NoteData):
    """ Creates a fully-populated note.  Used when loading notes from the database.
    """
    newNote = self.createNote(noteData.noteId)

    newNote.setNoteContents(noteData)

    newNote.showNote()
