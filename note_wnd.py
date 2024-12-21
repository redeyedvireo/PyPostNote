from PySide6 import QtCore, QtWidgets, QtGui
from button_bar_widget import ButtonBarWidget
from text_edit import TextEdit
from ui_note_wnd import Ui_NoteWnd
from note_data import TOPIC_ID, NoteData, kInvalidNote
from note_style import ENoteBackground, NoteStyle
from topic import kDefaultTopicId
from topic_manager import TopicManager
from note_properties_dlg import NotePropertiesDlg
import datetime
import logging

class NoteWnd(QtWidgets.QWidget):
  saveNote = QtCore.Signal(NoteData)
  deleteNote = QtCore.Signal(int)
  showEditTopicDialog = QtCore.Signal(int)

  def __init__(self, topicManager: TopicManager, parent: QtWidgets.QWidget = None):
    super(NoteWnd, self).__init__(parent, QtCore.Qt.Tool | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)

    # The modificationAllowed flag prevents various changes to the note as being considered user modifications.  It will be
    # set to False while the note is being created, and will be set to True once the note is ready for user input.
    self.modificationAllowed = False

    self.buttonBarWidget = None

    self.ui = Ui_NoteWnd()
    self.ui.setupUi(self)

    self.topicManager = topicManager

    self.noteId = kInvalidNote
    self.noteCreationTime = datetime.datetime.now()
    self.lastUpdateTime = datetime.datetime.now()
    self._topicId = kDefaultTopicId
    self.noteUsesOwnColorScheme = False
    self.alwaysOnTop = False
    self.dirtyFlag = False          # Indicates if the user has made any changes to the note

    self.noteStyle = NoteStyle()

    self.propertiesDlg = None

    self.setMinimumSize(QtCore.QSize(40, 20))
    self.updateNote()

    QtCore.QTimer.singleShot(100, self.createButtonBarWidget)

  @property
  def noteData(self) -> NoteData:
    outNoteData = NoteData()

    outNoteData.noteId = self.noteId
    outNoteData.geometryData = self.saveGeometry()
    outNoteData.title = self.windowTitle()
    outNoteData.contentsData = self.ui.textEdit.toHtml()
    outNoteData.addedTime = self.noteCreationTime
    outNoteData.lastModifiedTime = self.lastUpdateTime
    outNoteData.topicId = self._topicId
    outNoteData.usesOwnColors = self.noteUsesOwnColorScheme
    outNoteData.alwaysOnTop = self.alwaysOnTop
    outNoteData.textColor = self.noteStyle.textColor
    outNoteData.bgColor = self.noteStyle.backgroundColor
    outNoteData.bgType = self.noteStyle.backgroundType
    outNoteData.transparency = self.noteStyle.transparency

    return outNoteData

  @noteData.setter
  def noteData(self, data: NoteData):
    self.setWindowTitle(data.title)
    self.setNoteGeometry(data.geometryData)
    self.ui.textEdit.setHtml(data.contentsData)
    self.noteId = data.noteId
    self.noteCreationTime = data.addedTime
    self.lastUpdateTime = data.lastModifiedTime
    self._topicId = data.topicId    # Don't use the setter here, to avoid the update triggered by doing so
    self.noteUsesOwnColorScheme = data.usesOwnColors
    self.alwaysOnTop = data.alwaysOnTop

    self.noteStyle.textColor = data.textColor
    self.noteStyle.backgroundColor = data.bgColor
    self.noteStyle.backgroundType = data.bgType
    self.noteStyle.transparency = data.transparency

    self.updateNote()

  @property
  def dirty(self) -> bool:
    return self.dirtyFlag

  @dirty.setter
  def dirty(self, inDirty: bool):
    self.dirtyFlag = inDirty

    if inDirty:
      # If setting the note to dirty, set the modification time
      self.lastUpdateTime = datetime.datetime.now()
    else:
      # If clearing the dirty flag, make sure the text edit's modified flag is cleared also
      self.ui.textEdit.document().setModified(False)

  @property
  def topicId(self):
    return self._topicId

  @topicId.setter
  def topicId(self, value: TOPIC_ID):
    self._topicId = value
    self.noteUsesOwnColorScheme = False

    self.updateNote()
    self.dirty = True

  @property
  def noteTitle(self):
    return self.windowTitle()

  @noteTitle.setter
  def noteTitle(self, title: str):
    self.setWindowTitle(title)

  def showNote(self):
    self.show()

    # Activate the note
    self.activateWindow()
    self.raise_()

    # When a note is shown, and thus ready for user input, it is open to allowing changes to be considered
    # as user modifications.
    self.modificationAllowed = True

  def hideNote(self):
    # When a note is hidden, any modifications made are not to be considered as user modifications.
    self.modificationAllowed = False
    self.hide()

  def updateNote(self):
    """ Updates the note's appearance. """
    # Most notes will take their appearance settings from the topic to which they belong
    topic = self.topicManager.getTopic(self.topicId)

    bgColor = QtGui.QColor("yellow")
    textColor = QtGui.QColor("black")
    transparency = 100

    if topic is not None:
      textColor = topic.topicStyle.textColor
      bgColor = topic.topicStyle.backgroundColor
      transparency = topic.topicStyle.transparency
    else:
      # Should not happen
      logging.error(f'[NoteWnd.updateNote] Note topicID is not found in TopicManager: {self.topicId}')

    if self.noteUsesOwnColorScheme or topic is None:
      textColor = self.noteStyle.textColor
      bgColor = self.noteStyle.backgroundColor
      transparency = self.noteStyle.transparency

    textCursor = self.ui.textEdit.textCursor()
    curpos = textCursor.position()

    self.ui.textEdit.selectAll()
    self.ui.textEdit.setTextColor(textColor)
    textCursor.setPosition(curpos)
    self.ui.textEdit.setTextCursor(textCursor)

    self.ui.textEdit.setStyleSheet(f'QTextEdit {{ color: {textColor.name()}; background-color: {bgColor.name()} }}')
    self.setNoteTransparency(transparency)
    self.setAlwaysOnTopness(self.alwaysOnTop)

  def setNoteGeometry(self, geometry: QtCore.QByteArray):
    # TODO: I think this is what causes the issue where all windows appear in the center of the screen.  There needs to be
    #       some way of checking if the note's window exists, and if the note's rectangle is within this window.  It might
    #       be good to store the note's geometry in a different way in the database.  To do so, add new fields to the database,
    #       (x, y, width, height), but keep the existing geometry field to preserve backward compatibility.  Then, continue to
    #       store note geometry in the legacy field, but also store it in new fields.  When reading, see if the new field has
    #       been initialized, and if so, use that; otherwise use the old geometry field.
    self.restoreGeometry(geometry)

  def setNoteTransparency(self, value: int):
    self.setWindowOpacity(float(value) / 100)

  def setAlwaysOnTopness(self, alwaysOnTop: bool):
    self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, alwaysOnTop)

  def createButtonBarWidget(self):
    self.buttonBarWidget = ButtonBarWidget(self.ui.textEdit.rect(), self)
    self.topicMenu = QtWidgets.QMenu('Topic', self)
    self.topicMenu.aboutToShow.connect(self.populateTopicMenu)
    self.buttonBarWidget.setTopicMenu(self.topicMenu)

    # Connect signals
    self.buttonBarWidget.notePropertiesDlgSignal.connect(self.onPropertiesDlg)
    self.buttonBarWidget.noteDeleteSignal.connect(self.onDeleteNote)

  # TODO: Instead of doing it this way, try to install an event filter on the window.  To do so,
  #       Google: "pyside6 detect click on title bar"
  # def nativeEvent(self, eventType: QtCore.QByteArray, message):
  #   return_value, result = super().nativeEvent(eventType, message)

  #   if eventType == b'windows_generic_MSG':
  #     msg = MSG.from_address(message.__int__())
  #     print(f'nativeEvent: {eventType}  --  {msg}')

  #     WM_LBUTTONDOWN = 0x0201
  #     HTCAPTION = 2

  #     if message == WM_LBUTTONDOWN:
  #       if message.wParam == HTCAPTION:
  #         yPos = (message.lParam >> 16) & 0x0000ffff
  #         xPos = message.lParam & 0x0000ffff

  #         hitPt = QtCore.QPoint(xPos, yPos)
  #         # self.onContextMenu(hitPt)
  #         print(f'hitPt: {hitPt}')
  #         return True

  #   return False

  def moveEvent(self, event: QtGui.QMoveEvent):
    # Moving the note consitutes making it dirty.  However, the note won't be
    # saved immediately; it will be saved at the next autosave timer event,
    # or if the note loses focus.
    self.dirty = True

    return super(NoteWnd, self).moveEvent(event)

  def resizeEvent(self, event):
    # Resizing the note consitutes making it dirty.  However, the note won't be
    # saved immediately; it will be saved at the next autosave timer event,
    # or if the note loses focus.
    self.dirty = True

    result = super().resizeEvent(event)

    # TODO: Resizing the button bar breaks it.  Breakage is similar to when
    #       the rect was not being copied.
    if self.buttonBarWidget is not None:
      self.buttonBarWidget.resizeButtonBar(self.ui.textEdit.rect())

    return result

  @QtCore.Slot()
  def populateTopicMenu(self):
    self.topicMenu.clear()

    topicIdList = self.topicManager.getTopicIds(True)

    for topicId in topicIdList:
      topic = self.topicManager.getTopic(topicId)

      if topic is not None:
        newAction = self.topicMenu.addAction(topic.topicName)
        newAction.setCheckable(True)

        if self.topicId == topicId:
          # Check the current topic
          newAction.setChecked(True)

        newAction.setData(topicId)
        newAction.triggered.connect(self.onSetNewTopic)
      else:
        logging.error(f'[NoteWnd.populateTopicMenu] topic ID {topicId} not found in TopicManager')

  def onSetNewTopic(self):
    sender = self.sender()
    if type(sender) is QtGui.QAction:
      self._topicId = sender.data()
      self.updateNote()
      self.saveNote.emit(self.noteData)
      self.dirty = False

  def onPropertiesDlg(self):
    self.propertiesDlg = NotePropertiesDlg(self.topicManager, self.noteData, self)
    self.propertiesDlg.showEditTopicsDialogSignal.connect(self.onEditNoteTopicsTriggered)

    result = self.propertiesDlg.exec_()

    if result == QtWidgets.QDialog.DialogCode.Accepted:
      # Set note with the data from the dialog
      self.noteData = self.propertiesDlg.noteData
      self.saveNote.emit(self.noteData)

    self.propertiesDlg = None

  def onEditNoteTopicsTriggered(self):
    self.showEditTopicDialog.emit(self.noteId)

  def updateTopics(self):
    if self.propertiesDlg is not None:
      self.propertiesDlg.populateTopicCombo()

  def onDeleteNote(self):
    self.deleteNote.emit(self.noteId)

  @QtCore.Slot()
  def on_textEdit_textChanged(self):
    # Use this signal to update the "last update" date/time, but note that this is tricky,
    # because this signal is called multiple times when on startup when notes are read from
    # the database and displayed.  The modificationAllowed flag is an attempt to filter out
    # system modifications so that the lastUpdateTime is only for user modifications.
    if self.modificationAllowed:
      if self.ui.textEdit.document().isModified():
        self.dirty = True

  @QtCore.Slot()
  def on_textEdit_TE_LostFocus(self):
    if self.dirty:
      # If the note is dirty and loses focus, save it
      self.saveNote.emit(self.noteData)
      self.dirty = False
