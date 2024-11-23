from note_data import TOPIC_ID
from topic import Topic

class TopicManager:
  def __init__(self):
    self.topicMap = {}      # Maps TOPIC_IDs to Topics
  
  def getTopic(self, topicId: TOPIC_ID) -> Topic:
    # TODO: Return the desired Topic
    print(f'topic ID: {topicId}')
    return Topic('Undefined Topic')     # TODO: Remove this