# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mensaje.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form_mensaje(object):
    def setupUi(self, Form_mensaje):
        if not Form_mensaje.objectName():
            Form_mensaje.setObjectName(u"Form_mensaje")
        Form_mensaje.resize(500, 100)
        Form_mensaje.setMinimumSize(QSize(500, 100))
        Form_mensaje.setMaximumSize(QSize(500, 100))
        Form_mensaje.setSizeIncrement(QSize(500, 100))
        Form_mensaje.setBaseSize(QSize(500, 100))
        self.gridLayout = QGridLayout(Form_mensaje)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form_mensaje)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_msj = QLabel(self.frame)
        self.label_msj.setObjectName(u"label_msj")

        self.gridLayout_2.addWidget(self.label_msj, 0, 0, 1, 1)

        self.btn_ok = QPushButton(self.frame)
        self.btn_ok.setObjectName(u"btn_ok")

        self.gridLayout_2.addWidget(self.btn_ok, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form_mensaje)

        QMetaObject.connectSlotsByName(Form_mensaje)
    # setupUi

    def retranslateUi(self, Form_mensaje):
        Form_mensaje.setWindowTitle(QCoreApplication.translate("Form_mensaje", u"Form", None))
        self.label_msj.setText(QCoreApplication.translate("Form_mensaje", u"<html><head/><body><p align=\"center\">-text-</p></body></html>", None))
        self.btn_ok.setText(QCoreApplication.translate("Form_mensaje", u"ok", None))
    # retranslateUi

