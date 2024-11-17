from PySide6 import QtCore, QtWidgets, QtGui
from ui_postnote import Ui_PostNoteClass
import logging

class PostNoteWindow(QtWidgets.QMainWindow):

  def __init__(self):
    super(PostNoteWindow, self).__init__()

    self.ui = Ui_PostNoteClass()
    self.ui.setupUi(self)

    self.setIcon()
    self.createNoteMenu()

  def initialize(self):
    logging.info('PostNoteWindow.initialize called.')
    # TODO: See stuff from C++ version

  def setIcon(self):
    systemTrayAvailable = QtWidgets.QSystemTrayIcon.isSystemTrayAvailable()

    if not systemTrayAvailable:
      logging.error('Whoops!  It looks like the system tray is not available.')
      return

    icon = QtGui.QIcon(':/PostNote/Resources/PostNote.ico')
    self.trayIcon = QtWidgets.QSystemTrayIcon()
    self.trayIcon.setIcon(icon)
    self.setWindowIcon(icon)
    self.trayIcon.setToolTip('PyPostNote')

  def createNoteMenu(self):
    self.trayIconMenu = QtWidgets.QMenu(self)
    self.trayIconMenu.addAction(self.ui.actionSave_All_Notes)
    self.trayIconMenu.addAction(self.ui.actionExit_PostNote)

    self.trayIcon.setContextMenu(self.trayIconMenu)
    self.trayIcon.show()

  # ************ SLOTS ************

  @QtCore.Slot()
  def on_actionSave_All_Notes(self):
    # TODO: Implement
    pass

  @QtCore.Slot()
  def on_actionExit_PostNote_triggered(self):
    print('on_actionExit_PostNote_triggered')
    QtCore.QCoreApplication.quit()