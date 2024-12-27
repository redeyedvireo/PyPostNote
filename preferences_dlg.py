from PySide6 import QtCore, QtWidgets, QtGui
from note_manager import NoteManager
from preferences import Preferences
from ui_preferences_dlg import Ui_PreferencesDlg

class PreferencesDlg(QtWidgets.QDialog):
  def __init__(self, noteManager: NoteManager, preferences: Preferences, parent: QtWidgets.QWidget):
    super().__init__(parent)

    self.ui = Ui_PreferencesDlg()
    self.ui.setupUi(self)

    self.noteManager = noteManager
    self.preferences = preferences

    self.populateControls()

  def populateControls(self):
    defaultFontFamily = self.preferences.defaultFontFamily

    index = self.ui.fontComboBox.findText(defaultFontFamily)
    if index != -1:
      self.ui.fontComboBox.setCurrentIndex(index)

    fontDatabase = QtGui.QFontDatabase()

    # Populate default font size combo box
    self.ui.fontSizeComboBox.clear()
    fontSizeList = fontDatabase.pointSizes(defaultFontFamily)

    for fontSize in fontSizeList:
      fontSizeStr = f'{fontSize}'
      self.ui.fontSizeComboBox.addItem(fontSizeStr)

    # Set the value for the default font size combo box
    defaultFontSize = self.preferences.defaultFontSize
    index = self.ui.fontSizeComboBox.findText(f'{defaultFontSize}')

    if index == -1:
      # Default font size not found, so search for the first size that is larger
      # than the given font size
      for i in range(self.ui.fontSizeComboBox.count()):
        fontSizeStr = self.ui.fontSizeComboBox.itemText(i)
        if len(fontSizeStr) == 0:
          continue

        curFontSize = int(fontSizeStr)

        if curFontSize >= defaultFontSize:
          self.ui.fontSizeComboBox.setCurrentIndex(i)
          break
    else:
      self.ui.fontSizeComboBox.setCurrentIndex(index)

    # Autosave time
    self.ui.autosaveSpinBox.setValue(self.preferences.autoSaveMinutes)

    # Double-click action
    self.ui.doubleClickActionComboBox.setCurrentIndex(int(self.preferences.doubleClickAction))

    # Auto-shutdown enable
    self.ui.autoShutdownCheckBox.setChecked(self.preferences.autoShutdownEnabled)

    # Auto-shutdown time
    self.ui.shutdownTimeEdit.setTime(QtCore.QTime.fromString(self.preferences.autoShutdownTime, 'hh:mm ap'))

    self.upddateAutoShutdownVisibility()

  def upddateAutoShutdownVisibility(self):
    self.ui.shutdownTimeEdit.setEnabled(self.ui.autoShutdownCheckBox.isChecked())

  @QtCore.Slot()
  def on_autoShutdownCheckBox_clicked(self):
    self.upddateAutoShutdownVisibility()

  @QtCore.Slot()
  def on_buttonBox_accepted(self):
    curFont = self.ui.fontComboBox.currentFont()
    self.preferences.defaultFontFamily = curFont.family()

    fontSizeStr = self.ui.fontSizeComboBox.currentText()
    fontSize = int(fontSizeStr)
    self.preferences.defaultFontSize = fontSize

    # Auto-save time
    self.preferences.autoSaveMinutes = self.ui.autosaveSpinBox.value()

    # Double-click action
    self.preferences.doubleClickAction = self.ui.doubleClickActionComboBox.currentIndex()   # TODO: Will this set the Enum properly?

    # Auto-shutdown enable
    self.preferences.autoShutdownEnabled = self.ui.autoShutdownCheckBox.isChecked()

    # Auto-shutdown time
    shutdownTime = self.ui.shutdownTimeEdit.time().toString('hh:mm ap')
    self.preferences.autoShutdownTime = shutdownTime

    self.preferences.writePrefsFile()
