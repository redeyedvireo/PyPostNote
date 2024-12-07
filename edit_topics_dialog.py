from PySide6 import QtCore, QtWidgets, QtGui
from note_data import TOPIC_ID
from ui_edit_topics_dialog import Ui_EditTopicsDialog
from topic import Topic, kDefaultTopicId, kInvalidTopicId
from note_manager import NoteManager
from topic_manager import TopicManager
from edit_topic_attr_dlg import EditTopicAttrDlg

kIconWidth = 40
kIconHeight	=	20

class EditTopicsDialog(QtWidgets.QDialog):

  def __init__(self, parent: QtWidgets.QWidget, topicManager: TopicManager, noteManager: NoteManager):
    super().__init__(parent)

    self.ui = Ui_EditTopicsDialog()
    self.ui.setupUi(self)

    self.topicManager = topicManager
    self.noteManager = noteManager

    self.ui.topicListWidget.setIconSize(QtCore.QSize(kIconWidth, kIconHeight))
    self.populateTopicList()

  def populateTopicList(self):
    topicIds = self.topicManager.getTopicIds()

    for topicId in topicIds:
      topic = self.topicManager.getTopic(topicId)
      self.addTopicToList(topic)

  def addTopicToList(self, topic: Topic):
    newItem = QtWidgets.QListWidgetItem()
    newItem.setData(QtCore.Qt.ItemDataRole.UserRole, topic.id)

    self.setTopicContents(topic, newItem)

    if topic.id == kDefaultTopicId:
      # The default topic cannot be edited, so remove the Qt.ItemIsSelectable flag
      newItem.setFlags(newItem.flags() & ~QtCore.Qt.ItemFlag.ItemIsSelectable)

    self.ui.topicListWidget.addItem(newItem)

  def setTopicContents(self, topic: Topic, listWidgetItem: QtWidgets.QListWidgetItem):
    listWidgetItem.setText(topic.topicName)

    # Add an icon indicating the topic's colors
    tempPixmap = QtGui.QPixmap(kIconWidth, kIconHeight)

    tempPixmap.fill(topic.topicStyle.backgroundColor)

    painter = QtGui.QPainter(tempPixmap)
    painter.setPen(topic.topicStyle.textColor)
    painter.drawText(QtCore.QRect(0, 0, kIconWidth, kIconHeight), \
                     QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter, \
                      'Text')
    painter.end()

    tempIcon = QtGui.QIcon(tempPixmap)

    listWidgetItem.setIcon(tempIcon)

  def updateTopicInList(self, topic: Topic, topicListItem: QtWidgets.QListWidgetItem):
    self.setTopicContents(topic, topicListItem)

  @QtCore.Slot()
  def on_addButton_clicked(self):
    dlg = EditTopicAttrDlg(self.topicManager, self)

    result = dlg.exec_()

    if result == QtWidgets.QDialog.DialogCode.Accepted:
      newTopic = dlg.getTopic()
      if newTopic is not None:
        self.addTopicToList(newTopic)
        self.topicManager.addTopic(newTopic, True)

  @QtCore.Slot()
  def on_editButton_clicked(self):
    selectedItems = self.ui.topicListWidget.selectedItems()
    if len(selectedItems) == 0:
      return

    currentItem = self.ui.topicListWidget.currentItem()

    topicId = TOPIC_ID(currentItem.data(QtCore.Qt.ItemDataRole.UserRole))

    dlg = EditTopicAttrDlg(self.topicManager, self, topicId)

    result = dlg.exec_()

    if result == QtWidgets.QDialog.DialogCode.Accepted:
      topic = dlg.getTopic()

      self.topicManager.updateTopic(topic, True)
      self.updateTopicInList(topic, currentItem)

  @QtCore.Slot()
  def on_deleteButton_clicked(self):
    currentItem = self.ui.topicListWidget.currentItem()
    topicId = TOPIC_ID(currentItem.data(QtCore.Qt.ItemDataRole.UserRole))

    if topicId == kDefaultTopicId:
      return      # Can't delete the default topic

    reply = QtWidgets.QMessageBox.question(self, 'Delete Topic',
                                           "Once deleted, a topic cannot be recovered.  All notes with this topic will be set to the Default topic.  Are you sure you want to delete this topic?")

    if reply == QtWidgets.QMessageBox.StandardButton.No:
      return

    curRow = self.ui.topicListWidget.currentRow()
    item = self.ui.topicListWidget.takeItem(curRow)

    self.topicManager.deleteTopic(topicId, True)

    # TODO: Scan through all notes and for any note that uses this topic, set that note's topic to Default
    allNoteIds = self.noteManager.allNoteIds()

    for noteId in allNoteIds:
      noteWnd = self.noteManager.getNote(noteId)
      if noteWnd.topicId == topicId:
        noteWnd.topicId = kDefaultTopicId
