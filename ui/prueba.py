# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prueba.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ventana(object):
    def setupUi(self, ventana):
        if not ventana.objectName():
            ventana.setObjectName(u"ventana")
        ventana.resize(886, 512)
        ventana.setMinimumSize(QSize(0, 0))
        ventana.setStyleSheet(u"background:#fff")
        #sizePolicy_expand = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #self.verticalLayoutWidget.setSizePolicy(sizePolicy_expand)
        self.verticalLayout = QVBoxLayout(ventana)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton()
        self.pushButton.setObjectName(u"pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton()
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout.addStretch(1)
        self.retranslateUi(ventana)

        QMetaObject.connectSlotsByName(ventana)
    # setupUi

    def retranslateUi(self, ventana):
        ventana.setWindowTitle(QCoreApplication.translate("ventana", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("ventana", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("ventana", u"PushButton", None))
    # retranslateUi

