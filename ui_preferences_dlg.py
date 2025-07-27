# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences_dlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFontComboBox, QFormLayout,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QSpinBox, QTimeEdit, QVBoxLayout, QWidget)

class Ui_PreferencesDlg(object):
    def setupUi(self, PreferencesDlg):
        if not PreferencesDlg.objectName():
            PreferencesDlg.setObjectName(u"PreferencesDlg")
        PreferencesDlg.resize(337, 243)
        self.verticalLayout = QVBoxLayout(PreferencesDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(PreferencesDlg)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.fontComboBox = QFontComboBox(PreferencesDlg)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.fontComboBox)

        self.label_4 = QLabel(PreferencesDlg)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.fontSizeComboBox = QComboBox(PreferencesDlg)
        self.fontSizeComboBox.setObjectName(u"fontSizeComboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.fontSizeComboBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(PreferencesDlg)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.autosaveSpinBox = QSpinBox(PreferencesDlg)
        self.autosaveSpinBox.setObjectName(u"autosaveSpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autosaveSpinBox.sizePolicy().hasHeightForWidth())
        self.autosaveSpinBox.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.autosaveSpinBox)

        self.label_2 = QLabel(PreferencesDlg)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(PreferencesDlg)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.doubleClickActionComboBox = QComboBox(PreferencesDlg)
        self.doubleClickActionComboBox.addItem("")
        self.doubleClickActionComboBox.addItem("")
        self.doubleClickActionComboBox.addItem("")
        self.doubleClickActionComboBox.addItem("")
        self.doubleClickActionComboBox.addItem("")
        self.doubleClickActionComboBox.addItem("")
        self.doubleClickActionComboBox.setObjectName(u"doubleClickActionComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doubleClickActionComboBox.sizePolicy().hasHeightForWidth())
        self.doubleClickActionComboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.doubleClickActionComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.autoShutdownCheckBox = QCheckBox(PreferencesDlg)
        self.autoShutdownCheckBox.setObjectName(u"autoShutdownCheckBox")

        self.verticalLayout.addWidget(self.autoShutdownCheckBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_6 = QLabel(PreferencesDlg)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.shutdownTimeEdit = QTimeEdit(PreferencesDlg)
        self.shutdownTimeEdit.setObjectName(u"shutdownTimeEdit")

        self.horizontalLayout_3.addWidget(self.shutdownTimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.buttonBox = QDialogButtonBox(PreferencesDlg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PreferencesDlg)
        self.buttonBox.accepted.connect(PreferencesDlg.accept)
        self.buttonBox.rejected.connect(PreferencesDlg.reject)

        self.doubleClickActionComboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PreferencesDlg)
    # setupUi

    def retranslateUi(self, PreferencesDlg):
        PreferencesDlg.setWindowTitle(QCoreApplication.translate("PreferencesDlg", u"Postnote Preferences", None))
        self.label_3.setText(QCoreApplication.translate("PreferencesDlg", u"Default font", None))
        self.label_4.setText(QCoreApplication.translate("PreferencesDlg", u"Default font size", None))
        self.label.setText(QCoreApplication.translate("PreferencesDlg", u"Autosave time", None))
        self.label_2.setText(QCoreApplication.translate("PreferencesDlg", u"minutes", None))
        self.label_5.setText(QCoreApplication.translate("PreferencesDlg", u"Tray icon double-click", None))
        self.doubleClickActionComboBox.setItemText(0, QCoreApplication.translate("PreferencesDlg", u"Create Small Note", None))
        self.doubleClickActionComboBox.setItemText(1, QCoreApplication.translate("PreferencesDlg", u"Create Medium Note", None))
        self.doubleClickActionComboBox.setItemText(2, QCoreApplication.translate("PreferencesDlg", u"Create Large Note", None))
        self.doubleClickActionComboBox.setItemText(3, QCoreApplication.translate("PreferencesDlg", u"Create Extra Large Note", None))
        self.doubleClickActionComboBox.setItemText(4, QCoreApplication.translate("PreferencesDlg", u"Quick Create Dialog", None))
        self.doubleClickActionComboBox.setItemText(5, QCoreApplication.translate("PreferencesDlg", u"Show All Notes", None))

        self.autoShutdownCheckBox.setText(QCoreApplication.translate("PreferencesDlg", u"Shut down automatically", None))
        self.label_6.setText(QCoreApplication.translate("PreferencesDlg", u"Auto-shutdown time", None))
    # retranslateUi

