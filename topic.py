from note_style import NoteStyle
from PySide6 import QtCore, QtWidgets, QtGui

# TODO: Since both notes and topics have some of the same properties (textColor, bgColor, bgType, and transparency),
#       maybe they should be refactored into a class.

class TopicData:
  """ Topic data from the database.
  """
  def __init__(self):
    self.id = 0
    self.name = ''
    self.textColor = QtGui.QColor('black')
    self.bgColor = QtGui.QColor('yellow')
    self.bgType = 0
    self.transparency = 100


class Topic:
  def __init__(self, topicName):
    self.topicName = topicName
    self.topicStyle = NoteStyle()

    # Use @properties for the functions that set and get various properties that are stored in NoteStyle