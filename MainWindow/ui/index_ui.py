# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from ui import resources_rc



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1920, 1080))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setGeometry(QRect(300, 20, 1561, 101))
        self.header_widget.setStyleSheet(u"background-color: #F5F3F1;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.rutas_pushButton = QPushButton(self.header_widget)
        self.rutas_pushButton.setObjectName(u"rutas_pushButton")
        self.rutas_pushButton.setGeometry(QRect(30, 20, 201, 71))
        font = QFont()
        font.setBold(True)
        self.rutas_pushButton.setFont(font)
        self.rutas_pushButton.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon = QIcon()
        icon.addFile(u":/recursos/Icons/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rutas_pushButton.setIcon(icon)
        self.rutas_pushButton.setIconSize(QSize(30, 30))
        self.corridas_pushButton = QPushButton(self.header_widget)
        self.corridas_pushButton.setObjectName(u"corridas_pushButton")
        self.corridas_pushButton.setGeometry(QRect(250, 20, 201, 71))
        self.corridas_pushButton.setFont(font)
        self.corridas_pushButton.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/recursos/Icons/calendario(1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.corridas_pushButton.setIcon(icon1)
        self.corridas_pushButton.setIconSize(QSize(30, 30))
        self.operadores_pushButton = QPushButton(self.header_widget)
        self.operadores_pushButton.setObjectName(u"operadores_pushButton")
        self.operadores_pushButton.setGeometry(QRect(470, 20, 201, 71))
        self.operadores_pushButton.setFont(font)
        self.operadores_pushButton.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/recursos/Icons/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operadores_pushButton.setIcon(icon2)
        self.operadores_pushButton.setIconSize(QSize(25, 25))
        self.autobuses_pushButton = QPushButton(self.header_widget)
        self.autobuses_pushButton.setObjectName(u"autobuses_pushButton")
        self.autobuses_pushButton.setGeometry(QRect(690, 20, 201, 71))
        self.autobuses_pushButton.setFont(font)
        self.autobuses_pushButton.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/recursos/Icons/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.autobuses_pushButton.setIcon(icon3)
        self.autobuses_pushButton.setIconSize(QSize(30, 30))
        self.pasajeros_pushButton = QPushButton(self.header_widget)
        self.pasajeros_pushButton.setObjectName(u"pasajeros_pushButton")
        self.pasajeros_pushButton.setGeometry(QRect(910, 20, 201, 71))
        self.pasajeros_pushButton.setFont(font)
        self.pasajeros_pushButton.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/recursos/Icons/pasajero.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pasajeros_pushButton.setIcon(icon4)
        self.pasajeros_pushButton.setIconSize(QSize(30, 30))
        self.label_2 = QLabel(self.header_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1460, 20, 71, 71))
        self.label_2.setPixmap(QPixmap(u":/recursos/Icons/gente.png"))
        self.label_2.setScaledContents(True)
        self.main_stackedWidget = QStackedWidget(self.centralwidget)
        self.main_stackedWidget.setObjectName(u"main_stackedWidget")
        self.main_stackedWidget.setGeometry(QRect(300, 150, 1561, 881))
        self.main_stackedWidget.setStyleSheet(u"background-color: #F5F3F1;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.corridasm_tableWidget = QTableWidget(self.main)
        if (self.corridasm_tableWidget.columnCount() < 4):
            self.corridasm_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.corridasm_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.corridasm_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.corridasm_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.corridasm_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.corridasm_tableWidget.setObjectName(u"corridasm_tableWidget")
        self.corridasm_tableWidget.setGeometry(QRect(110, 30, 751, 361))
        self.corridasm_tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.corridasm_tableWidget.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 15px;\n"
"    gridline-color: #e0e0e0;\n"
"    outline: none;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #409eff;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5f7fa;\n"
"}\n"
"\n"
"/* Header con bordes redondeados solo arriba */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1061C4;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    padding: 8px 12px;\n"
"    border: none;\n"
"    border-right: 1px solid #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color:"
                        " #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:pressed {\n"
"    background-color: #083a7a;\n"
"}\n"
"")
        self.corridasm_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.corridasm_tableWidget.horizontalHeader().setDefaultSectionSize(187)
        self.corridasm_tableWidget.verticalHeader().setVisible(False)
        self.autobusm_tableWidget = QTableWidget(self.main)
        if (self.autobusm_tableWidget.columnCount() < 4):
            self.autobusm_tableWidget.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.autobusm_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.autobusm_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.autobusm_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.autobusm_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.autobusm_tableWidget.setObjectName(u"autobusm_tableWidget")
        self.autobusm_tableWidget.setGeometry(QRect(110, 480, 751, 361))
        self.autobusm_tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.autobusm_tableWidget.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 15px;\n"
"    gridline-color: #e0e0e0;\n"
"    outline: none;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #409eff;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5f7fa;\n"
"}\n"
"\n"
"/* Header con bordes redondeados solo arriba */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1061C4;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    padding: 8px 12px;\n"
"    border: none;\n"
"    border-right: 1px solid #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color:"
                        " #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:pressed {\n"
"    background-color: #083a7a;\n"
"}\n"
"")
        self.autobusm_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.autobusm_tableWidget.horizontalHeader().setDefaultSectionSize(187)
        self.autobusm_tableWidget.verticalHeader().setVisible(False)
        self.pasajerosm_tableWidget = QTableWidget(self.main)
        if (self.pasajerosm_tableWidget.columnCount() < 4):
            self.pasajerosm_tableWidget.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.pasajerosm_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.pasajerosm_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.pasajerosm_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.pasajerosm_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.pasajerosm_tableWidget.setObjectName(u"pasajerosm_tableWidget")
        self.pasajerosm_tableWidget.setGeometry(QRect(960, 30, 511, 811))
        self.pasajerosm_tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pasajerosm_tableWidget.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 15px;\n"
"    gridline-color: #e0e0e0;\n"
"    outline: none;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #409eff;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5f7fa;\n"
"}\n"
"\n"
"/* Header con bordes redondeados solo arriba */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1061C4;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    padding: 8px 12px;\n"
"    border: none;\n"
"    border-right: 1px solid #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color:"
                        " #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:pressed {\n"
"    background-color: #083a7a;\n"
"}\n"
"")
        self.pasajerosm_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.pasajerosm_tableWidget.horizontalHeader().setDefaultSectionSize(127)
        self.pasajerosm_tableWidget.verticalHeader().setVisible(False)
        self.main_stackedWidget.addWidget(self.main)
        self.operadores = QWidget()
        self.operadores.setObjectName(u"operadores")
        self.label_8 = QLabel(self.operadores)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 80, 581, 71))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_8.setFont(font1)
        self.o_tableWidget = QTableWidget(self.operadores)
        if (self.o_tableWidget.columnCount() < 5):
            self.o_tableWidget.setColumnCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        self.o_tableWidget.setObjectName(u"o_tableWidget")
        self.o_tableWidget.setGeometry(QRect(80, 170, 1421, 661))
        self.o_tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.o_tableWidget.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 15px;\n"
