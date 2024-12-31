# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'postnote.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)
import postnote_rc

class Ui_PostNoteClass(object):
    def setupUi(self, PostNoteClass):
        if not PostNoteClass.objectName():
            PostNoteClass.setObjectName(u"PostNoteClass")
        PostNoteClass.resize(224, 138)
        self.actionNew_Note = QAction(PostNoteClass)
        self.actionNew_Note.setObjectName(u"actionNew_Note")
        self.actionSave_All_Notes = QAction(PostNoteClass)
        self.actionSave_All_Notes.setObjectName(u"actionSave_All_Notes")
        self.actionHide_All_Notes = QAction(PostNoteClass)
        self.actionHide_All_Notes.setObjectName(u"actionHide_All_Notes")
        self.actionShow_All_Notes = QAction(PostNoteClass)
        self.actionShow_All_Notes.setObjectName(u"actionShow_All_Notes")
        self.actionShow_Note = QAction(PostNoteClass)
        self.actionShow_Note.setObjectName(u"actionShow_Note")
        self.actionImport_Notes = QAction(PostNoteClass)
        self.actionImport_Notes.setObjectName(u"actionImport_Notes")
        self.actionExport_Notes = QAction(PostNoteClass)
        self.actionExport_Notes.setObjectName(u"actionExport_Notes")
        self.actionEdit_Topics = QAction(PostNoteClass)
        self.actionEdit_Topics.setObjectName(u"actionEdit_Topics")
        self.actionPreferences = QAction(PostNoteClass)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionAbout_PostNote = QAction(PostNoteClass)
        self.actionAbout_PostNote.setObjectName(u"actionAbout_PostNote")
        self.actionExit_PostNote = QAction(PostNoteClass)
        self.actionExit_PostNote.setObjectName(u"actionExit_PostNote")
        self.actionAbout_Qt = QAction(PostNoteClass)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionSmall = QAction(PostNoteClass)
        self.actionSmall.setObjectName(u"actionSmall")
        self.actionMedium = QAction(PostNoteClass)
        self.actionMedium.setObjectName(u"actionMedium")
        self.actionLarge = QAction(PostNoteClass)
        self.actionLarge.setObjectName(u"actionLarge")
        self.actionExtra_Large = QAction(PostNoteClass)
        self.actionExtra_Large.setObjectName(u"actionExtra_Large")
        self.actionDebug_Mode = QAction(PostNoteClass)
        self.actionDebug_Mode.setObjectName(u"actionDebug_Mode")
        self.actionDebug_Mode.setMenuRole(QAction.MenuRole.NoRole)
        self.centralWidget = QWidget(PostNoteClass)
        self.centralWidget.setObjectName(u"centralWidget")
        PostNoteClass.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(PostNoteClass)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 224, 33))
        PostNoteClass.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(PostNoteClass)
        self.statusBar.setObjectName(u"statusBar")
        PostNoteClass.setStatusBar(self.statusBar)

        self.retranslateUi(PostNoteClass)

        QMetaObject.connectSlotsByName(PostNoteClass)
    # setupUi

    def retranslateUi(self, PostNoteClass):
        PostNoteClass.setWindowTitle(QCoreApplication.translate("PostNoteClass", u"PostNote", None))
        self.actionNew_Note.setText(QCoreApplication.translate("PostNoteClass", u"New Note", None))
        self.actionSave_All_Notes.setText(QCoreApplication.translate("PostNoteClass", u"Save All Notes", None))
        self.actionHide_All_Notes.setText(QCoreApplication.translate("PostNoteClass", u"Hide All Notes", None))
        self.actionShow_All_Notes.setText(QCoreApplication.translate("PostNoteClass", u"Show All Notes", None))
        self.actionShow_Note.setText(QCoreApplication.translate("PostNoteClass", u"Show Note", None))
        self.actionImport_Notes.setText(QCoreApplication.translate("PostNoteClass", u"Import Notes...", None))
        self.actionExport_Notes.setText(QCoreApplication.translate("PostNoteClass", u"Export Notes...", None))
        self.actionEdit_Topics.setText(QCoreApplication.translate("PostNoteClass", u"Edit Topics...", None))
        self.actionPreferences.setText(QCoreApplication.translate("PostNoteClass", u"Preferences...", None))
#if QT_CONFIG(tooltip)
        self.actionPreferences.setToolTip(QCoreApplication.translate("PostNoteClass", u"PostNote Preferences", None))
#endif // QT_CONFIG(tooltip)
        self.actionAbout_PostNote.setText(QCoreApplication.translate("PostNoteClass", u"About PostNote...", None))
        self.actionExit_PostNote.setText(QCoreApplication.translate("PostNoteClass", u"Exit PostNote", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("PostNoteClass", u"About Qt...", None))
        self.actionSmall.setText(QCoreApplication.translate("PostNoteClass", u"Small", None))
#if QT_CONFIG(tooltip)
        self.actionSmall.setToolTip(QCoreApplication.translate("PostNoteClass", u"Create a small note", None))
#endif // QT_CONFIG(tooltip)
        self.actionMedium.setText(QCoreApplication.translate("PostNoteClass", u"Medium", None))
#if QT_CONFIG(tooltip)
        self.actionMedium.setToolTip(QCoreApplication.translate("PostNoteClass", u"Create a medium note", None))
#endif // QT_CONFIG(tooltip)
        self.actionLarge.setText(QCoreApplication.translate("PostNoteClass", u"Large", None))
#if QT_CONFIG(tooltip)
        self.actionLarge.setToolTip(QCoreApplication.translate("PostNoteClass", u"Create a large note", None))
#endif // QT_CONFIG(tooltip)
        self.actionExtra_Large.setText(QCoreApplication.translate("PostNoteClass", u"Extra Large", None))
#if QT_CONFIG(tooltip)
        self.actionExtra_Large.setToolTip(QCoreApplication.translate("PostNoteClass", u"Create an extra large note", None))
#endif // QT_CONFIG(tooltip)
        self.actionDebug_Mode.setText(QCoreApplication.translate("PostNoteClass", u"Debug Mode...", None))
    # retranslateUi

