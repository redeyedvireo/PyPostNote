# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quick_create_dlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_QuickCreateDlg(object):
    def setupUi(self, QuickCreateDlg):
        if not QuickCreateDlg.objectName():
            QuickCreateDlg.setObjectName(u"QuickCreateDlg")
        QuickCreateDlg.resize(262, 139)
        self.verticalLayout = QVBoxLayout(QuickCreateDlg)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(QuickCreateDlg)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.titleEdit = QLineEdit(QuickCreateDlg)
        self.titleEdit.setObjectName(u"titleEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titleEdit)

        self.label_2 = QLabel(QuickCreateDlg)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.sizeCombo = QComboBox(QuickCreateDlg)
        self.sizeCombo.addItem("")
        self.sizeCombo.addItem("")
        self.sizeCombo.addItem("")
        self.sizeCombo.addItem("")
        self.sizeCombo.setObjectName(u"sizeCombo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sizeCombo)

        self.label_3 = QLabel(QuickCreateDlg)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.topicCombo = QComboBox(QuickCreateDlg)
        self.topicCombo.setObjectName(u"topicCombo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topicCombo.sizePolicy().hasHeightForWidth())
        self.topicCombo.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.topicCombo)

        self.topicsButton = QPushButton(QuickCreateDlg)
        self.topicsButton.setObjectName(u"topicsButton")

        self.horizontalLayout.addWidget(self.topicsButton)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(QuickCreateDlg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(QuickCreateDlg)
        self.buttonBox.rejected.connect(QuickCreateDlg.reject)
        self.buttonBox.accepted.connect(QuickCreateDlg.accept)

        QMetaObject.connectSlotsByName(QuickCreateDlg)
    # setupUi

    def retranslateUi(self, QuickCreateDlg):
        QuickCreateDlg.setWindowTitle(QCoreApplication.translate("QuickCreateDlg", u"Create Note", None))
        self.label.setText(QCoreApplication.translate("QuickCreateDlg", u"Note Title", None))
        self.label_2.setText(QCoreApplication.translate("QuickCreateDlg", u"Size", None))
        self.sizeCombo.setItemText(0, QCoreApplication.translate("QuickCreateDlg", u"Small", None))
        self.sizeCombo.setItemText(1, QCoreApplication.translate("QuickCreateDlg", u"Medium", None))
        self.sizeCombo.setItemText(2, QCoreApplication.translate("QuickCreateDlg", u"Large", None))
        self.sizeCombo.setItemText(3, QCoreApplication.translate("QuickCreateDlg", u"Extra Large", None))

        self.label_3.setText(QCoreApplication.translate("QuickCreateDlg", u"Topic", None))
        self.topicsButton.setText(QCoreApplication.translate("QuickCreateDlg", u"Edit Topics...", None))
    # retranslateUi

