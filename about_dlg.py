from PySide6 import QtCore, QtWidgets, QtGui
from ui_about_dlg import Ui_AboutDialog

class AboutDlg(QtWidgets.QDialog):
    def __init__(self, notesPath: str, parent=None):
        super().__init__(parent)

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        # self.ui.label.setPixmap(QtGui.QPixmap(':/images/images/logo.png'))
        self.ui.notesDirectoryLabel.setText(notesPath)
