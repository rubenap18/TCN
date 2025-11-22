# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RutasDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 370)
        Dialog.setMinimumSize(QSize(424, 370))
        Dialog.setMaximumSize(QSize(424, 370))
        font = QFont()
        font.setPointSize(20)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid gray; \n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height: 24px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"	border: 1px solid gray; \n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height: 21px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 401, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 351, 31))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        self.addr_btn = QPushButton(Dialog)
        self.addr_btn.setObjectName(u"addr_btn")
        self.addr_btn.setGeometry(QRect(250, 320, 141, 24))
        font2 = QFont()
        font2.setBold(True)
        self.addr_btn.setFont(font2)
        self.addr_btn.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")
        self.btn_cancelar = QPushButton(Dialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(150, 320, 81, 24))
        self.btn_cancelar.setFont(font2)
        self.btn_cancelar.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 80, 191, 60))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_2.setFont(font3)

        self.verticalLayout.addWidget(self.label_2)

        self.cmb_origen = QComboBox(self.layoutWidget)
        self.cmb_origen.addItem("")
        self.cmb_origen.addItem("")
        self.cmb_origen.addItem("")
        self.cmb_origen.addItem("")
        self.cmb_origen.addItem("")
        self.cmb_origen.addItem("")
        self.cmb_origen.setObjectName(u"cmb_origen")
        self.cmb_origen.setStyleSheet(u"\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #909399;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    outline: none;\n"
"    selection-background-color: #409eff;\n"
"    selection-color: white;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.cmb_origen)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 150, 191, 60))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_3)

        self.cmb_destino = QComboBox(self.layoutWidget1)
        self.cmb_destino.addItem("")
        self.cmb_destino.addItem("")
        self.cmb_destino.addItem("")
        self.cmb_destino.addItem("")
        self.cmb_destino.addItem("")
        self.cmb_destino.addItem("")
        self.cmb_destino.setObjectName(u"cmb_destino")
        self.cmb_destino.setStyleSheet(u"\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #909399;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    outline: none;\n"
"    selection-background-color: #409eff;\n"
"    selection-color: white;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.cmb_destino)

        self.layoutWidget2 = QWidget(Dialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 220, 191, 66))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_5)

        self.txt_distancia = QLineEdit(self.layoutWidget2)
        self.txt_distancia.setObjectName(u"txt_distancia")
        self.txt_distancia.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f5f7fa;\n"
"    color: #c0c4cc;\n"
"    border-color: #e4e7ed;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background-color: #f5f7fa;\n"
"    color: #909399;\n"
"}")

        self.verticalLayout_3.addWidget(self.txt_distancia)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir nueva ruta", None))
        self.addr_btn.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir Ruta", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Origen", None))
        self.cmb_origen.setItemText(0, QCoreApplication.translate("Dialog", u"Tijuana", None))
        self.cmb_origen.setItemText(1, QCoreApplication.translate("Dialog", u"Mexicali", None))
        self.cmb_origen.setItemText(2, QCoreApplication.translate("Dialog", u"Ensenada", None))
        self.cmb_origen.setItemText(3, QCoreApplication.translate("Dialog", u"San Felipe", None))
        self.cmb_origen.setItemText(4, QCoreApplication.translate("Dialog", u"Tecate", None))
        self.cmb_origen.setItemText(5, QCoreApplication.translate("Dialog", u"San Quintin", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"Destino", None))
        self.cmb_destino.setItemText(0, QCoreApplication.translate("Dialog", u"Tijuana", None))
        self.cmb_destino.setItemText(1, QCoreApplication.translate("Dialog", u"Mexicali", None))
        self.cmb_destino.setItemText(2, QCoreApplication.translate("Dialog", u"Ensenada", None))
        self.cmb_destino.setItemText(3, QCoreApplication.translate("Dialog", u"San Felipe", None))
        self.cmb_destino.setItemText(4, QCoreApplication.translate("Dialog", u"Tecate", None))
        self.cmb_destino.setItemText(5, QCoreApplication.translate("Dialog", u"San Quintin", None))

        self.label_5.setText(QCoreApplication.translate("Dialog", u"Distancia", None))
    # retranslateUi

