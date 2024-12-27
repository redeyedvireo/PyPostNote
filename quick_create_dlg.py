from PySide6 import QtCore, QtWidgets, QtGui
from topic_manager import TopicManager
from ui_quick_create_dlg import Ui_QuickCreateDlg
from util import createTopicIcon
from note_data import ENoteSizeEnum

kIconWidth = 40
kIconHeight	=	20

class QuickCreateDlg(QtWidgets.QDialog):
  showEditTopicsDialogSignal = QtCore.Signal()

  def __init__(self, topicManager: TopicManager, parent: QtWidgets.QWidget):
    super().__init__(parent)

    self.ui = Ui_QuickCreateDlg()
    self.ui.setupUi(self)

    self.topicManager = topicManager

    self.ui.topicCombo.view().setIconSize(QtCore.QSize(kIconWidth, kIconHeight))

    self.populateTopicCombo()

    # TODO: Get default settings from somewhere

  def populateTopicCombo(self):
    self.ui.topicCombo.clear()
    topicIds = self.topicManager.getTopicIds()

    for topicId in topicIds:
      topic = self.topicManager.getTopic(topicId)

      # Create an icon indicating the topic's colors
      tempIcon = createTopicIcon(kIconWidth, kIconHeight, topic.topicStyle.backgroundColor, topic.topicStyle.textColor, 'Text')

      self.ui.topicCombo.addItem(tempIcon, topic.topicName, topicId)

    self.ui.topicCombo.model().sort(0)

  def getTopicId(self):
    return self.ui.topicCombo.currentData()

  def getNoteTitle(self):
    return self.ui.titleEdit.text()

  def getNoteSize(self):
    sizeIndex = self.ui.sizeCombo.currentIndex()
    return ENoteSizeEnum(sizeIndex)

  @QtCore.Slot()
  def on_topicsButton_clicked(self):
    self.showEditTopicsDialogSignal.emit()

  @QtCore.Slot()
  def on_buttonBox_accepted(self):
    self.accept()