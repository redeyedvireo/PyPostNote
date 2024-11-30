from PySide6 import QtCore, QtWidgets, QtGui
from button_bar_widget import ButtonBarWidget
from text_edit import TextEdit
from ui_note_wnd import Ui_NoteWnd
from note_data import NoteData, kInvalidNote, kInvalidTopic
from note_style import NoteStyle
from topic_manager import TopicManager
import datetime
import logging

class NoteWnd(QtWidgets.QWidget):
  # TODO: Also pass in database
  def __init__(self, topicManager: TopicManager, parent: QtWidgets.QWidget = None):
    super(NoteWnd, self).__init__(parent, QtCore.Qt.Tool | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)

    self.ui = Ui_NoteWnd()
    self.ui.setupUi(self)

    self.topicManager = topicManager

    self.noteId = kInvalidNote
    self.noteCreationTime = datetime.datetime.now()
    self.lastUpdateTime = datetime.datetime.now()
    self.topicId = kInvalidTopic
    self.noteUsesOwnColorScheme = False
    self.alwaysOnTop = False

    self.noteStyle = NoteStyle()

    self.setMinimumSize(QtCore.QSize(40, 20))
    self.updateNote()

    QtCore.QTimer.singleShot(100, self.createButtonBarWidget)

  def showNote(self):
    self.show()

    # Activate the note
    self.activateWindow()
    self.raise_()

  def updateNote(self):
    """ Updates the note's appearance. """
    # Most notes will take their appearance settings from the topic to which they belong
    topic = self.topicManager.getTopic(self.topicId)

    bgColor = QtGui.QColor("yellow")
    textColor = QtGui.QColor("black")
    transparency = 100

    if topic is not None:
      textColor = topic.topicStyle.textColor
      bgColor = topic.topicStyle.backgroundColor
      transparency = topic.topicStyle.transparency
    else:
      # Should not happen
      logging.error(f'[NoteWnd.updateNote] Note topicID is not found in TopicManager: {self.topicId}')

    if self.noteUsesOwnColorScheme or topic is None:
      textColor = self.noteStyle.textColor
      bgColor = self.noteStyle.backgroundColor
      transparency = self.noteStyle.transparency

    textCursor = self.ui.textEdit.textCursor()
    curpos = textCursor.position()

    self.ui.textEdit.selectAll()
    self.ui.textEdit.setTextColor(textColor)
    textCursor.setPosition(curpos)
    self.ui.textEdit.setTextCursor(textCursor)

    self.ui.textEdit.setStyleSheet(f'QTextEdit {{ color: {textColor.name()}; background-color: {bgColor.name()} }}')
    self.setNoteTransparency(transparency)
    self.setAlwaysOnTopness(self.alwaysOnTop)

  def setNoteContents(self, noteData: NoteData):
    self.setWindowTitle(noteData.title)
    self.setNoteGeometry(noteData.geometryData)
    self.ui.textEdit.setHtml(noteData.contentsData)
    self.noteId = noteData.noteId
    self.noteCreationTime = noteData.addedTime
    self.lastUpdateTime = noteData.lastModifiedTime
    self.topicId = noteData.topicId
    self.noteUsesOwnColorScheme = noteData.usesOwnColors
    self.alwaysOnTop = noteData.alwaysOnTop

    self.noteStyle.textColor = noteData.textColor
    self.noteStyle.backgroundColor = noteData.bgColor
    self.noteStyle.backgroundType = noteData.bgType
    self.noteStyle.transparency = noteData.transparency

    self.updateNote()


  def setNoteTitle(self, title: str):
    self.setWindowTitle(title)

  def setNoteGeometry(self, geometry: QtCore.QByteArray):
    # TODO: I think this is what causes the issue where all windows appear in the center of the screen.  There needs to be
    #       some way of checking if the note's window exists, and if the note's rectangle is within this window.  It might
    #       be good to store the note's geometry in a different way in the database.  To do so, add new fields to the database,
    #       (x, y, width, height), but keep the existing geometry field to preserve backward compatibility.  Then, continue to
    #       store note geometry in the legacy field, but also store it in new fields.  When reading, see if the new field has
    #       been initialized, and if so, use that; otherwise use the old geometry field.
    self.restoreGeometry(geometry)

  def setNoteTransparency(self, value: int):
    self.setWindowOpacity(float(value) / 100)

  def setAlwaysOnTopness(self, alwaysOnTop: bool):
    self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, alwaysOnTop)

  def createButtonBarWidget(self):
    self.buttonBarWidget = ButtonBarWidget(self.ui.textEdit.rect(), self)
    self.topicMenu = QtWidgets.QMenu('Topic', self)
    self.topicMenu.aboutToShow.connect(self.populateTopicMenu)
    self.buttonBarWidget.setTopicMenu(self.topicMenu)

    # TODO: Connect signals (see C++ version)

  @QtCore.Slot()
  def populateTopicMenu(self):
    self.topicMenu.clear()

    topicIdList = self.topicManager.getTopicIds()

    for topicId in topicIdList:
      topic = self.topicManager.getTopic(topicId)

      if topic is not None:
        newAction = self.topicMenu.addAction(topic.topicName)
        newAction.setCheckable(True)

        if self.topicId == topicId:
          # Check the current topic
          newAction.setChecked(True)

        newAction.setData(topicId)
        newAction.triggered.connect(self.onSetNewTopic)
      else:
        logging.error(f'[NoteWnd.populateTopicMenu] topic ID {topicId} not found in TopicManager')

  def onSetNewTopic(self):
    sender = self.sender()
    if type(sender) is QtGui.QAction:
      self.topicId = sender.data()
      # TODO: Update the note in the database
      # self.db.updateNote(self)
      self.updateNote()
