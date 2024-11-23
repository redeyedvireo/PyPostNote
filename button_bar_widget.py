from PySide6 import QtCore, QtWidgets, QtGui
from ui_button_bar_widget import Ui_ButtonBarWidget

class ButtonBarWidget(QtWidgets.QWidget):
  def __init__(self, textEditRect: QtCore.QRect, parent: QtWidgets.QWidget = None):
    super(ButtonBarWidget, self).__init__(parent)

    self.ui = Ui_ButtonBarWidget()
    self.ui.setupUi(self)

  def setTopicMenu(self, menu: QtWidgets.QMenu):
    self.ui.topicButton.setMenu(menu)
    