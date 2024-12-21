# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_toolbar.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFontComboBox, QHBoxLayout,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)
import postnote_rc

class Ui_EditToolbar(object):
    def setupUi(self, EditToolbar):
        if not EditToolbar.objectName():
            EditToolbar.setObjectName(u"EditToolbar")
        EditToolbar.resize(262, 51)
        self.verticalLayout = QVBoxLayout(EditToolbar)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fontComboBox = QFontComboBox(EditToolbar)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout.addWidget(self.fontComboBox)

        self.sizeComboBox = QComboBox(EditToolbar)
        self.sizeComboBox.setObjectName(u"sizeComboBox")
        self.sizeComboBox.setMinimumSize(QSize(65, 0))
        self.sizeComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout.addWidget(self.sizeComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftAlignButton = QToolButton(EditToolbar)
        self.leftAlignButton.setObjectName(u"leftAlignButton")
        self.leftAlignButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon()
        icon.addFile(u":/PostNote/Resources/Left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leftAlignButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.leftAlignButton)

        self.centerAlignButton = QToolButton(EditToolbar)
        self.centerAlignButton.setObjectName(u"centerAlignButton")
        self.centerAlignButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/PostNote/Resources/Center.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.centerAlignButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.centerAlignButton)

        self.rightAlignButton = QToolButton(EditToolbar)
        self.rightAlignButton.setObjectName(u"rightAlignButton")
        self.rightAlignButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/PostNote/Resources/Right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rightAlignButton.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.rightAlignButton)

        self.boldButton = QToolButton(EditToolbar)
        self.boldButton.setObjectName(u"boldButton")
        self.boldButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/PostNote/Resources/Bold.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boldButton.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.boldButton)

        self.italicButton = QToolButton(EditToolbar)
        self.italicButton.setObjectName(u"italicButton")
        self.italicButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u":/PostNote/Resources/Italic.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.italicButton.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.italicButton)

        self.underlineButton = QToolButton(EditToolbar)
        self.underlineButton.setObjectName(u"underlineButton")
        self.underlineButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon5 = QIcon()
        icon5.addFile(u":/PostNote/Resources/Underline.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.underlineButton.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.underlineButton)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLineButton = QToolButton(EditToolbar)
        self.horizontalLineButton.setObjectName(u"horizontalLineButton")
        self.horizontalLineButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon6 = QIcon()
        icon6.addFile(u":/PostNote/Resources/Horiz Line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.horizontalLineButton.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.horizontalLineButton)

        self.bulletListInsertButton = QToolButton(EditToolbar)
        self.bulletListInsertButton.setObjectName(u"bulletListInsertButton")
        self.bulletListInsertButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon7 = QIcon()
        icon7.addFile(u":/PostNote/Resources/Bullet Table.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bulletListInsertButton.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.bulletListInsertButton)

        self.numberListInsertButton = QToolButton(EditToolbar)
        self.numberListInsertButton.setObjectName(u"numberListInsertButton")
        self.numberListInsertButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon8 = QIcon()
        icon8.addFile(u":/PostNote/Resources/Number Table.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.numberListInsertButton.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.numberListInsertButton)

        self.tableInsertButton = QToolButton(EditToolbar)
        self.tableInsertButton.setObjectName(u"tableInsertButton")
        self.tableInsertButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon9 = QIcon()
        icon9.addFile(u":/PostNote/Resources/Table.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tableInsertButton.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.tableInsertButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(EditToolbar)

        QMetaObject.connectSlotsByName(EditToolbar)
    # setupUi

    def retranslateUi(self, EditToolbar):
        EditToolbar.setWindowTitle(QCoreApplication.translate("EditToolbar", u"Edit", None))
#if QT_CONFIG(tooltip)
        self.fontComboBox.setToolTip(QCoreApplication.translate("EditToolbar", u"Change Font Family", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sizeComboBox.setToolTip(QCoreApplication.translate("EditToolbar", u"Change Font Size", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.leftAlignButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Align Left", None))
#endif // QT_CONFIG(tooltip)
        self.leftAlignButton.setText(QCoreApplication.translate("EditToolbar", u"L", None))
#if QT_CONFIG(tooltip)
        self.centerAlignButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Align Center", None))
#endif // QT_CONFIG(tooltip)
        self.centerAlignButton.setText(QCoreApplication.translate("EditToolbar", u"C", None))
#if QT_CONFIG(tooltip)
        self.rightAlignButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Align Right", None))
#endif // QT_CONFIG(tooltip)
        self.rightAlignButton.setText(QCoreApplication.translate("EditToolbar", u"R", None))
#if QT_CONFIG(tooltip)
        self.boldButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Bold", None))
#endif // QT_CONFIG(tooltip)
        self.boldButton.setText(QCoreApplication.translate("EditToolbar", u"B", None))
#if QT_CONFIG(tooltip)
        self.italicButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Italic", None))
#endif // QT_CONFIG(tooltip)
        self.italicButton.setText(QCoreApplication.translate("EditToolbar", u"I", None))
#if QT_CONFIG(tooltip)
        self.underlineButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Underline", None))
#endif // QT_CONFIG(tooltip)
        self.underlineButton.setText(QCoreApplication.translate("EditToolbar", u"U", None))
#if QT_CONFIG(tooltip)
        self.horizontalLineButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Insert Horizontal Line", None))
#endif // QT_CONFIG(tooltip)
        self.horizontalLineButton.setText("")
#if QT_CONFIG(tooltip)
        self.bulletListInsertButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Insert Bulleted List", None))
#endif // QT_CONFIG(tooltip)
        self.bulletListInsertButton.setText(QCoreApplication.translate("EditToolbar", u"Bl", None))
#if QT_CONFIG(tooltip)
        self.numberListInsertButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Insert Numbered List", None))
#endif // QT_CONFIG(tooltip)
        self.numberListInsertButton.setText(QCoreApplication.translate("EditToolbar", u"N", None))
#if QT_CONFIG(tooltip)
        self.tableInsertButton.setToolTip(QCoreApplication.translate("EditToolbar", u"Insert Table", None))
#endif // QT_CONFIG(tooltip)
        self.tableInsertButton.setText(QCoreApplication.translate("EditToolbar", u"Tb", None))
    # retranslateUi

