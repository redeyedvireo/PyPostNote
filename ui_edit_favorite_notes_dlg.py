# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_favorite_notes_dlg.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_EditFavoriteNotesDialog(object):
    def setupUi(self, EditFavoriteNotesDialog):
        if not EditFavoriteNotesDialog.objectName():
            EditFavoriteNotesDialog.setObjectName(u"EditFavoriteNotesDialog")
        EditFavoriteNotesDialog.resize(399, 348)
        self.verticalLayout = QVBoxLayout(EditFavoriteNotesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(EditFavoriteNotesDialog)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.editButton = QPushButton(EditFavoriteNotesDialog)
        self.editButton.setObjectName(u"editButton")

        self.horizontalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(EditFavoriteNotesDialog)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(EditFavoriteNotesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(EditFavoriteNotesDialog)
        self.buttonBox.accepted.connect(EditFavoriteNotesDialog.accept)
        self.buttonBox.rejected.connect(EditFavoriteNotesDialog.reject)

        QMetaObject.connectSlotsByName(EditFavoriteNotesDialog)
    # setupUi

    def retranslateUi(self, EditFavoriteNotesDialog):
        EditFavoriteNotesDialog.setWindowTitle(QCoreApplication.translate("EditFavoriteNotesDialog", u"Edit Favorite Notes", None))
        self.editButton.setText(QCoreApplication.translate("EditFavoriteNotesDialog", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("EditFavoriteNotesDialog", u"Delete", None))
    # retranslateUi

