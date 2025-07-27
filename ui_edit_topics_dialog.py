# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_topics_dialog.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_EditTopicsDialog(object):
    def setupUi(self, EditTopicsDialog):
        if not EditTopicsDialog.objectName():
            EditTopicsDialog.setObjectName(u"EditTopicsDialog")
        EditTopicsDialog.resize(279, 355)
        EditTopicsDialog.setMinimumSize(QSize(279, 0))
        EditTopicsDialog.setMaximumSize(QSize(279, 16777215))
        EditTopicsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QVBoxLayout(EditTopicsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topicListWidget = QListWidget(EditTopicsDialog)
        self.topicListWidget.setObjectName(u"topicListWidget")

        self.verticalLayout.addWidget(self.topicListWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(EditTopicsDialog)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)

        self.editButton = QPushButton(EditTopicsDialog)
        self.editButton.setObjectName(u"editButton")

        self.horizontalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(EditTopicsDialog)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(EditTopicsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(EditTopicsDialog)
        self.buttonBox.accepted.connect(EditTopicsDialog.accept)
        self.buttonBox.rejected.connect(EditTopicsDialog.reject)

        QMetaObject.connectSlotsByName(EditTopicsDialog)
    # setupUi

    def retranslateUi(self, EditTopicsDialog):
        EditTopicsDialog.setWindowTitle(QCoreApplication.translate("EditTopicsDialog", u"Edit Topics", None))
        self.addButton.setText(QCoreApplication.translate("EditTopicsDialog", u"Add...", None))
        self.editButton.setText(QCoreApplication.translate("EditTopicsDialog", u"Edit...", None))
        self.deleteButton.setText(QCoreApplication.translate("EditTopicsDialog", u"Delete", None))
    # retranslateUi

