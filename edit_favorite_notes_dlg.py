from PySide6 import QtCore, QtWidgets, QtGui
from ui_edit_favorite_notes_dlg import Ui_EditFavoriteNotesDialog
from database import Database
from note_manager import NoteManager
import logging

class EditFavoriteNotesDialog(QtWidgets.QDialog):
  def __init__(self, noteManager: NoteManager, db: Database, parent=None):
      super(EditFavoriteNotesDialog, self).__init__(parent)

      self.ui = Ui_EditFavoriteNotesDialog()
      self.ui.setupUi(self)

      self.noteManager = noteManager
      self.db = db

      self.populateFavoriteNotesList()

  def populateFavoriteNotesList(self):
      """Populates the list of favorite notes in the dialog."""
      self.ui.listWidget.clear()
      favoriteNoteIds = self.noteManager.allFavoriteNoteIds()

      for noteId in favoriteNoteIds:
          noteData = self.noteManager.getFavoriteNoteData(noteId)
          if noteData:
              item = QtWidgets.QListWidgetItem(noteData.title)
              item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsEditable)
              item.setData(QtCore.Qt.ItemDataRole.UserRole, noteId)
              self.ui.listWidget.addItem(item)

  @QtCore.Slot()
  def on_editButton_clicked(self):
    """Handles the edit button click event."""
    selectedItems = self.ui.listWidget.selectedItems()
    if selectedItems:
      item = selectedItems[0]
      self.ui.listWidget.editItem(item)

      # noteId = item.data(QtCore.Qt.ItemDataRole.UserRole)
      # noteData = self.noteManager.getFavoriteNoteData(noteId)

      # if noteData:
        # Open a dialog to edit the favorite note
        # This could be a separate dialog or inline editing
        # newTitle, ok = QtWidgets.QInputDialog.getText(self, "Edit Favorite Note", "Enter new title:", text=noteData.title)
        # if ok and newTitle:
        #   noteData.title = newTitle
        #   # self.db.updateFavoriteNoteTitle(noteId, newTitle)  # Update in the database
        #   item.setText(newTitle)  # Update the list item text


  @QtCore.Slot()
  def on_deleteButton_clicked(self):
    selectedItems = self.ui.listWidget.selectedItems()
    if selectedItems:
      item = selectedItems[0]
      noteId = item.data(QtCore.Qt.ItemDataRole.UserRole)

      reply = QtWidgets.QMessageBox.question(self, 'Delete Note Favorite',
                                        "Once deleted, a note favorite cannot be recovered.  Are you sure you want to delete?")

      if reply == QtWidgets.QMessageBox.StandardButton.Yes:
        result = self.db.deleteNote(noteId)

        if not result:
          logging.error(f"[EditFavoriteNotesDialog] Failed to delete favorite note {noteId}.")
          QtWidgets.QMessageBox.critical(self,
                                        "Delete Note Favorite",
                                        "An error occurred when deleting the favorite note.")
          return

        self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
        self.noteManager.removeNoteFromFavorites(noteId)

  @QtCore.Slot(QtWidgets.QListWidgetItem)
  def on_listWidget_itemChanged(self, item: QtWidgets.QListWidgetItem):
    """Handles the item changed event in the list widget."""
    noteId = item.data(QtCore.Qt.ItemDataRole.UserRole)
    if noteId:
      newTitle = item.text()
      result = self.db.updateNoteTitle(noteId, newTitle)

      if not result:
        logging.error(f"[EditFavoriteNotesDialog] Failed to update favorite note {noteId} title.")
        QtWidgets.QMessageBox.critical(self,
                              "Change favorite",
                              "An error occurred when changing the favorite's title.")
        return

      self.noteManager.updateFavoriteNoteTitle(noteId, newTitle)
