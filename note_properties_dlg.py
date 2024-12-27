from PySide6 import QtCore, QtWidgets, QtGui
from edit_note_color_scheme_dlg import EditNoteColorScheme
from note_data import NoteData
from topic_manager import TopicManager
from ui_note_properties_dlg import Ui_notePropertiesDialog
from util import createTopicIcon, formatDateAndTime
import datetime

kIconWidth = 40
kIconHeight = 20

class NotePropertiesDlg(QtWidgets.QDialog):
  showEditTopicsDialogSignal = QtCore.Signal()

  def __init__(self, topicManager: TopicManager, noteData: NoteData, parent: QtWidgets.QWidget):
    super().__init__(parent)

    self.ui = Ui_notePropertiesDialog()
    self.ui.setupUi(self)

    self.noteData = noteData
    self.topicManager = topicManager

    self.populateControls(self.noteData)

  def populateControls(self, noteData: NoteData):
    self.ui.topicCombo.view().setIconSize(QtCore.QSize(kIconWidth, kIconHeight + 4))
    self.populateTopicCombo()

    self.ui.createdWhenLabel.setText(formatDateAndTime(noteData.addedTime))
    self.ui.titleEdit.setText(noteData.title)
    topicIdIndex = self.ui.topicCombo.findData(noteData.topicId)
    self.ui.topicCombo.setCurrentIndex(topicIdIndex)
    self.ui.alwaysOnTopCheckBox.setChecked(noteData.alwaysOnTop)
    self.ui.usesOwnColorsRadio.setChecked(noteData.usesOwnColors)
    self.ui.editColorSchemeButton.setEnabled(noteData.usesOwnColors)

  def populateTopicCombo(self):
    self.ui.topicCombo.clear()
    topicIds = self.topicManager.getTopicIds()

    for topicId in topicIds:
      topic = self.topicManager.getTopic(topicId)

      # Create an icon indicating the topic's colors
      tempIcon = createTopicIcon(kIconWidth, kIconHeight, topic.topicStyle.backgroundColor, topic.topicStyle.textColor, 'Text')

      self.ui.topicCombo.addItem(tempIcon, topic.topicName, topicId)

    self.ui.topicCombo.model().sort(0)

  def setNoteCreationTime(self, creationTime: datetime.datetime):
    self.ui.createdWhenLabel.setText()

  @QtCore.Slot()
  def on_editTopicsButton_clicked(self):
    self.showEditTopicsDialogSignal.emit()

    # We might not be able to edit topics here, because we can't get to the note manager, because
    # this dialog is launched from NoteWnd, which does not have access to the note manager (in order
    # to avoid a circular reference.)
    # It may, however, be possible to use a signal to launch it somehow, but this will be tricky because
    # the Postnote object doesn't know about this dialog; only the dialog's parent (NoteWnd) knows about it,
    # but NoteWnd doesn't know about the Note Manager (which is needed to edit topics, because if a topic
    # is deleted, all notes must be traversed so that any note that was using the deleted topic needs to
    # have its topic changed to the default topic.)

  @QtCore.Slot()
  def on_buttonBox_accepted(self):
    self.noteData.lastModifiedTime = datetime.datetime.now()      # This counts as a modification
    self.noteData.title = self.ui.titleEdit.text()
    self.noteData.topicId = self.ui.topicCombo.currentData()
    self.noteData.alwaysOnTop = self.ui.alwaysOnTopCheckBox.isChecked()
    self.noteData.usesOwnColors = self.ui.usesOwnColorsRadio.isChecked()

  @QtCore.Slot()
  def on_editColorSchemeButton_clicked(self):
    dlg = EditNoteColorScheme(self.noteData.noteStyle, self)

    result = dlg.exec_()

    if result == QtWidgets.QDialog.DialogCode.Accepted:
      self.noteData.noteStyle = dlg.noteStyle
