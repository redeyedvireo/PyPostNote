# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note_wnd.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from text_edit import TextEdit
import postnote_rc

class Ui_NoteWnd(object):
    def setupUi(self, NoteWnd):
        if not NoteWnd.objectName():
            NoteWnd.setObjectName(u"NoteWnd")
        NoteWnd.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/PostNote/Resources/PostNote.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        NoteWnd.setWindowIcon(icon)
        NoteWnd.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(NoteWnd)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = TextEdit(NoteWnd)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(NoteWnd)

        QMetaObject.connectSlotsByName(NoteWnd)
    # setupUi

    def retranslateUi(self, NoteWnd):
        NoteWnd.setWindowTitle(QCoreApplication.translate("NoteWnd", u"New Note", None))
    # retranslateUi