"    gridline-color: #e0e0e0;\n"
"    outline: none;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #409eff;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5f7fa;\n"
"}\n"
"\n"
"/* Header con bordes redondeados solo arriba */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1061C4;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    padding: 8px 12px;\n"
"    border: none;\n"
"    border-right: 1px solid #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color:"
                        " #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:pressed {\n"
"    background-color: #083a7a;\n"
"}\n"
"\n"
"")
        self.o_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.o_tableWidget.horizontalHeader().setDefaultSectionSize(284)
        self.o_tableWidget.verticalHeader().setVisible(False)
        self.main_stackedWidget.addWidget(self.operadores)
        self.rutas = QWidget()
        self.rutas.setObjectName(u"rutas")
        self.label_7 = QLabel(self.rutas)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 70, 341, 81))
        self.label_7.setFont(font1)
        self.frame_2 = QFrame(self.rutas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(90, 160, 1381, 661))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(0)
        self.rutas_tableWidget = QTableWidget(self.frame_2)
        if (self.rutas_tableWidget.columnCount() < 4):
            self.rutas_tableWidget.setColumnCount(4)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.rutas_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font);
        self.rutas_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font);
        self.rutas_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font);
        self.rutas_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        self.rutas_tableWidget.setObjectName(u"rutas_tableWidget")
        self.rutas_tableWidget.setGeometry(QRect(0, 0, 1421, 661))
        self.rutas_tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.rutas_tableWidget.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 15px;\n"
"    gridline-color: #e0e0e0;\n"
"    outline: none;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #409eff;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5f7fa;\n"
"}\n"
"\n"
"/* Header con bordes redondeados solo arriba */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1061C4;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    padding: 8px 12px;\n"
"    border: none;\n"
"    border-right: 1px solid #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color:"
                        " #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:pressed {\n"
