# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OperadorDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 517)
        Dialog.setMinimumSize(QSize(424, 517))
        Dialog.setMaximumSize(QSize(424, 517))
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
        self.line.setGeometry(QRect(20, 60, 381, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 361, 31))
        font1 = QFont()
        font1.setPointSize(21)
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 453, 171, 41))
        font2 = QFont()
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        self.can_pushButton = QPushButton(Dialog)
        self.can_pushButton.setObjectName(u"can_pushButton")
        self.can_pushButton.setGeometry(QRect(120, 453, 91, 41))
        self.can_pushButton.setFont(font2)
        self.can_pushButton.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #E85F30;   /* Naranja m\u00e1s oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC532A;   /* M\u00e1s oscuro para click */\n"
"}")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 81, 381, 66))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_2.setFont(font3)

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.widget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 38))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 24))
        font4 = QFont()
        self.name_lineEdit.setFont(font4)
        self.name_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    \n"
"	background-color: rgb(246, 245, 244);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.name_lineEdit)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 162, 381, 66))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_3)

        self.ap_lineEdit = QLineEdit(self.widget1)
        self.ap_lineEdit.setObjectName(u"ap_lineEdit")
        self.ap_lineEdit.setMinimumSize(QSize(0, 38))
        self.ap_lineEdit.setMaximumSize(QSize(16777215, 24))
        self.ap_lineEdit.setFont(font4)
        self.ap_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(246, 245, 244);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.ap_lineEdit)

        self.widget2 = QWidget(Dialog)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 239, 381, 66))
        self.verticalLayout_5 = QVBoxLayout(self.widget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_5)

        self.am_lineEdit = QLineEdit(self.widget2)
        self.am_lineEdit.setObjectName(u"am_lineEdit")
        self.am_lineEdit.setMinimumSize(QSize(0, 38))
        self.am_lineEdit.setMaximumSize(QSize(16777215, 24))
        self.am_lineEdit.setFont(font4)
        self.am_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(246, 245, 244);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.am_lineEdit)

        self.tel_lineEdit = QLineEdit(Dialog)
        self.tel_lineEdit.setObjectName(u"tel_lineEdit")
        self.tel_lineEdit.setGeometry(QRect(20, 340, 149, 38))
        self.tel_lineEdit.setMinimumSize(QSize(0, 38))
        self.tel_lineEdit.setMaximumSize(QSize(16777215, 24))
        self.tel_lineEdit.setFont(font4)
        self.tel_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(246, 245, 244);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 320, 66, 20))
        self.label_4.setFont(font3)
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(220, 341, 169, 35))
        self.dateEdit.setMinimumSize(QSize(0, 35))
        self.dateEdit.setMaximumSize(QSize(16777215, 24))
        self.dateEdit.setFont(font4)
        self.dateEdit.setStyleSheet(u"\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"")
        self.dateEdit.setMaximumDate(QDate(9997, 12, 31))
        self.dateEdit.setCalendarPopup(False)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 320, 157, 20))
        self.label_6.setFont(font3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir un nuevo operador", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir Operador", None))
        self.can_pushButton.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Apellido Parterno", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Apellido Materno", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Telefono", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Fecha de nacimiento", None))
    # retranslateUi

