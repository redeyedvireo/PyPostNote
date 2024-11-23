from PySide6 import QtCore, QtWidgets, QtGui
from database import Database
from note_manager import NoteManager
from ui_postnote import Ui_PostNoteClass
import logging

from util import getDatabasePath

kAppName = 'PyPostNote'
kDatabaseName = 'Notes.db'

class PostNoteWindow(QtWidgets.QMainWindow):

  def __init__(self):
    super(PostNoteWindow, self).__init__()

    self.ui = Ui_PostNoteClass()
    self.ui.setupUi(self)

    self.setIcon()
    self.createNoteMenu()

  # TODO: Pass the topic manager here also
  def initialize(self, db: Database, noteManager: NoteManager):
    # TODO: See stuff from C++ version
    self.noteManager = noteManager
    self.db = db

    databasePath = getDatabasePath(kAppName, kDatabaseName)
    if self.db.openDatabase(databasePath):
      loadingTopicsSuccessful, topics = self.db.getTopics()

      if loadingTopicsSuccessful:
        # Create topics
        for topicData in topics:
          # TODO: Create the topic (use the topic manager to do this)
          pass
      else:
        logging.error('Error loading topics')
        # TODO: Pop up an error dialog

      loadingNotesSuccessful, notes = self.db.getNotes()

      if loadingNotesSuccessful:
        # Create the note windows
        for note in notes:
          self.noteManager.createPopulatedNote(note)
      else:
        logging.error('Error loading notes')
        # TODO: Pop up an error dialog

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

    # Create Note Size menu (for creating new notes)
    self.noteSizeMenu = QtWidgets.QMenu('New Note', self)
    self.noteSizeMenu.addAction(self.ui.actionSmall)
    self.noteSizeMenu.addAction(self.ui.actionMedium)
    self.noteSizeMenu.addAction(self.ui.actionLarge)
    self.noteSizeMenu.addAction(self.ui.actionExtra_Large)

    self.trayIconMenu.addMenu(self.noteSizeMenu)

    # Create note list menu
    self.noteListMenu = QtWidgets.QMenu('Show Note', self)
    self.trayIconMenu.addMenu(self.noteListMenu)

    self.trayIconMenu.addAction(self.ui.actionExport_Notes)
    self.trayIconMenu.addAction(self.ui.actionEdit_Topics)
    self.trayIconMenu.addAction(self.ui.actionPreferences)

    self.trayIconMenu.addAction(self.ui.actionSave_All_Notes)
    self.trayIconMenu.addAction(self.ui.actionHide_All_Notes)
    self.trayIconMenu.addAction(self.ui.actionShow_All_Notes)

    self.trayIconMenu.addSeparator()
    self.trayIconMenu.addAction(self.ui.actionAbout_Qt)
    self.trayIconMenu.addAction(self.ui.actionAbout_PostNote)

    self.trayIconMenu.addSeparator()
    self.trayIconMenu.addAction(self.ui.actionExit_PostNote)

    self.trayIcon.setContextMenu(self.trayIconMenu)
    self.trayIcon.show()

  # ************ SLOTS ************

  @QtCore.Slot()
  def on_actionSmall_triggered(self):
    # TODO: Implement
    print('Create small note')

  @QtCore.Slot()
  def on_actionMedium_triggered(self):
    # TODO: Implement
    print('Create medium note')

  @QtCore.Slot()
  def on_actionLarge_triggered(self):
    # TODO: Implement
    print('Create large note')

  @QtCore.Slot()
  def on_actionExtra_Large_triggered(self):
    # TODO: Implement
    print('Create extra large note')

  @QtCore.Slot()
  def on_actionExport_Notes_triggered(self):
    # TODO: Implement
    print('Export notes')

  @QtCore.Slot()
  def on_actionEdit_Topics_triggered(self):
    # TODO: Implement
    print('Edit topics')

  @QtCore.Slot()
  def on_actionPreferences_triggered(self):
    # TODO: Implement
    print('Preferences')

  @QtCore.Slot()
  def on_actionSave_All_Notes_triggered(self):
    # TODO: Implement
    print('Save all notes')

  @QtCore.Slot()
  def on_actionHide_All_Notes_triggered(self):
    # TODO: Implement
    print('Hide all notes')

  @QtCore.Slot()
  def on_actionShow_All_Notes_triggered(self):
    # TODO: Implement
    print('Show all notes')

  @QtCore.Slot()
  def on_actionAbout_Qt_triggered(self):
    QtWidgets.QMessageBox.aboutQt(None)

  @QtCore.Slot()
  def on_actionAbout_PostNote_triggered(self):
    # TODO: Implement
    print('About PostNote')

  @QtCore.Slot()
  def on_actionExit_PostNote_triggered(self):
    print('on_actionExit_PostNote_triggered')
    QtCore.QCoreApplication.quit()