from PySide6 import QtCore, QtWidgets, QtGui

class TextEdit(QtWidgets.QTextEdit):
  def __init__(self, parent):
    super(TextEdit, self).__init__(parent)
    self.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
  