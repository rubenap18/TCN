# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_reservacion1.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 712)
        Form.setStyleSheet(u"background:#fff")
        #self.verticalLayoutWidget = QWidget(Form)
        #self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        #self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 1281, 711))
        #self.main_layout = QVBoxLayout(self.verticalLayoutWidget)
        
        self.main_layout = QVBoxLayout(Form)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(20, 0, 0, 0)
        self.var_layout = QHBoxLayout()
        self.var_layout.setObjectName(u"var_layout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.boton_regresar = QPushButton()
        self.boton_regresar.setObjectName(u"boton_regresar")

        self.verticalLayout_4.addWidget(self.boton_regresar)
        self.var_layout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_horario = QLabel()
        self.label_horario.setObjectName(u"label_horario")
        font = QFont()
        font.setPointSize(35)
        font.setWeight(QFont.DemiBold)
        self.label_horario.setFont(font)
        self.label_horario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_horario.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_horario)
        self.var_layout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_logo = QLabel(self)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setPixmap(QPixmap(u"recursos/logo.png"))
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_logo)


        self.var_layout.addLayout(self.verticalLayout_2)

        self.var_layout.setStretch(0, 1)
        self.var_layout.setStretch(1, 6)
        self.var_layout.setStretch(2, 1)

        self.main_layout.addLayout(self.var_layout)

        self.filtros_layout = QHBoxLayout()
        self.filtros_layout.setSpacing(6)
        self.filtros_layout.setObjectName(u"filtros_layout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_origen = QLabel()
        self.label_origen.setObjectName(u"label_origen")

        self.horizontalLayout_4.addWidget(self.label_origen)

        self.combo_origen = QComboBox()
        self.combo_origen.setObjectName(u"combo_origen")

        self.horizontalLayout_4.addWidget(self.combo_origen)


        self.filtros_layout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_detino = QLabel()
        self.label_detino.setObjectName(u"label_detino")

        self.horizontalLayout_3.addWidget(self.label_detino)

        self.combo_destino = QComboBox()
        self.combo_destino.setObjectName(u"combo_destino")

        self.horizontalLayout_3.addWidget(self.combo_destino)


        self.filtros_layout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_fecha = QLabel()
        self.label_fecha.setObjectName(u"label_fecha")

        self.horizontalLayout_2.addWidget(self.label_fecha)

        self.dateEdit_fecha = QDateEdit()
        self.dateEdit_fecha.setObjectName(u"dateEdit_fecha")

        self.horizontalLayout_2.addWidget(self.dateEdit_fecha)


        self.filtros_layout.addLayout(self.horizontalLayout_2)

        self.filtros_layout.setStretch(0, 1)
        self.filtros_layout.setStretch(1, 1)
        self.filtros_layout.setStretch(2, 1)

        self.main_layout.addLayout(self.filtros_layout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea()
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background:#eee")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1256, 528))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.main_layout.addLayout(self.verticalLayout)

        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 1)
        self.main_layout.setStretch(2, 6)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.boton_regresar.setText(QCoreApplication.translate("Form", u"Regresar", None))
        self.label_horario.setText(QCoreApplication.translate("Form", u"Horarios", None))
        self.label_logo.setText("")
        self.label_origen.setText(QCoreApplication.translate("Form", u"Origen:", None))
        self.label_detino.setText(QCoreApplication.translate("Form", u"Destino:", None))
        self.label_fecha.setText(QCoreApplication.translate("Form", u"Fecha:", None))
    # retranslateUi

