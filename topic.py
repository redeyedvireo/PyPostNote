from note_style import ENoteBackground, NoteStyle
from PySide6 import QtCore, QtWidgets, QtGui

kInvalidTopicId = 0
kDefaultTopicId = 1


class TopicData:
  """ Topic data from the database.
  """
  def __init__(self):
    self.id = kInvalidTopicId
    self.name = ''
    self.textColor = QtGui.QColor('black')
    self.bgColor = QtGui.QColor('yellow')
    self.bgType = ENoteBackground.eSolid
    self.transparency = 100


class Topic:
  def __init__(self, topicName):
    self.id = kInvalidTopicId
    self.topicName = topicName
    self.topicStyle = NoteStyle()

  @property
  def topicData(self) -> TopicData:
    outTopicData = TopicData()

    outTopicData.id = self.id
    outTopicData.name = self.topicName
    outTopicData.textColor = self.topicStyle.textColor
    outTopicData.bgColor = self.topicStyle.backgroundColor
    outTopicData.bgType = self.topicStyle.backgroundType
    outTopicData.transparency = self.topicStyle.transparency

    return outTopicData

  @topicData.setter
  def topicData(self, topicData: TopicData):
    self.id = topicData.id
    self.topicName = topicData.name
    self.topicStyle.textColor = topicData.textColor
    self.topicStyle.backgroundColor = topicData.bgColor
    self.topicStyle.backgroundType = topicData.bgType
    self.topicStyle.transparency = topicData.transparency

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

