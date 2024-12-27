import datetime
from enum import Enum
from PySide6 import QtCore, QtWidgets, QtGui
from note_style import NoteStyle, ENoteBackground

class ENoteSizeEnum(Enum):
  eSmallNote = 0
  eMediumNote = 1
  eLargeNote = 2
  eExLargeNote = 3

# Type aliases
NOTE_ID = int
TOPIC_ID = int

kInvalidNote = -1

class NoteData:
  def __init__(self):
    self.noteId = kInvalidNote
    self.geometryData: QtCore.QByteArray = QtCore.QByteArray()
    self.title = ''
    self.contentsData = ''
    self.addedTime = datetime.datetime.now()		# When created
    self.lastModifiedTime = datetime.datetime.now()		# When last modified
    self.topicId = 0
    self.usesOwnColors = False
    self.alwaysOnTop = False
    self.textColor = QtGui.QColor('black')
    self.bgColor = QtGui.QColor('yellow')
    self.bgType = ENoteBackground(0)
    self.transparency = 100

  @property
  def noteStyle(self) -> NoteStyle:
    style = NoteStyle()
    style.backgroundColor = self.bgColor
    style.textColor = self.textColor
    style.backgroundType = self.bgType
    style.transparency = self.transparency

    return style

  @noteStyle.setter
  def noteStyle(self, noteStyle: NoteStyle):
    # TODO: Are deep copy operations needed when copying QColors?
    self.bgColor = noteStyle.backgroundColor
    self.textColor = noteStyle.textColor
    self.bgType = noteStyle.backgroundType
    self.transparency = noteStyle.transparency
