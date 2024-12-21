from PySide6 import QtCore, QtWidgets, QtGui
from ui_edit_toolbar import Ui_EditToolbar
from util import copyQSize
import logging

class EditToolbar(QtWidgets.QWidget):
  toolbarClosing = QtCore.Signal()
  fontSizeChanged = QtCore.Signal(int)
  fontFamilyChanged = QtCore.Signal(str)
  leftAlignTriggered = QtCore.Signal()
  centerAlignTriggered = QtCore.Signal()
  rightAlignTriggered = QtCore.Signal()
  boldTriggered = QtCore.Signal()
  italicTriggered = QtCore.Signal()
  underlineTriggered = QtCore.Signal()
  horizontalLineTriggered = QtCore.Signal()
  bulletListTriggered = QtCore.Signal()
  numberListTriggered = QtCore.Signal()
  tableTriggered = QtCore.Signal(int, int)      # Number of rows, number of columns

  def __init__(self, parent: QtWidgets.QWidget):
    super(EditToolbar, self).__init__(parent, QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)

    self.ui = Ui_EditToolbar()
    self.ui.setupUi(self)

  def closeEvent(self, event):
    super(EditToolbar, self).closeEvent(event)
    self.toolbarClosing.emit()

  def showEditToolbar(self, pos: QtCore.QPoint, size: QtCore.QSize, textCursor: QtGui.QTextCursor):
    self.moveEditToolbar(pos, copyQSize(size))
    self.setFontCombos(textCursor)
    self.show()

  def moveEditToolbar(self, pos: QtCore.QPoint, size: QtCore.QSize):
    kToolbarHeight = 80   # Approximate
    kToolbarWidth = 270   # Approximate

    # Determine the screen size on which this window is on
    screen = self.screen()
    screenRect = screen.availableGeometry()

    y = 0
    x = 0

    # Try to put the toolbar above the note
    if pos.y() > kToolbarHeight:
      y = pos.y() - kToolbarHeight
      x = pos.x()
    elif pos.y() + size.height() + 30 < screenRect.bottom() - kToolbarHeight:
      # Put toolbar below note
      y = pos.y() + size.height() + 40    # Account for window frame
      x = pos.x()
    elif pos.x() > kToolbarWidth:
      # Put toolbar to the left of the note
      y = pos.y()
      x = pos.x() - kToolbarWidth
    elif pos.x() + size.width() + 10 < screenRect.right():
      # Put toolbar to the right of the note
      y = pos.y()
      x = pos.x() + size.width() + 20     # Account for window frame
    else:
      # Should never get here
      return

    self.move(x, y)

  def setFontCombos(self, textCursor: QtGui.QTextCursor):
    charFormat = textCursor.charFormat()
    self.setFontFamily(charFormat.fontFamily())
    self.setFontSize(charFormat.fontPointSize())

  def setFontFamily(self, family: str):
    if len(family) > 0:
      index = self.ui.fontComboBox.findText(family)

      if index != -1:
        self.ui.fontComboBox.setCurrentIndex(index)
        self.populatePointSizesCombo()

  def populatePointSizesCombo(self):
    curFontFamily = self.ui.fontComboBox.currentText()

    self.ui.sizeComboBox.clear()

    fontSizeList = QtGui.QFontDatabase.pointSizes(curFontFamily)

    if len(fontSizeList) == 0:
      # For some reason there are no font sizes with this font.  Try using standard Sizes.
      fontSizeList = QtGui.QFontDatabase.standardSizes()

    for size in fontSizeList:
      self.ui.sizeComboBox.addItem(f'{size}')

  def setFontSize(self, fontSize: int):
    intFontSize = int(fontSize)
    if intFontSize > 0:
      index = self.ui.sizeComboBox.findText(f'{intFontSize}')

      if index != -1:
        self.ui.sizeComboBox.setCurrentIndex(index)

  @QtCore.Slot(int)
  def on_sizeComboBox_activated(self, index: int):
    fontText = self.ui.sizeComboBox.itemText(index)

    if len(fontText) > 0:
      self.fontSizeChanged.emit(int(fontText))

  @QtCore.Slot(int)
  def on_fontComboBox_activated(self, index: int):
    self.populatePointSizesCombo()

    fontFamily = self.ui.fontComboBox.currentText()
    self.fontFamilyChanged.emit(fontFamily)

  @QtCore.Slot()
  def on_leftAlignButton_clicked(self):
    self.leftAlignTriggered.emit()
    self.ui.leftAlignButton.clearFocus()
    self.clearFocus()

  @QtCore.Slot()
  def on_centerAlignButton_clicked(self):
    self.centerAlignTriggered.emit()
    self.ui.centerAlignButton.clearFocus()
    self.clearFocus()

  @QtCore.Slot()
  def on_rightAlignButton_clicked(self):
    self.rightAlignTriggered.emit()
    self.ui.rightAlignButton.clearFocus()
    self.clearFocus()

  @QtCore.Slot()
  def on_boldButton_clicked(self):
    self.boldTriggered.emit()
    self.ui.boldButton.clearFocus()
    self.clearFocus()

  @QtCore.Slot()
  def on_italicButton_clicked(self):
    self.italicTriggered.emit()
    self.ui.italicButton.clearFocus()
    self.clearFocus()

  @QtCore.Slot()
  def on_underlineButton_clicked(self):
    self.underlineTriggered.emit()
    self.ui.underlineButton.clearFocus()
    self.clearFocus()

  @QtCore.Slot()
  def on_horizontalLineButton_clicked(self):
    self.horizontalLineTriggered.emit()
    self.ui.horizontalLineButton.clearFocus()
    self.clearFocus()

  @QtCore.Slot()
  def on_bulletListInsertButton_clicked(self):
    self.bulletListTriggered.emit()
    self.ui.bulletListInsertButton.clearFocus()
    self.clearFocus()

  @QtCore.Slot()
  def on_numberListInsertButton_clicked(self):
    self.numberListTriggered.emit()
    self.ui.numberListInsertButton.clearFocus()
    self.clearFocus()

  @QtCore.Slot()
  def on_tableInsertButton_clicked(self):
    # TODO: Need a dialog to ask how many rows and columns
    self.tableTriggered.emit(2, 2)
    self.ui.tableInsertButton.clearFocus()
    self.clearFocus()

