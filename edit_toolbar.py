from PySide6 import QtCore, QtWidgets, QtGui
from ui_edit_toolbar import Ui_EditToolbar
import logging

class EditToolbar(QtWidgets.QWidget):
  toolbarClosing = QtCore.Signal()
  fontSizeChanged = QtCore.Signal(int)
  fontFamilyChanged = QtCore.Signal(str)

  def __init__(self, parent: QtWidgets.QWidget):
    super(EditToolbar, self).__init__(parent, QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)

    self.ui = Ui_EditToolbar()
    self.ui.setupUi(self)

  def closeEvent(self, event):
    super(EditToolbar, self).closeEvent(event)
    self.toolbarClosing.emit()

  def showEditToolbar(self, pos: QtCore.QPoint, size: QtCore.QSize):
    self.moveEditToolbar(pos, size)
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
    if fontSize > 0:
      index = self.ui.sizeComboBox.findText(f'{fontSize}')

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
