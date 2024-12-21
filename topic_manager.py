from PySide6 import QtCore, QtWidgets, QtGui
from note_data import TOPIC_ID
from note_exporter import NoteExporter
from topic import Topic, TopicData, kDefaultTopicId
import logging

class TopicManager(QtCore.QObject):
  topicAdded = QtCore.Signal(Topic)
  topicUpdated = QtCore.Signal(Topic)
  topicDeleted = QtCore.Signal(TOPIC_ID)

  def __init__(self):
    super(TopicManager, self).__init__()
    self.topicMap: dict[TOPIC_ID, Topic] = {}      # Maps TOPIC_IDs to Topics

    self.createDefaultTopic()

  def createDefaultTopic(self):
    topic = Topic('Default')    # This creates a Topic with the default style (yellow background, black text)
    topic.id = kDefaultTopicId

    self.topicMap[kDefaultTopicId] = topic

  def createNewTopic(self, topicName: str) -> Topic:
    """Creates a new Topic, and gives it an ID, but does not store it in the Topic Map.

    Args:
        topicName (str): Topic name

    Returns:
        Topic: Created topic.
    """
    topic = Topic(topicName)      # This does not provide an ID
    topic.id = self.getFreeId()
    return topic

  def getTopic(self, topicId: TOPIC_ID) -> Topic | None:
    return self.topicMap[topicId] if topicId in self.topicMap else None

  def getTopicIds(self, alphabeticByTopicName: bool = False) -> list[TOPIC_ID]:
    """Returns a list of all topic IDs.

    Args:
        alphabeticByTopicName (bool): If true, the IDs will be returned such that the resulting
                                      topics will be in alphabetical order, by topic name

    Returns:
        list[TOPIC_ID]: List of topic IDs
    """
    topicIds = self.topicMap.keys()

    if not alphabeticByTopicName:
      return topicIds
    else:
      # Create a dictionary: [topicID, topicName]
      topicNameDict = {}
      for topicId in self.topicMap.keys():
        topicNameDict[topicId] = self.topicMap[topicId].topicName
      sortedTopicNameDict = dict(sorted(topicNameDict.items(), key=lambda x: x[1]))
      return sortedTopicNameDict.keys()

  def addTopicFromTopicData(self, topicData: TopicData):
    """Adds a topic to the list, from topic data.  This is generally used when reading topics from the database.

    Args:
        topicData (TopicData): Topic to add
    """
    # First, check that the topicId is not already being used.
    if topicData.id in self.topicMap:
      # Topic is already being used
      inUseTopic = self.topicMap[topicData.id]

      if inUseTopic.topicName == topicData.name:
        # If the topic names are the same, then assume this topic is the same as the one already in use
        return
      else:
        # Same ID but different topic names.  In this case, create a new topic ID
        topicData.id = self.getFreeId()

    newTopic = Topic(topicData.name)
    newTopic.topicData = topicData

    self.addTopic(newTopic, False)    # Don't add to the database, since this data has just come from the database

  def addTopic(self, topic: Topic, addToDatabase = False):
    """Adds a topic to the list`

    Args:
        topic: Topic to add
        addToDatabase (bool, optional): Whether to add this topic to the database. Defaults to False.
    """
    # First, check that the topicId is not already being used.
    if topic.id in self.topicMap:
      # Topic is already being used
      inUseTopic = self.topicMap[topic.id]

      if inUseTopic.topicName == topic.topicName:
        # If the topic names are the same, then assume this topic is the same as the one already in use
        return
      else:
        # Same ID but different topic names.  In this case, create a new topic ID
        topic.id = self.getFreeId()

    self.topicMap[topic.id] = topic

    if addToDatabase:
      self.topicAdded.emit(topic)

  def updateTopic(self, topic: Topic, updateDatabase = True):
    """Updates a topic.

    Args:
        topicId (TOPIC_ID): ID of topic to update
        topic (Topic): Topic to update
        updateDatabase (bool, optional): Whether to update the topic in the database. Defaults to True.
    """
    self.topicMap[topic.id] = topic     # Not sure if a deep copy needs to be done here

    if updateDatabase:
      self.topicUpdated.emit(topic)

  def deleteTopic(self, topicId: TOPIC_ID, updateDatabase = True):
    """Deletes a topic.

    Args:
        topicId (TOPIC_ID): ID of topic to delete
        updateDatabase (bool, optional): Whether to update the topic in the database. Defaults to True.
    """
    self.topicMap.pop(topicId, None)

    if updateDatabase:
      self.topicDeleted.emit(topicId)

  def getFreeId(self, addToDatabase = False):
    """Returns the next free ID to use when creating a new topic.
    """
    keysInUse = self.topicMap.keys()

    # There should always be at least one member in this list, the default topic (ID = 1),
    # but to be safe, we'll check first.
    highestKey = max(keysInUse) if len(keysInUse) > 0 else 2

    return highestKey + 1

  def addTopicsToExporter(self, exporter: NoteExporter):
    """Adds all topics to the exporter.

    Args:
        exporter: Exporter to add topics to
    """
    for topic in self.topicMap.values():
      exporter.addTopic(topic.topicData)
