# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_topic_attr_dlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

from color_button import ColorButton
import postnote_rc

class Ui_EditTopicAttrDlg(object):
    def setupUi(self, EditTopicAttrDlg):
        if not EditTopicAttrDlg.objectName():
            EditTopicAttrDlg.setObjectName(u"EditTopicAttrDlg")
        EditTopicAttrDlg.resize(196, 211)
        self.verticalLayout = QVBoxLayout(EditTopicAttrDlg)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(EditTopicAttrDlg)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.topicEdit = QLineEdit(EditTopicAttrDlg)
        self.topicEdit.setObjectName(u"topicEdit")

        self.horizontalLayout_4.addWidget(self.topicEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(EditTopicAttrDlg)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.typeCombo = QComboBox(EditTopicAttrDlg)
        self.typeCombo.setObjectName(u"typeCombo")

        self.horizontalLayout_2.addWidget(self.typeCombo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(EditTopicAttrDlg)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textColorButton = ColorButton(EditTopicAttrDlg)
        self.textColorButton.setObjectName(u"textColorButton")
        icon = QIcon()
        icon.addFile(u":/PostNote/Resources/Text Foreground.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.textColorButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.textColorButton)

        self.bgColorButton = ColorButton(EditTopicAttrDlg)
        self.bgColorButton.setObjectName(u"bgColorButton")
        icon1 = QIcon()
        icon1.addFile(u":/PostNote/Resources/Text Background.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bgColorButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.bgColorButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.sampleLabel = QLabel(EditTopicAttrDlg)
        self.sampleLabel.setObjectName(u"sampleLabel")
        self.sampleLabel.setFrameShape(QFrame.Shape.Box)
        self.sampleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.sampleLabel)

        self.line_2 = QFrame(EditTopicAttrDlg)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(EditTopicAttrDlg)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.transparencySlider = QSlider(EditTopicAttrDlg)
        self.transparencySlider.setObjectName(u"transparencySlider")
        self.transparencySlider.setMinimum(1)
        self.transparencySlider.setMaximum(100)
        self.transparencySlider.setValue(100)
        self.transparencySlider.setOrientation(Qt.Orientation.Horizontal)
        self.transparencySlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.transparencySlider.setTickInterval(10)

        self.horizontalLayout.addWidget(self.transparencySlider)

        self.transparencyValueLabel = QLabel(EditTopicAttrDlg)
        self.transparencyValueLabel.setObjectName(u"transparencyValueLabel")

        self.horizontalLayout.addWidget(self.transparencyValueLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(EditTopicAttrDlg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(EditTopicAttrDlg)
        self.buttonBox.accepted.connect(EditTopicAttrDlg.accept)
        self.buttonBox.rejected.connect(EditTopicAttrDlg.reject)

        QMetaObject.connectSlotsByName(EditTopicAttrDlg)
    # setupUi

    def retranslateUi(self, EditTopicAttrDlg):
        EditTopicAttrDlg.setWindowTitle(QCoreApplication.translate("EditTopicAttrDlg", u"Edit Topic", None))
        self.label.setText(QCoreApplication.translate("EditTopicAttrDlg", u"Topic", None))
        self.label_2.setText(QCoreApplication.translate("EditTopicAttrDlg", u"Background", None))
        self.textColorButton.setText("")
        self.bgColorButton.setText("")
        self.sampleLabel.setText(QCoreApplication.translate("EditTopicAttrDlg", u"Resulting Note Appearance", None))
        self.label_3.setText(QCoreApplication.translate("EditTopicAttrDlg", u"Transparency", None))
        self.transparencyValueLabel.setText(QCoreApplication.translate("EditTopicAttrDlg", u"100", None))
    # retranslateUi

