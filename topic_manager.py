from note_data import TOPIC_ID
from topic import Topic, TopicData
import logging

class TopicManager:
  def __init__(self):
    self.topicMap = {}      # Maps TOPIC_IDs to Topics
  
  def getTopic(self, topicId: TOPIC_ID) -> Topic | None:
    return self.topicMap[topicId] if topicId in self.topicMap else None
  
  def addTopic(self, topicData: TopicData):
    # First, check that the topicId is not already being used.
    if topicData.id in self.topicMap:
      # Topic is already being used
      logging.error(f'[TopicManager.addTopic] addTopic called with pre-existing topic ID: {topicData.id}')
      return
    
    newTopic = Topic(topicData.name)
    newTopic.topicStyle.textColor = topicData.textColor
    newTopic.topicStyle.backgroundColor = topicData.bgColor
    newTopic.topicStyle.backgroundType = topicData.bgType
    newTopic.topicStyle.transparency = topicData.transparency

    self.topicMap[topicData.id] = newTopic
