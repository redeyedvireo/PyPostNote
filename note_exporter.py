from note_data import NoteData
import json
import base64

from topic import TopicData

class NoteExporter:
  def __init__(self):
    self.notes = []
    self.topics = []

  def addNote(self, noteData: NoteData):
    jsonNoteData = {}
    jsonNoteData['noteId'] = noteData.noteId
    jsonNoteData['title'] = noteData.title
    jsonNoteData['topicId'] = noteData.topicId
    jsonNoteData['posX'] = 0
    jsonNoteData['posY'] = 0
    jsonNoteData['width'] = 0
    jsonNoteData['height'] = 0
    jsonNoteData['geometry'] = base64.b64encode(noteData.geometryData.data()).decode('utf-8')
    jsonNoteData['contents'] = noteData.contentsData
    jsonNoteData['addedTime'] = noteData.addedTime.isoformat()
    jsonNoteData['lastModifiedTime'] = noteData.lastModifiedTime.isoformat()
    jsonNoteData['usesOwnColors'] = noteData.usesOwnColors
    jsonNoteData['alwaysOnTop'] = noteData.alwaysOnTop
    jsonNoteData['textColor'] = noteData.textColor.rgba()
    jsonNoteData['bgColor'] = noteData.bgColor.rgba()
    jsonNoteData['bgType'] = noteData.bgType.value
    jsonNoteData['transparency'] = noteData.transparency

    self.notes.append(jsonNoteData)

  def addTopic(self, topicData: TopicData):
    jsonTopicData = {}
    jsonTopicData['topicId'] = topicData.id
    jsonTopicData['topicName'] = topicData.name
    jsonTopicData['textColor'] = topicData.textColor.rgba()
    jsonTopicData['bgColor'] = topicData.bgColor.rgba()
    jsonTopicData['bgType'] = topicData.bgType.value
    jsonTopicData['transparency'] = topicData.transparency

    self.topics.append(jsonTopicData)

  def export(self, fileName: str):
    outputDoc = { 'notes': self.notes, 'topics': self.topics }
    jsonDoc = json.dumps(outputDoc)

    with open(fileName, 'w') as file:
      file.write(jsonDoc)
