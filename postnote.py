from PySide6 import QtCore, QtWidgets, QtGui
from about_dlg import AboutDlg
from database import Database
from note_data import TOPIC_ID, NoteData, ENoteSizeEnum
from note_exporter import NoteExporter
from note_importer import NoteImporter
from note_manager import NoteManager
from note_wnd import NoteWnd
from preferences import Preferences, EDoubleClickAction
from preferences_dlg import PreferencesDlg
from quick_create_dlg import QuickCreateDlg
from select_style_dlg import SelectStyleDialog
from style_manager import StyleManager
from topic import Topic
from topic_manager import TopicManager
from ui_postnote import Ui_PostNoteClass
from edit_topics_dialog import EditTopicsDialog
from util import getDatabasePath, getPrefsPath, getStorageDirectory, getStyleDefsPath
import logging


kAppName = 'PyPostNote'
kDatabaseName = 'Notes.db'
kDatabaseNameDebug = 'NotesDebug.db'
kPrefsName = 'PyPostNote.ini'
kStyleDefsName = 'Styles.xml'

class PostNoteWindow(QtWidgets.QMainWindow):
  def __init__(self, db: Database, noteManager: NoteManager, topicManager: TopicManager, styleManager: StyleManager, preferences: Preferences, debug: bool):
    super(PostNoteWindow, self).__init__()

    self.ui = Ui_PostNoteClass()
    self.ui.setupUi(self)

    self.debug = debug

    self.noteManager = noteManager
    self.topicManager = topicManager
    self.styleManager = styleManager
    self.db = db
    self.preferences = preferences

    self.noteManager.saveNote.connect(self.onSaveNote)

    self.topicManager.topicAdded.connect(self.onNewTopicAdded)
    self.topicManager.topicUpdated.connect(self.onTopicUpdated)
    self.topicManager.topicDeleted.connect(self.onTopicDeleted)

    self.autoSaveTimer = QtCore.QTimer()
    self.autoSaveTimer.timeout.connect(self.onAutoSaveTimerTimeout)

    self.setIcon()
    self.createNoteMenu()

  def initialize(self):
    preferencesPath = getPrefsPath(kAppName, kPrefsName)

    self.preferences.readPrefsFile(preferencesPath)

    # Load the style definitions
    styleDefsPath = getStyleDefsPath(kAppName, kStyleDefsName)
    self.styleManager.loadStyleDefs(styleDefsPath)

    databaseName = kDatabaseName if not self.debug else kDatabaseNameDebug

    databasePath = getDatabasePath(kAppName, databaseName)
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
          noteWnd = self.noteManager.createPopulatedNote(note)
          if noteWnd is not None:
            # Connect to any signals the note might have, such as a signal to launch the topics editor.
            self.connectNoteSignals(noteWnd)

        # Start the auto-save timer
        self.autoSaveTimer.start(1000 * 60 * self.preferences.autoSaveMinutes)
      else:
        logging.error('Error loading notes')
        # TODO: Pop up an error dialog

  def connectNoteSignals(self, noteWnd: NoteWnd):
    noteWnd.saveNote.connect(self.onSaveNote)
    noteWnd.deleteNote.connect(self.onDeleteNote)
    noteWnd.showEditTopicDialog.connect(self.onEditTopicsTriggeredFromNote)

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
    self.trayIconMenu.addSeparator()

    self.trayIconMenu.addAction(self.ui.actionHide_All_Notes)
    self.trayIconMenu.addAction(self.ui.actionShow_All_Notes)

    # Create note list menu
    self.noteListMenu = QtWidgets.QMenu('Show Note', self)
    self.trayIconMenu.addMenu(self.noteListMenu)

    self.trayIconMenu.addSeparator()
    self.trayIconMenu.addAction(self.ui.actionEdit_Topics)
    self.trayIconMenu.addAction(self.ui.actionEdit_Styles)
    self.trayIconMenu.addAction(self.ui.actionPreferences)

    self.trayIconMenu.addSeparator()
    self.trayIconMenu.addAction(self.ui.actionSave_All_Notes)
    self.trayIconMenu.addAction(self.ui.actionImport_Notes)
    self.trayIconMenu.addAction(self.ui.actionExport_Notes)

    self.trayIconMenu.addSeparator()
    self.trayIconMenu.addAction(self.ui.actionAbout_PostNote)
    self.trayIconMenu.addAction(self.ui.actionAbout_Qt)

    if self.debug:
      self.trayIconMenu.addAction(self.ui.actionDebug_Mode)

    self.trayIconMenu.addSeparator()
    self.trayIconMenu.addAction(self.ui.actionExit_PostNote)

    self.trayIcon.setContextMenu(self.trayIconMenu)
    self.trayIcon.show()

  def createNewNote(self, sizeEnum: ENoteSizeEnum):
    noteWnd = self.noteManager.createBlankNote(sizeEnum)

    if noteWnd is not None:
      success = self.db.addNote(noteWnd.noteData)

      if success:
        # Connect to any signals the note might have, such as a signal to launch the topics editor.
        self.connectNoteSignals(noteWnd)
        return noteWnd
      else:
        logging.error(f'[PostNoteWindow.createNewNote] Error creating a note of size {sizeEnum}')
        return None


  # ************ SLOTS ************

  @QtCore.Slot(int)
  def onDeleteNote(self, noteId: int):
    self.noteManager.deleteNote(noteId)
    self.db.deleteNote(noteId)

  @QtCore.Slot(Topic)
  def onNewTopicAdded(self, topic: Topic):
    self.db.addTopic(topic)

  @QtCore.Slot(Topic)
  def onTopicUpdated(self, topic: Topic):
    self.db.updateTopic(topic)
    self.noteManager.onTopicChanged(topic)

  @QtCore.Slot(int)
  def onTopicDeleted(self, topicId: TOPIC_ID):
    self.db.deleteTopic(topicId)
    self.noteManager.onTopicDeleted(topicId)

  def onActivated(self, reason: QtWidgets.QSystemTrayIcon.ActivationReason):
    if reason == QtWidgets.QSystemTrayIcon.ActivationReason.Context:
      # The tray icon was right-clicked
      self.noteListMenu.clear()

      ids = self.noteManager.allNoteIds()

      for id in ids:
        note = self.noteManager.getNote(id)

        if note is not None:
          title = note.noteTitle
          action = self.noteListMenu.addAction(title, self.onShowNote)
          action.setData(id)

    elif reason == QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick:
      # The tray icon was double-clicked
      match self.preferences.doubleClickAction:
        case EDoubleClickAction.eDCACreateSmallNote:
          self.createNewNote(ENoteSizeEnum.eSmallNote)

        case EDoubleClickAction.eDCACreateMediumNote:
          self.createNewNote(ENoteSizeEnum.eMediumNote)

        case EDoubleClickAction.eDCACreateLargeNote:
          self.createNewNote(ENoteSizeEnum.eLargeNote)

        case EDoubleClickAction.eDCACreateExtraLargeNote:
          self.createNewNote(ENoteSizeEnum.eExLargeNote)

        case EDoubleClickAction.eDCAQuickCreateDialog:
          self.showQuickCreateDialog()

        case EDoubleClickAction.eDCAShowAllNotes:
          self.noteManager.showAllNotes()

  def showQuickCreateDialog(self):
    dlg = QuickCreateDlg(self.topicManager, self)

    def updateTopics():
      self.on_actionEdit_Topics_triggered()
      dlg.populateTopicCombo()

    dlg.showEditTopicsDialogSignal.connect(updateTopics)

    result = dlg.exec_()
    if result == QtWidgets.QDialog.DialogCode.Accepted:
      noteTitle = dlg.getNoteTitle()
      noteSize = dlg.getNoteSize()
      noteTopicId = dlg.getTopicId()

      noteWnd = self.createNewNote(noteSize)

      if noteWnd is not None:
        noteWnd.noteTitle = noteTitle
        noteWnd.topicId = noteTopicId

  @QtCore.Slot()
  def onShowNote(self):
    sender = self.sender()

    if type(sender) is QtGui.QAction:
      noteId = sender.data()
      self.noteManager.showNote(noteId)

  @QtCore.Slot(NoteData)
  def onSaveNote(self, noteData: NoteData):
    success = self.db.updateNote(noteData)
    if not success:
      logging.error(f'Error saving note {noteData.title} (ID: {noteData.noteId})')
      # TODO: Show error dialog?

  def onEditTopicsTriggeredFromNote(self, noteId: int):
    """Triggers the edit topics dialog from a note.  After the dialog is closed,
       the note will be updated with the new topic.

    Args:
        noteId (int): Note ID
    """
    self.on_actionEdit_Topics_triggered()

    self.noteManager.updateTopicsForANote(noteId)

  @QtCore.Slot()
  def on_actionSmall_triggered(self):
    self.createNewNote(ENoteSizeEnum.eSmallNote)

  @QtCore.Slot()
  def on_actionMedium_triggered(self):
    self.createNewNote(ENoteSizeEnum.eMediumNote)

  @QtCore.Slot()
  def on_actionLarge_triggered(self):
    self.createNewNote(ENoteSizeEnum.eLargeNote)

  @QtCore.Slot()
  def on_actionExtra_Large_triggered(self):
    self.createNewNote(ENoteSizeEnum.eExLargeNote)

  @QtCore.Slot()
  def on_actionImport_Notes_triggered(self):
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Import Notes", "",
                                                        "JSON Files (*.json);;All Files (*)")

    if fileName is not None:
      noteImporter = NoteImporter()
      result = noteImporter.importNotes(fileName)

      errorsOccurred = False

      if type(result) is tuple:
        notes, topics = result

        for topicData in topics:
          self.topicManager.addTopicFromTopicData(topicData)

        for noteData in notes:
          # Create the note window.  If the note's ID already exists, a new ID will be generated.
          noteWnd = self.noteManager.createPopulatedNote(noteData, True)

          if noteWnd is not None:
            noteData.noteId = noteWnd.noteId    # createPopulatedNote() may have generated a new ID
            success = self.db.addNote(noteData)

            if success:
              self.connectNoteSignals(noteWnd)
            else:
              logging.error(f'[PostNoteWindow.on_actionImport_Notes_triggered] Error saving note {noteData.title}')
              errorsOccurred = True
          else:
            logging.error(f'[PostNoteWindow.on_actionImport_Notes_triggered] Error creating note {noteData.title}')
            errorsOccurred = True

      if errorsOccurred:
        QtWidgets.QMessageBox.warning(self,
                                      "Import Notes",
                                      "Some notes could not be created.")

  @QtCore.Slot()
  def on_actionExport_Notes_triggered(self):
    fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Export Notes", "",
                                                        "JSON Files (*.json);;All Files (*)")

    if fileName is not None:
      noteExporter = NoteExporter()
      self.noteManager.addNotesToExporter(noteExporter)
      self.topicManager.addTopicsToExporter(noteExporter)
      noteExporter.export(fileName)

  @QtCore.Slot()
  def on_actionEdit_Topics_triggered(self):
    dlg = EditTopicsDialog(self, self.topicManager, self.noteManager)
    dlg.exec()

  @QtCore.Slot()
  def on_actionEdit_Styles_triggered(self):
    dlg = SelectStyleDialog(self, self.styleManager, self.preferences.defaultFontFamily, self.preferences.defaultFontSize)
    dlg.exec()

    # Save style defs
    styleDefsPath = getStyleDefsPath(kAppName, kStyleDefsName)
    self.styleManager.saveStyleDefs(styleDefsPath)

  @QtCore.Slot()
  def on_actionPreferences_triggered(self):
    dlg = PreferencesDlg(self.noteManager, self.preferences, self)

    dlg.exec()

    self.updateAutoShutdown()

    # Restart the auto-save timer
    self.autoSaveTimer.start(1000 * 60 * self.preferences.autoSaveMinutes)

  @QtCore.Slot()
  def on_actionSave_All_Notes_triggered(self):
    self.noteManager.saveAllNotes()

  @QtCore.Slot()
  def on_actionHide_All_Notes_triggered(self):
    self.noteManager.hideAllNotes()

  @QtCore.Slot()
  def on_actionShow_All_Notes_triggered(self):
    self.noteManager.showAllNotes()

  @QtCore.Slot()
  def on_actionAbout_Qt_triggered(self):
    QtWidgets.QMessageBox.aboutQt(self)

  @QtCore.Slot()
  def on_actionAbout_PostNote_triggered(self):
    dlg = AboutDlg(getStorageDirectory(kAppName), self)
    dlg.exec_()

  @QtCore.Slot()
  def on_actionExit_PostNote_triggered(self):
    QtCore.QCoreApplication.quit()

  @QtCore.Slot()
  def on_actionDebug_Mode_triggered(self):
    QtWidgets.QMessageBox.information(self, 'Debug Mode',
                                    f"The application is running in debug mode.  The database is {kDatabaseNameDebug}.")

  def onAutoSaveTimerTimeout(self):
    """Idle timeout handler.  Used auto-save dirty notes.
    """
    self.noteManager.saveDirtyNotes()
