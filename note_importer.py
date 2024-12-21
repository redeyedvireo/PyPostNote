from PySide6 import QtGui
from note_data import NoteData
from note_style import ENoteBackground
from topic import TopicData
import json
import base64
import datetime


class NoteImporter:
  def __init__(self):
    self.notes = []
    self.topics = []

  def importNotes(self, filePath: str) -> tuple[list[NoteData], list[TopicData]] | bool:
    try:
      with open(filePath, 'r') as file:
        parsedContents = json.load(file)
        notes = parsedContents['notes']
        topics = parsedContents['topics']

        for note in notes:
          noteData = NoteData()
          noteData.noteId = note['noteId']
          noteData.title = note['title']
          noteData.topicId = note['topicId']
          # noteData.posX = note['posX']
          # noteData.posY = note['posY']
          # noteData.width = note['width']
          # noteData.height = note['height']
          noteData.geometryData = base64.b64decode(note['geometry'])
          noteData.contentsData = note['contents']
          noteData.addedTime = datetime.datetime.fromisoformat(note['addedTime'])
          noteData.lastModifiedTime = datetime.datetime.fromisoformat(note['lastModifiedTime'])
          noteData.usesOwnColors = note['usesOwnColors']
          noteData.alwaysOnTop = note['alwaysOnTop']
          noteData.textColor = QtGui.QColor.fromRgba(note['textColor'])
          noteData.bgColor = QtGui.QColor.fromRgba(note['bgColor'])
          noteData.bgType = ENoteBackground(int(note['bgType']))
          noteData.transparency = note['transparency']

          self.notes.append(noteData)

        for topic in topics:
          topicData = TopicData()
          topicData.id = topic['topicId']
          topicData.name = topic['topicName']
          topicData.textColor = QtGui.QColor.fromRgba(topic['textColor'])
          topicData.bgColor = QtGui.QColor.fromRgba(topic['bgColor'])
          topicData.bgType = ENoteBackground(int(topic['bgType']))
          topicData.transparency = topic['transparency']

          self.topics.append(topicData)

        return (self.notes, self.topics)

    except FileNotFoundError:
      print(f"File {self.filePath} not found.")
      return False
    except json.JSONDecodeError:
      print(f"Error decoding JSON from file {self.filePath}.")
      return False
