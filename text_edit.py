from PySide6 import QtCore, QtWidgets, QtGui

from edit_toolbar import EditToolbar

class TextEdit(QtWidgets.QTextEdit):
  TE_GainedFocus = QtCore.Signal()
  TE_LostFocus = QtCore.Signal()

  def __init__(self, parent):
    super(TextEdit, self).__init__(parent)
    self.theParent: QtWidgets.QWidget = parent
    self.editToolbar = None
    self.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)

    self.selectionChanged.connect(self.on_selectionChanged)
    self.cursorPositionChanged.connect(self.on_cursorPositionChanged)

  def setDefaultFont(self, fontFamily: str, fontSize: int):
    if fontSize < 3 or len(fontFamily) == 0:
      return

    tempFont = QtGui.QFont(fontFamily, fontSize)

    self.document().setDefaultFont(tempFont)

  def contextMenuEvent(self, event: QtGui.QContextMenuEvent):
    # super().contextMenuEvent(event)

    menu = self.createStandardContextMenu()

    if self.textCursor().hasSelection():
      menu.addSeparator()

      formatMenu = QtWidgets.QMenu()

      formatMenu.setTitle('Format')

      formatMenu.addAction('Bold', self.onBoldTriggered)
      formatMenu.addAction('Italic', self.onItalicTriggered)
      formatMenu.addAction('Underline', self.onUnderlineTriggered)

      menu.addMenu(formatMenu)

    menu.addSeparator()

    menu.addAction('Edit Toolbar', self.onEditToolbarTriggered)
    menu.addAction('Entire Note to Default Font', self.onToDefaultFontTriggered)

    menu.exec_(event.globalPos())

  def focusInEvent(self, event: QtGui.QFocusEvent):
    super(TextEdit, self).focusInEvent(event)

    self.updateFontControls()
    self.TE_GainedFocus.emit()

  def focusOutEvent(self, event: QtGui.QFocusEvent):
    super(TextEdit, self).focusOutEvent(event)

    self.TE_LostFocus.emit()

  def insertFromMimeData(self, source: QtCore.QMimeData):
    if source.hasHtml():
      # Covert it to a plain text object
      plainText = source.text()

      newMimeData = QtCore.QMimeData()
      newMimeData.setText(plainText)
      super(TextEdit, self).insertFromMimeData(newMimeData)
      return
    else:
      # Call the base class
      return super(TextEdit, self).insertFromMimeData(source)

  def updateFontControls(self):
    if self.editToolbar is None:
      return

    selectionCursor = self.textCursor()
    selectionFormat = selectionCursor.charFormat()

    fontFamily = selectionFormat.fontFamily()
    self.editToolbar.setFontFamily(fontFamily)

    fontSize = selectionFormat.fontPointSize()
    self.editToolbar.setFontSize(fontSize)

  def getCursorAndSelectionFormat(self) -> tuple[QtGui.QTextCursor, QtGui.QTextCharFormat]:
    selectionCursor = self.textCursor()
    selectionFormat = selectionCursor.charFormat()
    return (selectionCursor, selectionFormat)

  def mergeCharFormat(self, tempCharFormat: QtGui.QTextCharFormat, selectionCursor: QtGui.QTextCursor):
    selectionCursor.mergeCharFormat(tempCharFormat)
    self.setTextCursor(selectionCursor)

  def getCursorAndBlockFormat(self) -> tuple[QtGui.QTextCursor, QtGui.QTextBlockFormat]:
    selectionCursor = self.textCursor()
    selectionFormat = selectionCursor.blockFormat()
    return (selectionCursor, selectionFormat)

  def setBlockFormat(self, selectionCursor: QtGui.QTextCursor, selectionFormat: QtGui.QTextBlockFormat):
    selectionCursor.setBlockFormat(selectionFormat)
    self.setTextCursor(selectionCursor)

  def getCursorAndListFormat(self) -> tuple[QtGui.QTextCursor, QtGui.QTextListFormat]:
    return (self.textCursor(), QtGui.QTextListFormat())

  def onEditToolbarTriggered(self):
    self.editToolbar = EditToolbar(self.parent())
    self.editToolbar.showEditToolbar(self.theParent.pos(), self.theParent.size())

    self.editToolbar.toolbarClosing.connect(self.onToolbarClosing)
    self.editToolbar.fontSizeChanged.connect(self.onFontSizeChanged)
    self.editToolbar.fontFamilyChanged.connect(self.onFontFamilyChanged)
    self.editToolbar.leftAlignTriggered.connect(self.onLeftAlignTriggered)
    self.editToolbar.centerAlignTriggered.connect(self.onCenterAlignTriggered)
    self.editToolbar.rightAlignTriggered.connect(self.onRightAlignTriggered)
    self.editToolbar.boldTriggered.connect(self.onBoldTriggered)
    self.editToolbar.italicTriggered.connect(self.onItalicTriggered)
    self.editToolbar.underlineTriggered.connect(self.onUnderlineTriggered)
    self.editToolbar.horizontalLineTriggered.connect(self.onHorizontalLineTriggered)
    self.editToolbar.bulletListTriggered.connect(self.onBulletListTriggered)
    self.editToolbar.numberListTriggered.connect(self.onNumberListTriggered)
    self.editToolbar.tableTriggered.connect(self.onTableTriggered)

  def onToDefaultFontTriggered(self):
    selectionCursor = self.textCursor()

    doc = self.document()

    # Select entire document
    selectionCursor.select(QtGui.QTextCursor.SelectionType.Document)
    selectionFormat = selectionCursor.charFormat()

    tempCharFormat = QtGui.QTextCharFormat()

    tempCharFormat.setFont(doc.defaultFont())
    tempCharFormat.clearForeground()
    tempCharFormat.clearBackground()

    selectionFormat.clearBackground()   # Clear background color, so it uses the note's background color
    selectionFormat.clearForeground()

    selectionCursor.setCharFormat(tempCharFormat)

    # Clear the colors of the block format
    selectionBlockFormat = QtGui.QTextBlockFormat()

    selectionBlockFormat = selectionCursor.blockFormat()
    selectionBlockFormat.clearForeground()
    selectionBlockFormat.clearBackground()

    selectionCursor.clearSelection()      # Deselect the text

    self.setTextCursor(selectionCursor)

  @QtCore.Slot()
  def on_selectionChanged(self):
    self.updateFontControls()
    selCursor = self.textCursor()

    # TODO: I think this code can be deleted; I think it was only relevant when there was a global toolbar.
    # if selCursor.hasSelection():
    #   # If the edit toolbar is visible, move it here
    #   if self.editToolbar is not None:
    #     self.editToolbar.moveEditToolbar(self.parent)

  @QtCore.Slot()
  def on_cursorPositionChanged(self):
    self.updateFontControls()

  def onToolbarClosing(self):
    """Handles the closing of the edit toolbar.
    """
    self.editToolbar = None

  def onFontSizeChanged(self, fontSize: int):
    selectionCursor, selectionFormat = self.getCursorAndSelectionFormat()
    tempCharFormat = QtGui.QTextCharFormat()

    tempCharFormat.setFontPointSize(fontSize)
    self.mergeCharFormat(tempCharFormat, selectionCursor)

  def onFontFamilyChanged(self, fontFamily: str):
    selectionCursor, selectionFormat = self.getCursorAndSelectionFormat()
    tempCharFormat = QtGui.QTextCharFormat()

    tempCharFormat.setFontFamily(fontFamily)
    self.mergeCharFormat(tempCharFormat, selectionCursor)

  def onLeftAlignTriggered(self):
    selectionCursor, selectionFormat = self.getCursorAndBlockFormat()
    selectionFormat.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
    self.setBlockFormat(selectionCursor, selectionFormat)
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

  def onCenterAlignTriggered(self):
    selectionCursor, selectionFormat = self.getCursorAndBlockFormat()
    selectionFormat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    self.setBlockFormat(selectionCursor, selectionFormat)
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

  def onRightAlignTriggered(self):
    selectionCursor, selectionFormat = self.getCursorAndBlockFormat()
    selectionFormat.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    self.setBlockFormat(selectionCursor, selectionFormat)
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

  def onBoldTriggered(self):
    selectionCursor, selectionFormat = self.getCursorAndSelectionFormat()
    tempCharFormat = QtGui.QTextCharFormat()

    if selectionFormat.fontWeight() != QtGui.QFont.Weight.Bold:
      tempCharFormat.setFontWeight(QtGui.QFont.Weight.Bold)
    else:
      tempCharFormat.setFontWeight(QtGui.QFont.Weight.Normal)

    self.mergeCharFormat(tempCharFormat, selectionCursor)
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

  def onItalicTriggered(self):
    selectionCursor, selectionFormat = self.getCursorAndSelectionFormat()
    tempCharFormat = QtGui.QTextCharFormat()

    tempCharFormat.setFontItalic(not selectionFormat.fontItalic())
    self.mergeCharFormat(tempCharFormat, selectionCursor)
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

  def onUnderlineTriggered(self):
    selectionCursor, selectionFormat = self.getCursorAndSelectionFormat()
    tempCharFormat = QtGui.QTextCharFormat()

    tempCharFormat.setFontUnderline(not selectionFormat.fontUnderline())
    self.mergeCharFormat(tempCharFormat, selectionCursor)
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

  def onHorizontalLineTriggered(self):
    self.insertHtml('<hr />')
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

  def onBulletListTriggered(self):
    self.createList(QtGui.QTextListFormat.Style.ListDisc)
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)
    self.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)
    QtCore.QTimer.singleShot(100, self.setFocusToParent)

  def setFocusToParent(self):
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

  def onNumberListTriggered(self):
    self.createList(QtGui.QTextListFormat.Style.ListDecimal)
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

  def createList(self, style: QtGui.QTextListFormat.Style):
    selectionCursor, newListFormat = self.getCursorAndListFormat()
    newListFormat.setIndent(1)
    newListFormat.setStyle(style)
    selectionCursor.createList(newListFormat)

  def onTableTriggered(self, numRows: int, numColumns: int):
    selectionCursor = self.textCursor()
    selectionCursor.insertTable(numRows, numColumns)
    self.theParent.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)
