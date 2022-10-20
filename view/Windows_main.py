# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Windows_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form_main(object):
    def setupUi(self, Form_main):
        if not Form_main.objectName():
            Form_main.setObjectName(u"Form_main")
        Form_main.resize(300, 200)
        Form_main.setMinimumSize(QSize(300, 200))
        Form_main.setMaximumSize(QSize(300, 200))
        Form_main.setSizeIncrement(QSize(300, 200))
        Form_main.setBaseSize(QSize(300, 200))
        self.gridLayout = QGridLayout(Form_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main = QFrame(Form_main)
        self.main.setObjectName(u"main")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_nombre = QLineEdit(self.main)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setMaxLength(25)
        self.line_nombre.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.line_nombre)

        self.line_cali = QLineEdit(self.main)
        self.line_cali.setObjectName(u"line_cali")
        self.line_cali.setMaxLength(3)
        self.line_cali.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.line_cali)

        self.checkBox_A = QCheckBox(self.main)
        self.checkBox_A.setObjectName(u"checkBox_A")

        self.verticalLayout.addWidget(self.checkBox_A)

        self.checkBox_R = QCheckBox(self.main)
        self.checkBox_R.setObjectName(u"checkBox_R")

        self.verticalLayout.addWidget(self.checkBox_R)

        self.btn_save = QPushButton(self.main)
        self.btn_save.setObjectName(u"btn_save")

        self.verticalLayout.addWidget(self.btn_save)


        self.gridLayout.addWidget(self.main, 0, 0, 1, 1)


        self.retranslateUi(Form_main)

        QMetaObject.connectSlotsByName(Form_main)
    # setupUi

    def retranslateUi(self, Form_main):
        Form_main.setWindowTitle(QCoreApplication.translate("Form_main", u"Form", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("Form_main", u"Nombre", None))
        self.line_cali.setPlaceholderText(QCoreApplication.translate("Form_main", u"calificacion", None))
        self.checkBox_A.setText(QCoreApplication.translate("Form_main", u"Aprovado", None))
        self.checkBox_R.setText(QCoreApplication.translate("Form_main", u"Reprovado", None))
        self.btn_save.setText(QCoreApplication.translate("Form_main", u"Save", None))
    # retranslateUi

