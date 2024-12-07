from PySide6 import QtCore, QtWidgets, QtGui
from note_data import TOPIC_ID
from topic import Topic, kDefaultTopicId, kInvalidTopicId
from topic_manager import TopicManager
from ui_edit_topic_addr_dlg import Ui_EditTopicAttrDlg
from note_style import ENoteBackground

class EditTopicAttrDlg(QtWidgets.QDialog):
  def __init__(self, topicManager: TopicManager, parent: QtWidgets.QWidget, topicId: TOPIC_ID = None):
    super().__init__(parent)

    self.ui = Ui_EditTopicAttrDlg()
    self.ui.setupUi(self)

    self.topicManager = topicManager
    self.topicId = topicId

    if topicId is not None:
      self.topic = self.topicManager.getTopic(topicId)
    else:
      # If topic ID is None, a new topic will be created
      self.topic = self.topicManager.createNewTopic('New Topic')

    self.ui.textColorButton.colorChangedSignal.connect(self.updateSampleLabel)
    self.ui.bgColorButton.colorChangedSignal.connect(self.updateSampleLabel)

    self.populateControls()

  def getTopic(self):
    return self.topic

  def populateControls(self):
    self.ui.topicEdit.setText(self.topic.topicName)

    # Init background type combo
    self.ui.typeCombo.addItem('Solid', ENoteBackground.eSolid)
    self.ui.typeCombo.addItem('Color Cycling', ENoteBackground.eColorCycling)

    tempRow = self.ui.typeCombo.findData(self.topic.topicStyle.backgroundType)

    if tempRow != -1:
      self.ui.typeCombo.setCurrentIndex(tempRow)

    self.ui.bgColorButton.setColor(self.topic.topicStyle.backgroundColor)
    self.ui.textColorButton.setColor(self.topic.topicStyle.textColor)

    self.ui.transparencySlider.setValue(self.topic.topicStyle.transparency)
    self.ui.transparencyValueLabel.setText(f'{self.topic.topicStyle.transparency}')

    self.updateSampleLabel()

  def updateSampleLabel(self):
    styleSheetStr = f'background-color: {self.ui.bgColorButton.getColor().name()}; color: {self.ui.textColorButton.getColor().name()};'
    self.ui.sampleLabel.setStyleSheet(styleSheetStr)

  @QtCore.Slot(int)
  def on_transparencySlider_sliderMoved(self, value: int):
    self.ui.transparencyValueLabel.setText(f'{value}')

  @QtCore.Slot()
  def on_buttonBox_accepted(self):
    self.topic.topicName = self.ui.topicEdit.text()

    currentComboIndex = self.ui.typeCombo.currentIndex()
    type = self.ui.typeCombo.itemData(currentComboIndex)
    self.topic.backgroundType = type

    self.topic.backgroundColor = self.ui.bgColorButton.getColor()
    self.topic.textColor = self.ui.textColorButton.getColor()
    self.topic.transparency = self.ui.transparencySlider.value()
