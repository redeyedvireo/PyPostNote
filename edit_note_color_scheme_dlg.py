from PySide6 import QtCore, QtWidgets, QtGui
from note_style import NoteStyle, ENoteBackground
from ui_edit_note_color_scheme_dlg import Ui_editNoteColorSchemeDlg

class EditNoteColorScheme(QtWidgets.QDialog):
  def __init__(self, noteStyle: NoteStyle, parent: QtWidgets.QWidget):
    super().__init__(parent)

    self.ui = Ui_editNoteColorSchemeDlg()
    self.ui.setupUi(self)

    self.ui.bgColorButton.colorChangedSignal.connect(self.updateSampleLabel)
    self.ui.textColorButton.colorChangedSignal.connect(self.updateSampleLabel)

    self.noteStyle = noteStyle

    self.populateControls()

  def populateControls(self):
    self.ui.typeCombo.addItem('Solid', ENoteBackground.eSolid)
    self.ui.typeCombo.addItem('Color Cylcing', ENoteBackground.eColorCycling)

    tempRow = self.ui.typeCombo.findData(self.noteStyle.backgroundType)
    if tempRow != -1:
      self.ui.typeCombo.setCurrentIndex(tempRow)

    self.ui.bgColorButton.setColor(self.noteStyle.backgroundColor)
    self.ui.textColorButton.setColor(self.noteStyle.textColor)
    self.ui.transparencySlider.setValue(self.noteStyle.transparency)
    self.ui.transparencyValueLabel.setText(f'{self.noteStyle.transparency}')

    self.updateSampleLabel()

  def updateSampleLabel(self):
    styleSheetStr = f'background-color: {self.ui.bgColorButton.getColor().name()}; color: {self.ui.textColorButton.getColor().name()}'
    self.ui.sampleLabel.setStyleSheet(styleSheetStr)

  @QtCore.Slot()
  def on_buttonBox_accepted(self):
    currentComboIndex = self.ui.typeCombo.currentIndex()
    self.noteStyle.backgroundType = self.ui.typeCombo.itemData(currentComboIndex)
    self.noteStyle.backgroundColor = self.ui.bgColorButton.getColor()
    self.noteStyle.textColor = self.ui.textColorButton.getColor()
    self.noteStyle.transparency = self.ui.transparencySlider.value()

  @QtCore.Slot()
  def on_transparencySlider_valueChanged(self):
    value = self.ui.transparencySlider.value()
    self.ui.transparencyValueLabel.setText(f'{value}')