"    background-color: #083a7a;\n"
"}\n"
"")
        self.rutas_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.rutas_tableWidget.setAlternatingRowColors(True)
        self.rutas_tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.rutas_tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.rutas_tableWidget.setShowGrid(False)
        self.rutas_tableWidget.horizontalHeader().setDefaultSectionSize(345)
        self.rutas_tableWidget.verticalHeader().setVisible(False)
        self.rutas_tableWidget.verticalHeader().setHighlightSections(False)
        self.main_stackedWidget.addWidget(self.rutas)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 241, 61))
        self.label.setPixmap(QPixmap(u":/recursos/Icons/Screenshot from 2025-11-22 14-58-14.png"))
        self.label.setScaledContents(True)
        self.side_stackedWidget = QStackedWidget(self.centralwidget)
        self.side_stackedWidget.setObjectName(u"side_stackedWidget")
        self.side_stackedWidget.setGeometry(QRect(50, 150, 221, 901))
        self.side_stackedWidget.setStyleSheet(u"background-color: #F5F3F1;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 350, 191, 26))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.label_9.setFont(font2)
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 390, 41, 26))
        font3 = QFont()
        font3.setPointSize(23)
        font3.setBold(True)
        self.label_10.setFont(font3)
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 440, 91, 26))
        self.label_11.setFont(font2)
        self.side_stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.addo_btn = QPushButton(self.page)
        self.addo_btn.setObjectName(u"addo_btn")
        self.addo_btn.setGeometry(QRect(20, 110, 181, 61))
        self.addo_btn.setFont(font)
        self.addo_btn.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E85F30;   /* Naranja m\u00e1s oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC532A;   /* M\u00e1s oscuro para click */\n"
"}")
        self.addo_btn.setIcon(icon2)
        self.addo_btn.setIconSize(QSize(30, 30))
        self.srch_line = QLineEdit(self.page)
        self.srch_line.setObjectName(u"srch_line")
        self.srch_line.setGeometry(QRect(20, 30, 181, 61))
        self.srch_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 15px;\n"
"    color: #606266;\n"
"    min-height: 15px;\n"
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
        self.edito_btn = QPushButton(self.page)
        self.edito_btn.setObjectName(u"edito_btn")
        self.edito_btn.setGeometry(QRect(20, 190, 181, 61))
        self.edito_btn.setFont(font)
        self.edito_btn.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E85F30;   /* Naranja m\u00e1s oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC532A;   /* M\u00e1s oscuro para click */\n"
"}")
        self.edito_btn.setIcon(icon)
        self.edito_btn.setIconSize(QSize(30, 30))
        self.side_stackedWidget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.addr_btn = QPushButton(self.page_4)
        self.addr_btn.setObjectName(u"addr_btn")
        self.addr_btn.setGeometry(QRect(20, 210, 181, 61))
        self.addr_btn.setFont(font)
        self.addr_btn.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E85F30;   /* Naranja m\u00e1s oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC532A;   /* M\u00e1s oscuro para click */\n"
