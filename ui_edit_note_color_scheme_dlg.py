# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_note_color_scheme_dlg.ui'
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
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

from color_button import ColorButton
import postnote_rc

class Ui_editNoteColorSchemeDlg(object):
    def setupUi(self, editNoteColorSchemeDlg):
        if not editNoteColorSchemeDlg.objectName():
            editNoteColorSchemeDlg.setObjectName(u"editNoteColorSchemeDlg")
        editNoteColorSchemeDlg.resize(198, 172)
        self.verticalLayout = QVBoxLayout(editNoteColorSchemeDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(editNoteColorSchemeDlg)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.typeCombo = QComboBox(editNoteColorSchemeDlg)
        self.typeCombo.setObjectName(u"typeCombo")

        self.horizontalLayout_3.addWidget(self.typeCombo)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textColorButton = ColorButton(editNoteColorSchemeDlg)
        self.textColorButton.setObjectName(u"textColorButton")
        icon = QIcon()
        icon.addFile(u":/PostNote/Resources/Text Foreground.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.textColorButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.textColorButton)

        self.bgColorButton = ColorButton(editNoteColorSchemeDlg)
        self.bgColorButton.setObjectName(u"bgColorButton")
        icon1 = QIcon()
        icon1.addFile(u":/PostNote/Resources/Text Background.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bgColorButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.bgColorButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.sampleLabel = QLabel(editNoteColorSchemeDlg)
        self.sampleLabel.setObjectName(u"sampleLabel")
        self.sampleLabel.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout.addWidget(self.sampleLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(editNoteColorSchemeDlg)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.transparencySlider = QSlider(editNoteColorSchemeDlg)
        self.transparencySlider.setObjectName(u"transparencySlider")
        self.transparencySlider.setMinimum(1)
        self.transparencySlider.setMaximum(100)
        self.transparencySlider.setValue(100)
        self.transparencySlider.setOrientation(Qt.Orientation.Horizontal)
        self.transparencySlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.transparencySlider.setTickInterval(10)

        self.horizontalLayout.addWidget(self.transparencySlider)

        self.transparencyValueLabel = QLabel(editNoteColorSchemeDlg)
        self.transparencyValueLabel.setObjectName(u"transparencyValueLabel")

        self.horizontalLayout.addWidget(self.transparencyValueLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(editNoteColorSchemeDlg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(editNoteColorSchemeDlg)
        self.buttonBox.accepted.connect(editNoteColorSchemeDlg.accept)
        self.buttonBox.rejected.connect(editNoteColorSchemeDlg.reject)

        QMetaObject.connectSlotsByName(editNoteColorSchemeDlg)
    # setupUi

    def retranslateUi(self, editNoteColorSchemeDlg):
        editNoteColorSchemeDlg.setWindowTitle(QCoreApplication.translate("editNoteColorSchemeDlg", u"Color Scheme", None))
        self.label.setText(QCoreApplication.translate("editNoteColorSchemeDlg", u"Background", None))
        self.textColorButton.setText("")
        self.bgColorButton.setText("")
        self.sampleLabel.setText(QCoreApplication.translate("editNoteColorSchemeDlg", u"Resulting Note Appearance", None))
        self.label_2.setText(QCoreApplication.translate("editNoteColorSchemeDlg", u"Transparency", None))
        self.transparencyValueLabel.setText(QCoreApplication.translate("editNoteColorSchemeDlg", u"100", None))
    # retranslateUi

