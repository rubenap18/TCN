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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_panelPrincipal(object):
    def setupUi(self, panelPrincipal):
        if not panelPrincipal.objectName():
            panelPrincipal.setObjectName(u"panelPrincipal")
        panelPrincipal.resize(1280, 820)
        self.botonCambio = QPushButton(panelPrincipal)
        self.botonCambio.setObjectName(u"botonCambio")
        self.botonCambio.setGeometry(QRect(760, 40, 161, 27))

        self.retranslateUi(panelPrincipal)

        QMetaObject.connectSlotsByName(panelPrincipal)
    # setupUi

    def retranslateUi(self, panelPrincipal):
        panelPrincipal.setWindowTitle(QCoreApplication.translate("panelPrincipal", u"Hola", None))
        self.botonCambio.setText(QCoreApplication.translate("panelPrincipal", u"Pantalla 1", None))
    # retranslateUi

