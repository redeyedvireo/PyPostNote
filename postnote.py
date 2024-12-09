from PySide6 import QtCore, QtWidgets, QtGui
from database import Database
from note_data import TOPIC_ID
from note_manager import NoteManager
from preferences import Preferences
from preferences_dlg import PreferencesDlg
from topic import Topic
from topic_manager import TopicManager
from ui_postnote import Ui_PostNoteClass
from edit_topics_dialog import EditTopicsDialog
import logging

from util import getDatabasePath, getPrefsPath

kAppName = 'PyPostNote'
kDatabaseName = 'Notes.db'
kPrefsName = 'PyPostNote.ini'

class PostNoteWindow(QtWidgets.QMainWindow):

  def __init__(self, db: Database, noteManager: NoteManager, topicManager: TopicManager, preferences: Preferences):
    super(PostNoteWindow, self).__init__()

    self.ui = Ui_PostNoteClass()
    self.ui.setupUi(self)

    self.noteManager = noteManager
    self.topicManager = topicManager
    self.db = db
    self.preferences = preferences

    self.topicManager.topicAdded.connect(self.onNewTopicAdded)
    self.topicManager.topicUpdated.connect(self.onTopicUpdated)
    self.topicManager.topicDeleted.connect(self.onTopicDeleted)

    self.setIcon()
    self.createNoteMenu()

  def initialize(self):
    # TODO: See stuff from C++ version

    preferencesPath = getPrefsPath(kAppName, kPrefsName)

    self.preferences.readPrefsFile(preferencesPath)

    databasePath = getDatabasePath(kAppName, kDatabaseName)
    if self.db.openDatabase(databasePath):
      loadingTopicsSuccessful, topics = self.db.getTopics()

      if loadingTopicsSuccessful:
        # Create topics
        for topicData in topics:
          self.topicManager.addTopicFromTopicData(topicData)
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

  def updateAutoShutdown(self):
    # TODO: Implement
    pass

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

    self.trayIcon.activated.connect(self.onActivated)

  def createNoteMenu(self):
    self.trayIconMenu = QtWidgets.QMenu(self)

    # Create Note Size menu (for creating new notes)
    self.noteSizeMenu = QtWidgets.QMenu('New Note', self)
    self.noteSizeMenu.addAction(self.ui.actionSmall)
    self.noteSizeMenu.addAction(self.ui.actionMedium)
    self.noteSizeMenu.addAction(self.ui.actionLarge)
    self.noteSizeMenu.addAction(self.ui.actionExtra_Large)

    self.trayIconMenu.addMenu(self.noteSizeMenu)

    self.trayIconMenu.addAction(self.ui.actionSave_All_Notes)
    self.trayIconMenu.addAction(self.ui.actionHide_All_Notes)
    self.trayIconMenu.addAction(self.ui.actionShow_All_Notes)

    # Create note list menu
    self.noteListMenu = QtWidgets.QMenu('Show Note', self)
    self.trayIconMenu.addMenu(self.noteListMenu)

    self.trayIconMenu.addAction(self.ui.actionExport_Notes)
    self.trayIconMenu.addAction(self.ui.actionEdit_Topics)
    self.trayIconMenu.addAction(self.ui.actionPreferences)


    self.trayIconMenu.addSeparator()
    self.trayIconMenu.addAction(self.ui.actionAbout_Qt)
    self.trayIconMenu.addAction(self.ui.actionAbout_PostNote)

    self.trayIconMenu.addSeparator()
    self.trayIconMenu.addAction(self.ui.actionExit_PostNote)

    self.trayIcon.setContextMenu(self.trayIconMenu)
    self.trayIcon.show()

  # ************ SLOTS ************

  @QtCore.Slot(Topic)
  def onNewTopicAdded(self, topic: Topic):
    # TODO: Implement
    print(f'onNewTopicAdded: {topic.topicName}')

  @QtCore.Slot(Topic)
  def onTopicUpdated(self, topic: Topic):
    # TODO: Implement
    print(f'onTopicUpdated: {topic.topicName}')

  @QtCore.Slot(int)
  def onTopicDeleted(self, topicId: TOPIC_ID):
    # TODO: Implement
    print(f'onTopicDeleted: {topicId}')


  def onActivated(self, reason: QtWidgets.QSystemTrayIcon.ActivationReason):
    if reason == QtWidgets.QSystemTrayIcon.ActivationReason.Context:
      # The tray icon was right-clicked
      self.noteListMenu.clear()

      ids = self.noteManager.allNoteIds()

      for id in ids:
        note = self.noteManager.getNote(id)

        if note is not None:
          title = note.noteTitle()
          action = self.noteListMenu.addAction(title, self.onShowNote)
          action.setData(id)

    elif reason == QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick:
      # The tray icon was dobule-clicked - create a new note
      # TODO: Implement
      print('Implement tray double-click event')

  @QtCore.Slot()
  def onShowNote(self):
    sender = self.sender()

    if type(sender) is QtGui.QAction:
      noteId = sender.data()
      self.noteManager.showNote(noteId)

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
    dlg = EditTopicsDialog(self, self.topicManager, self.noteManager)
    dlg.exec_()

  @QtCore.Slot()
  def on_actionPreferences_triggered(self):
    dlg = PreferencesDlg(self.noteManager, self.preferences, self)

    dlg.exec_()

    self.updateAutoShutdown()

    # TODO: update other things, like the auto-save timer, and whatever else needs to be updated

  @QtCore.Slot()
  def on_actionSave_All_Notes_triggered(self):
    # TODO: Implement
    print('Save all notes')

  @QtCore.Slot()
  def on_actionHide_All_Notes_triggered(self):
    self.noteManager.hideAllNotes()

  @QtCore.Slot()
  def on_actionShow_All_Notes_triggered(self):
    self.noteManager.showAllNotes()

  @QtCore.Slot()
  def on_actionAbout_Qt_triggered(self):
    QtWidgets.QMessageBox.aboutQt(None)

  @QtCore.Slot()
  def on_actionAbout_PostNote_triggered(self):
    # TODO: Implement
    print('About PostNote')

  @QtCore.Slot()
  def on_actionExit_PostNote_triggered(self):
    QtCore.QCoreApplication.quit()
