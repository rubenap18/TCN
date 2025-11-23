# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1133, 642)
        MainWindow.setStyleSheet(u"background-color:white; \n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.icono = QLabel(self.centralwidget)
        self.icono.setObjectName(u"icono")
        self.icono.setGeometry(QRect(20, -20, 161, 121))
        self.icono.setPixmap(QPixmap(u"recursos/logo.png"))
        self.icono.setScaledContents(True)
        self.botonViajar = QPushButton(self.centralwidget)
        self.botonViajar.setObjectName(u"botonViajar")
        self.botonViajar.setGeometry(QRect(670, 10, 141, 41))
        font = QFont()
        font.setBold(True)
        self.botonViajar.setFont(font)
        self.botonViajar.setStyleSheet(u"color:#398FDB;\n"
"border:2px solid #398FDB;")
        self.botonDestinos = QPushButton(self.centralwidget)
        self.botonDestinos.setObjectName(u"botonDestinos")
        self.botonDestinos.setGeometry(QRect(840, 10, 141, 41))
        self.botonDestinos.setFont(font)
        self.botonDestinos.setStyleSheet(u"border: none;\n"
"background-color:  #ccc;\n"
"color: #282E30;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 130, 250, 181))
        self.label.setPixmap(QPixmap(u"recursos/slogan.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 330, 441, 91))
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 490, 31, 31))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:#398FDB;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 490, 71, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:#FF9236;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(620, 490, 71, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:#FF9236;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 520, 71, 16))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(370, 520, 71, 16))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(560, 520, 191, 41))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(600, 130, 491, 281))
        self.label_9.setPixmap(QPixmap(u"recursos/autobus.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botonCuenta = QPushButton(self.centralwidget)
        self.botonCuenta.setObjectName(u"botonCuenta")
        self.botonCuenta.setGeometry(QRect(1010, 20, 96, 27))
        self.botonMisReserv = QPushButton(self.centralwidget)
        self.botonMisReserv.setObjectName(u"botonMisReserv")
        self.botonMisReserv.setGeometry(QRect(455, 20, 191, 27))
        self.botonMisReserv.setStyleSheet(u"border: None;\n"
"color: #000;\n"
"font-weight: 600;\n"
"font-size: 18px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1133, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tu Cuervo Negro", None))
        self.icono.setText("")
        self.botonViajar.setText(QCoreApplication.translate("MainWindow", u"Viajar", None))
        self.botonDestinos.setText(QCoreApplication.translate("MainWindow", u"Destinos", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">Descubre Baja California a tu estilo. Con TCN, elige entre nuestras dos categorias de autobus y vive un viaje donde la comodidad y tecnologia transforman cada proyecto en una experiencia unica.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"24/7", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Destinos", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Soporte", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Descuento en adultos mayores y ninos.", None))
        self.label_9.setText("")
        self.botonCuenta.setText(QCoreApplication.translate("MainWindow", u"Mi Cuenta", None))
        self.botonMisReserv.setText(QCoreApplication.translate("MainWindow", u"Mis Reservaciones", None))
    # retranslateUi

