# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'button_bar_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QToolButton, QWidget)
import postnote_rc

class Ui_ButtonBarWidget(object):
    def setupUi(self, ButtonBarWidget):
        if not ButtonBarWidget.objectName():
            ButtonBarWidget.setObjectName(u"ButtonBarWidget")
        ButtonBarWidget.resize(383, 32)
        ButtonBarWidget.setWindowOpacity(0.300000000000000)
        ButtonBarWidget.setAutoFillBackground(True)
        ButtonBarWidget.setStyleSheet(u"QToolButton {\n"
"    background-color: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(ButtonBarWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.deleteButton = QToolButton(ButtonBarWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/PostNote/Resources/trash-can.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.deleteButton)

        self.hideButton = QToolButton(ButtonBarWidget)
        self.hideButton.setObjectName(u"hideButton")
        icon1 = QIcon()
        icon1.addFile(u":/PostNote/Resources/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hideButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.hideButton)

        self.horizontalSpacer = QSpacerItem(209, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.propertiesButton = QToolButton(ButtonBarWidget)
        self.propertiesButton.setObjectName(u"propertiesButton")
        icon2 = QIcon()
        icon2.addFile(u":/PostNote/Resources/properties.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.propertiesButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.propertiesButton)

        self.topicButton = QToolButton(ButtonBarWidget)
        self.topicButton.setObjectName(u"topicButton")
        icon3 = QIcon()
        icon3.addFile(u":/PostNote/Resources/PostNote.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.topicButton.setIcon(icon3)
        self.topicButton.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)

        self.horizontalLayout.addWidget(self.topicButton)


        self.retranslateUi(ButtonBarWidget)

        QMetaObject.connectSlotsByName(ButtonBarWidget)
    # setupUi

    def retranslateUi(self, ButtonBarWidget):
        ButtonBarWidget.setWindowTitle(QCoreApplication.translate("ButtonBarWidget", u"ButtonBarWidget", None))
#if QT_CONFIG(tooltip)
        self.deleteButton.setToolTip(QCoreApplication.translate("ButtonBarWidget", u"Delete note", None))
#endif // QT_CONFIG(tooltip)
        self.deleteButton.setText("")
#if QT_CONFIG(tooltip)
        self.hideButton.setToolTip(QCoreApplication.translate("ButtonBarWidget", u"Hide note", None))
#endif // QT_CONFIG(tooltip)
        self.hideButton.setText("")
#if QT_CONFIG(tooltip)
        self.propertiesButton.setToolTip(QCoreApplication.translate("ButtonBarWidget", u"Properties", None))
#endif // QT_CONFIG(tooltip)
        self.propertiesButton.setText("")
#if QT_CONFIG(tooltip)
        self.topicButton.setToolTip(QCoreApplication.translate("ButtonBarWidget", u"Topics", None))
#endif // QT_CONFIG(tooltip)
        self.topicButton.setText("")
    # retranslateUi

