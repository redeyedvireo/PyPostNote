import datetime
from PySide6 import QtCore, QtWidgets, QtGui

# Type aliases
NOTE_ID = int
TOPIC_ID = int

kInvalidNote = -1
kInvalidTopic = -1

class NoteData:
  def __init__(self):
    self.noteId = kInvalidNote
    self.geometryData = None
    self.title = ''
    self.contentsData = ''
    self.addedTime = datetime.datetime.now()		# When created
    self.lastModifiedTime = datetime.datetime.now()		# When last modified
    self.topicId = 0
    self.usesOwnColors = False
    self.alwaysOnTop = False
    self.textColor = QtGui.QColor('black')
    self.bgColor = QtGui.QColor('yellow')
    self.bgType = 0
    self.transparency = 100

