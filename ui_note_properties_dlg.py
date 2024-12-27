# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note_properties_dlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_notePropertiesDialog(object):
    def setupUi(self, notePropertiesDialog):
        if not notePropertiesDialog.objectName():
            notePropertiesDialog.setObjectName(u"notePropertiesDialog")
        notePropertiesDialog.resize(349, 213)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(notePropertiesDialog.sizePolicy().hasHeightForWidth())
        notePropertiesDialog.setSizePolicy(sizePolicy)
        notePropertiesDialog.setMinimumSize(QSize(349, 194))
        notePropertiesDialog.setMaximumSize(QSize(400, 300))
        notePropertiesDialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(notePropertiesDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(notePropertiesDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.createdWhenLabel = QLabel(notePropertiesDialog)
        self.createdWhenLabel.setObjectName(u"createdWhenLabel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.createdWhenLabel)

        self.label_2 = QLabel(notePropertiesDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.titleEdit = QLineEdit(notePropertiesDialog)
        self.titleEdit.setObjectName(u"titleEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.titleEdit)

        self.label_3 = QLabel(notePropertiesDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.topicCombo = QComboBox(notePropertiesDialog)
        self.topicCombo.setObjectName(u"topicCombo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topicCombo.sizePolicy().hasHeightForWidth())
        self.topicCombo.setSizePolicy(sizePolicy1)
        self.topicCombo.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_3.addWidget(self.topicCombo)

        self.editTopicsButton = QPushButton(notePropertiesDialog)
        self.editTopicsButton.setObjectName(u"editTopicsButton")
        self.editTopicsButton.setMinimumSize(QSize(0, 23))

        self.horizontalLayout_3.addWidget(self.editTopicsButton)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.alwaysOnTopCheckBox = QCheckBox(notePropertiesDialog)
        self.alwaysOnTopCheckBox.setObjectName(u"alwaysOnTopCheckBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.alwaysOnTopCheckBox)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.line = QFrame(notePropertiesDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.usesOwnColorsRadio = QRadioButton(notePropertiesDialog)
        self.usesOwnColorsRadio.setObjectName(u"usesOwnColorsRadio")

        self.horizontalLayout.addWidget(self.usesOwnColorsRadio)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editColorSchemeButton = QPushButton(notePropertiesDialog)
        self.editColorSchemeButton.setObjectName(u"editColorSchemeButton")
        self.editColorSchemeButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.editColorSchemeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.usesTopicColorsRadio = QRadioButton(notePropertiesDialog)
        self.usesTopicColorsRadio.setObjectName(u"usesTopicColorsRadio")
        self.usesTopicColorsRadio.setChecked(True)

        self.verticalLayout.addWidget(self.usesTopicColorsRadio)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.line_2 = QFrame(notePropertiesDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.buttonBox = QDialogButtonBox(notePropertiesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(notePropertiesDialog)
        self.buttonBox.accepted.connect(notePropertiesDialog.accept)
        self.buttonBox.rejected.connect(notePropertiesDialog.reject)
        self.usesOwnColorsRadio.clicked["bool"].connect(self.editColorSchemeButton.setEnabled)
        self.usesTopicColorsRadio.clicked["bool"].connect(self.editColorSchemeButton.setDisabled)

        QMetaObject.connectSlotsByName(notePropertiesDialog)
    # setupUi

    def retranslateUi(self, notePropertiesDialog):
        notePropertiesDialog.setWindowTitle(QCoreApplication.translate("notePropertiesDialog", u"Note Properties", None))
        self.label.setText(QCoreApplication.translate("notePropertiesDialog", u"Created:", None))
        self.createdWhenLabel.setText(QCoreApplication.translate("notePropertiesDialog", u"-", None))
        self.label_2.setText(QCoreApplication.translate("notePropertiesDialog", u"Title:", None))
        self.label_3.setText(QCoreApplication.translate("notePropertiesDialog", u"Topic:", None))
        self.editTopicsButton.setText(QCoreApplication.translate("notePropertiesDialog", u"Edit Topics...", None))
        self.alwaysOnTopCheckBox.setText(QCoreApplication.translate("notePropertiesDialog", u"Always On Top", None))
        self.usesOwnColorsRadio.setText(QCoreApplication.translate("notePropertiesDialog", u"Note Uses Its Own Color Scheme", None))
        self.editColorSchemeButton.setText(QCoreApplication.translate("notePropertiesDialog", u"Edit Color Scheme...", None))
        self.usesTopicColorsRadio.setText(QCoreApplication.translate("notePropertiesDialog", u"Note Inherits Color Scheme From Topic", None))
    # retranslateUi