"}")
        self.addr_btn.setIcon(icon)
        self.addr_btn.setIconSize(QSize(30, 30))
        self.layoutWidget = QWidget(self.page_4)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 181, 66))
        self.filtro_origen = QVBoxLayout(self.layoutWidget)
        self.filtro_origen.setObjectName(u"filtro_origen")
        self.filtro_origen.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setPointSize(14)
        self.label_4.setFont(font4)

        self.filtro_origen.addWidget(self.label_4)

        self.forigen_comboBox = QComboBox(self.layoutWidget)
        self.forigen_comboBox.addItem("")
        self.forigen_comboBox.addItem("")
        self.forigen_comboBox.addItem("")
        self.forigen_comboBox.addItem("")
        self.forigen_comboBox.addItem("")
        self.forigen_comboBox.addItem("")
        self.forigen_comboBox.addItem("")
        self.forigen_comboBox.setObjectName(u"forigen_comboBox")
        self.forigen_comboBox.setStyleSheet(u"\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 10px;\n"
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

        self.filtro_origen.addWidget(self.forigen_comboBox)

        self.layoutWidget_2 = QWidget(self.page_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 110, 181, 81))
        self.filtro_destino = QVBoxLayout(self.layoutWidget_2)
        self.filtro_destino.setObjectName(u"filtro_destino")
        self.filtro_destino.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.filtro_destino.addWidget(self.label_5)

        self.fdestino_comboBox = QComboBox(self.layoutWidget_2)
        self.fdestino_comboBox.addItem("")
        self.fdestino_comboBox.addItem("")
        self.fdestino_comboBox.addItem("")
        self.fdestino_comboBox.addItem("")
        self.fdestino_comboBox.addItem("")
        self.fdestino_comboBox.addItem("")
        self.fdestino_comboBox.addItem("")
        self.fdestino_comboBox.setObjectName(u"fdestino_comboBox")
        self.fdestino_comboBox.setStyleSheet(u"\n"
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

        self.filtro_destino.addWidget(self.fdestino_comboBox)

        self.editr_bbtn = QPushButton(self.page_4)
        self.editr_bbtn.setObjectName(u"editr_bbtn")
        self.editr_bbtn.setGeometry(QRect(20, 290, 181, 61))
        self.editr_bbtn.setFont(font)
        self.editr_bbtn.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E85F30;   /* Naranja m\u00e1s oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC532A;   /* M\u00e1s oscuro para click */\n"
"}")
        self.editr_bbtn.setIcon(icon)
        self.editr_bbtn.setIconSize(QSize(30, 30))
        self.side_stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.header_widget.raise_()
        self.main_stackedWidget.raise_()
        self.side_stackedWidget.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.main_stackedWidget.setCurrentIndex(0)
        self.side_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rutas_pushButton.setText(QCoreApplication.translate("MainWindow", u"Rutas", None))
        self.corridas_pushButton.setText(QCoreApplication.translate("MainWindow", u"Corridas", None))
        self.operadores_pushButton.setText(QCoreApplication.translate("MainWindow", u"Operadores", None))
        self.autobuses_pushButton.setText(QCoreApplication.translate("MainWindow", u"Autobuses", None))
        self.pasajeros_pushButton.setText(QCoreApplication.translate("MainWindow", u"Pasajeros", None))
        self.label_2.setText("")
        ___qtablewidgetitem = self.corridasm_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Corrida", None));
        ___qtablewidgetitem1 = self.corridasm_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem2 = self.corridasm_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Hora Salida", None));
        ___qtablewidgetitem3 = self.corridasm_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ruta", None));
        ___qtablewidgetitem4 = self.autobusm_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Autob\u00fas", None));
        ___qtablewidgetitem5 = self.autobusm_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Matricula", None));
        ___qtablewidgetitem6 = self.autobusm_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Marca/Modelo", None));
        ___qtablewidgetitem7 = self.autobusm_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem8 = self.pasajerosm_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Pasajero", None));
        ___qtablewidgetitem9 = self.pasajerosm_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nombre ", None));
        ___qtablewidgetitem10 = self.pasajerosm_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        ___qtablewidgetitem11 = self.pasajerosm_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"OPERADORES", None))
        ___qtablewidgetitem12 = self.o_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Num", None));
        ___qtablewidgetitem13 = self.o_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem14 = self.o_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Fecha de nacimiento", None));
        ___qtablewidgetitem15 = self.o_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None));
        ___qtablewidgetitem16 = self.o_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Fecha de contrato", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Rutas", None))
        ___qtablewidgetitem17 = self.rutas_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Num", None));
        ___qtablewidgetitem18 = self.rutas_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Origen", None));
        ___qtablewidgetitem19 = self.rutas_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
        ___qtablewidgetitem20 = self.rutas_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Distancia", None));
        self.label.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bienvenido", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TCN", None))
        self.addo_btn.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir operador", None))
        self.srch_line.setText("")
        self.srch_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar operador...", None))
        self.edito_btn.setText(QCoreApplication.translate("MainWindow", u"Editar operador", None))
        self.addr_btn.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir ruta", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Filtrar por origen", None))
        self.forigen_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.forigen_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tijuana", None))
        self.forigen_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Mexicali", None))
        self.forigen_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Ensenada", None))
        self.forigen_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"San Felipe", None))
        self.forigen_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Tecate", None))
        self.forigen_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"San Quintin", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Filtrar por destino", None))
        self.fdestino_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.fdestino_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tijuana", None))
        self.fdestino_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Mexicali", None))
        self.fdestino_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Ensenada", None))
        self.fdestino_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"San Felipe", None))
        self.fdestino_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Tecate", None))
        self.fdestino_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"San Quintin", None))

        self.editr_bbtn.setText(QCoreApplication.translate("MainWindow", u"Editar ruta", None))
    # retranslateUi

