from note_style import ENoteBackground, NoteStyle
from PySide6 import QtCore, QtWidgets, QtGui

kInvalidTopicId = 0
kDefaultTopicId = 1

# TODO: Since both notes and topics have some of the same properties (textColor, bgColor, bgType, and transparency),
#       maybe they should be refactored into a class.

class TopicData:
  """ Topic data from the database.
  """
  def __init__(self):
    self.id = kInvalidTopicId
    self.name = ''
    self.textColor = QtGui.QColor('black')
    self.bgColor = QtGui.QColor('yellow')
    self.bgType = 0
    self.transparency = 100


class Topic:
  def __init__(self, topicName):
    self.id = kInvalidTopicId
    self.topicName = topicName
    self.topicStyle = NoteStyle()

    # Use @properties for the functions that set and get various properties that are stored in NoteStyle

  @property
  def backgroundColor(self) -> QtGui.QColor:
    return self.topicStyle.backgroundColor

  @backgroundColor.setter
  def backgroundColor(self, color: QtGui.QColor):
    self.topicStyle.backgroundColor = color

  @property
  def backgroundType(self) -> ENoteBackground:
    return self.topicStyle.backgroundType

  @backgroundType.setter
  def backgroundType(self, type: ENoteBackground):
    self.topicStyle.backgroundType = type

  @property
  def textColor(self) -> QtGui.QColor:
    return self.topicStyle.textColor

  @textColor.setter
  def textColor(self, color: QtGui.QColor):
    self.topicStyle.textColor = color

  @property
  def transparency(self) -> int:
    return self.topicStyle.transparency

  @transparency.setter
  def transparency(self, value: int):
    self.topicStyle.transparency = value

