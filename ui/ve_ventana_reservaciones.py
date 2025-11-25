# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 've_ventana_reservaciones.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget,QTableWidget,QTableWidgetItem,QVBoxLayout,QHBoxLayout)
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableView, QHeaderView
)
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QColor, QFont, QBrush

from objetos.reservacion import Reservacion
# ...

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1920, 1080))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setStyleSheet(u"background-color: #eee\n"
";")
        self.widget_central = QWidget(MainWindow)
        self.widget_central.setObjectName(u"widget_central")
        self.stacked_principal = QStackedWidget(self.widget_central)
        self.stacked_principal.setObjectName(u"stacked_principal")
        self.stacked_principal.setGeometry(QRect(0, 170, 1931, 909))
        self.stacked_principal.setStyleSheet(u"background-color: #F7F7F7;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget_totoal_reservacion1 = QWidget(self.page)
        self.widget_totoal_reservacion1.setObjectName(u"widget_totoal_reservacion1")
        self.widget_totoal_reservacion1.setGeometry(QRect(20, 20, 571, 131))
        self.widget_totoal_reservacion1.setStyleSheet(u"QWidget {\n"
"   background: #fff;\n"
"   border-radius: 10px;\n"
"    border: 1px solid #eee;\n"
"}\n"
"QWidget:hover {\n"
"   border: 1px solid #aaa;\n"
"}")
        self.label = QLabel(self.widget_totoal_reservacion1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 171, 19))
        font = QFont()
        font.setWeight(QFont.DemiBold)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: None; font-size: 17px; color: #444")
        self.label_total_reservaciones = QLabel(self.widget_totoal_reservacion1)
        self.label_total_reservaciones.setObjectName(u"label_total_reservaciones")
        self.label_total_reservaciones.setGeometry(QRect(40, 60, 80, 41))
        self.label_total_reservaciones.setFont(font)
        self.label_total_reservaciones.setStyleSheet(u"border: None; font-size: 35px; color: #000")
        self.label_3 = QLabel(self.widget_totoal_reservacion1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 30, 61, 61))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background: #FADABD;border: None; font-size: 35px; color: #000; padding: 15px 16px")
        self.label_3.setPixmap(QPixmap(u"recursos/icono_carpeta.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setMargin(0)
        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(630, 20, 621, 131))
        self.widget_2.setStyleSheet(u"QWidget {\n"
"   background: #fff;\n"
"   border-radius: 10px;\n"
"    border: 1px solid #eee;\n"
"}\n"
"QWidget:hover {\n"
"   border: 1px solid #aaa;\n"
"}")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 30, 300, 19))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"border: None; font-size: 17px; color: #444")
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 60, 70, 41))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"border: None; font-size: 35px; color: #000")
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(490, 30, 61, 61))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background: #FADABD;border: None; font-size: 35px; color: #000; padding: 15px 16px")
        self.label_12.setPixmap(QPixmap(u"recursos/icono_carpeta.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12.setMargin(0)
        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1290, 20, 611, 131))
        self.widget_3.setStyleSheet(u"QWidget {\n"
"   background: #fff;\n"
"   border-radius: 10px;\n"
"    border: 1px solid #eee;\n"
"}\n"
"QWidget:hover {\n"
"   border: 1px solid #aaa;\n"
"}")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 30, 300, 19))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"border: None; font-size: 17px; color: #444")
        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 60, 70, 41))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"border: None; font-size: 35px; color: #000")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(500, 30, 61, 61))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"background: #FADABD;border: None; font-size: 35px; color: #000; padding: 15px 16px")
        self.label_15.setPixmap(QPixmap(u"recursos/icono_carpeta.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15.setMargin(0)
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 170, 1880, 869))
        self.widget_4.setStyleSheet(u"QWidget {\n"
"   background: #fff;\n"
"   border-radius: 10px;\n"
"    border: 1px solid #eee;\n"
"}\n"
"")
        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 30, 181, 41))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"border: None; font-size: 25px; color: #000")
        self.comboBox_filtros = QComboBox(self.widget_4)
        self.comboBox_filtros.setObjectName(u"comboBox_filtros")
        self.comboBox_filtros.setGeometry(QRect(1370, 90, 281, 41))
        self.comboBox_filtros.addItem('Reservaciones Activas')
        self.comboBox_filtros.addItem('Reservaciones Pasadas')
        self.comboBox_filtros.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 12px;\n"
"    padding: 6px 32px 6px 12px;  \n"
"    font-size: 15px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #F6C392;\n"
"}\n"
"\n"
"/* Quitar el borde del drop-down */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 24px;\n"
"}\n"
"\n"
"/* Flecha tipo iOS / Web moderna */\n"
"QComboBox::down-arrow {\n"
"    image: url(\"recursos/arrow_drop_down.svg\");\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"")
        self.boton_mas_filtros = QPushButton(self.widget_4)
        self.boton_mas_filtros.setObjectName(u"boton_mas_filtros")
        self.boton_mas_filtros.setGeometry(QRect(1670, 90, 151, 41))
        font1 = QFont()
        font1.setBold(True)
        self.boton_mas_filtros.setFont(font1)
        self.boton_mas_filtros.setStyleSheet(u"QPushButton{\n"
"   background: #1061C4;\n"
"   color:WHITE;\n"
"   border:none;\n"
"   border-radius: 8px;\n"
"   font-weight: bold;\n"
"   font-size: 15px;\n"
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
        icon.addFile(u"recursos/icono_filtro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_mas_filtros.setIcon(icon)
        self.boton_mas_filtros.setIconSize(QSize(18, 18))
        
        # =========================================================================
        # INICIO: CÓDIGO MODIFICADO PARA LA BARRA DE BÚSQUEDA Y BOTÓN
        # =========================================================================

        # 1. Contenedor (QWidget) que reemplaza la geometría del LineEdit
        self.widget_contenedor_busqueda = QWidget(self.widget_4)
        # Usa la geometría original del line_edit_buscar_corrida
        self.widget_contenedor_busqueda.setGeometry(QRect(40, 90, 1311, 41))
        self.widget_contenedor_busqueda.setObjectName(u"widget_contenedor_busqueda")
        
        # 2. Layout Horizontal (QHBoxLayout) dentro del contenedor
        self.layout_busqueda = QHBoxLayout(self.widget_contenedor_busqueda)
        self.layout_busqueda.setSpacing(0)
        self.layout_busqueda.setContentsMargins(0, 0, 0, 0)
        
        # 3. QLineEdit de Búsqueda
        self.line_edit_buscar_corrida = QLineEdit(self.widget_contenedor_busqueda)
        self.line_edit_buscar_corrida.setObjectName(u"line_edit_buscar_corrida")
        self.line_edit_buscar_corrida.setMaxLength(100)
        self.line_edit_buscar_corrida.setStyleSheet(u"""
QLineEdit {
    padding-left:10px;
    border-top-left-radius: 8px;
    border-bottom-left-radius: 8px;
    border-top: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    border-left: 1px solid #ccc;
    border-right: none; /* Quitamos el borde derecho */
    height: 39px; /* Asegura la altura si el layout no lo hace por completo */
}
QLineEdit:hover {
    border: 1px solid #F6C392;
    border-right: none;
}
""")
        # 4. QPushButton de Búsqueda
        self.boton_buscar_corrida = QPushButton(self.widget_contenedor_busqueda)
        self.boton_buscar_corrida.setObjectName(u"boton_buscar_corrida")
        # El ancho es igual al alto para que sea cuadrado (41px para que coincida con la altura)
        self.boton_buscar_corrida.setFixedSize(QSize(41, 41)) 
        
        icon_search = QIcon()
        # Nota: Asegúrate de tener la imagen 'recursos/icono_search.png' disponible.
        icon_search.addFile(u"recursos/icono_buscar_reservacion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off) 
        self.boton_buscar_corrida.setIcon(icon_search)
        self.boton_buscar_corrida.setIconSize(QSize(20, 20))
        
        self.boton_buscar_corrida.setStyleSheet(u"""
QPushButton {
    background: #1061C4;
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
    color: WHITE;
    font-weight: bold;
    border: 1px solid #1061C4; /* Borde del mismo color */
}
QPushButton:hover {
    background-color: #0D4FAB;
}
QPushButton:pressed {
    background-color: #0A3F8A;
}
""")
        
        # 5. Añadir los Widgets al Layout
        self.layout_busqueda.addWidget(self.line_edit_buscar_corrida) 
        self.layout_busqueda.addWidget(self.boton_buscar_corrida) 
        
        # =========================================================================
        # FIN: CÓDIGO MODIFICADO
        # =========================================================================
        
        self.line = QFrame(self.widget_4)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-10, 160, 1920, 1))
        self.line.setStyleSheet(u"background:#eee;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.boton_crear_reservacion = QPushButton(self.widget_4)
        self.boton_crear_reservacion.setObjectName(u"boton_crear_reservacion")
        self.boton_crear_reservacion.setGeometry(QRect(1590, 30, 231, 41))
        self.boton_crear_reservacion.setFont(font1)
        self.boton_crear_reservacion.setStyleSheet(u"QPushButton{\n"
"   background: #EE8C30;\n"
"   color:WHITE;\n"
"   border:none;\n"
"   border-radius: 8px;\n"
"   font-weight: bold;\n"
"   font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C16610;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #6D3909;     \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"recursos/icono_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_crear_reservacion.setIcon(icon1)
        self.boton_crear_reservacion.setIconSize(QSize(18, 18))
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 180, 1880, 61))
        self.widget_5.setStyleSheet(u"background:#FADABD;border-radius:0;")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 91, 19))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_18 = QLabel(self.widget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(200, 20, 91, 19))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_19 = QLabel(self.widget_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(1260, 20, 121, 19))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(370, 20, 91, 19))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_cliente = QLabel(self.widget_5)
        self.label_cliente.setText('CLIENTE')
        self.label_cliente.setObjectName(u'label_cliente')
        self.label_cliente.setGeometry(QRect(1100,20,91,19))
        self.label_cliente.setFont(font)
        self.label_cliente.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_cliente.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_26 = QLabel(self.widget_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(930, 20, 91, 19))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_27 = QLabel(self.widget_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(1440, 20, 91, 19))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_28 = QLabel(self.widget_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(560, 20, 91, 19))
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_29 = QLabel(self.widget_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(740, 20, 91, 19))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_30 = QLabel(self.widget_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(1740, 20, 91, 19))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"border: None; font-size: 14px; color: #444")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollArea_reservaciones = QScrollArea(self.widget_4)
        self.scrollArea_reservaciones.setObjectName(u"scrollArea_reservaciones")
        self.scrollArea_reservaciones.setGeometry(QRect(0, 240, 1881, 481))
        self.scrollArea_reservaciones.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1879, 479))
        self.scrollAreaWidgetContents.setStyleSheet('background:#fff')
        self.scrollAreaWidgetContents.setContentsMargins(0,0,0,0)
        self.scrollArea_reservaciones.setWidget(self.scrollAreaWidgetContents)
        # --- SECCIÓN DE RESERVACIONES DESLIZABLES usando(QScrollArea) --- #
        # Contenedor para los items de horario (dentro del QScrollArea)
        self.reservaciones_v_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.reservaciones_v_layout.setSpacing(0) # Espacio entre cada tarjeta de horario
        self.reservaciones_v_layout.setAlignment(Qt.AlignmentFlag.AlignTop) # Alinear tarjetas arriba
        self.reservaciones_v_layout.addStretch(1) # Importante para que las tarjetas se agrupen arriba y el scroll funcione
        self.reservaciones_v_layout.setContentsMargins(0, 0, 0, 0) # Quitar márgenes internos
        self.scrollArea_reservaciones.setStyleSheet("""
        QScrollArea {
            border:none;
                    }
        QScrollBar:vertical {
            background: #eee;
            width: 12px;
            margin: 0;
            border-radius: 6px;
        }

        QScrollBar::handle:vertical {
            background: #777;
            min-height: 20px;
            border-radius: 6px;
        }

        QScrollBar::handle:vertical:hover {
            background: #EB8C07;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            height: 0;
        }""")

        self.stacked_principal.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stacked_principal.addWidget(self.page_2)
        self.widget_header = QWidget(self.widget_central)
        self.widget_header.setObjectName(u"widget_header")
        self.widget_header.setGeometry(QRect(0, 0, 1920, 171))
        self.widget_header.setStyleSheet(u"background:#fff")
        self.rutas_pushButton = QPushButton(self.widget_header)
        self.rutas_pushButton.setObjectName(u"rutas_pushButton")
        self.rutas_pushButton.setGeometry(QRect(30, 90, 161, 51))
        self.rutas_pushButton.setFont(font1)
        self.rutas_pushButton.setStyleSheet(u"QPushButton{\n"
"   background: #1061C4;\n"
"   color:WHITE;\n"
"   border:none;\n"
"   border-radius: 8px;\n"
"   font-weight: bold;\n"
"   font-size:25px;\n"
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
        icon2.addFile(u":/recursos/Icons/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rutas_pushButton.setIcon(icon2)
        self.rutas_pushButton.setIconSize(QSize(30, 30))
        self.label_icono = QLabel(self.widget_header)
        self.label_icono.setObjectName(u"label_icono")
        self.label_icono.setGeometry(QRect(40, 20, 141, 41))
        self.label_icono.setPixmap(QPixmap(u"recursos/logo_tcn.jpeg"))
        self.label_icono.setScaledContents(True)
        self.label_seccion = QLabel(self.widget_header)
        self.label_seccion.setObjectName(u"label_seccion")
        self.label_seccion.setGeometry(QRect(200, 20, 511, 41))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setWeight(QFont.DemiBold)
        self.label_seccion.setFont(font2)
        self.label_seccion.setStyleSheet(u"background: #fff")
        self.corridas_pushButton = QPushButton(self.widget_header)
        self.corridas_pushButton.setObjectName(u"corridas_pushButton")
        self.corridas_pushButton.setGeometry(QRect(220, 90, 171, 51))
        self.corridas_pushButton.setFont(font1)
        self.corridas_pushButton.setStyleSheet(u"QPushButton{\n"
"   background: #1061C4;\n"
"   color:WHITE;\n"
"   border:none;\n"
"   border-radius: 8px;\n"
"   font-weight: bold;\n"
"   font-size: 25px;\n"
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
        icon3.addFile(u":/recursos/Icons/calendario(1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.corridas_pushButton.setIcon(icon3)
        self.corridas_pushButton.setIconSize(QSize(30, 30))
        self.operadores_pushButton = QPushButton(self.widget_header)
        self.operadores_pushButton.setObjectName(u"operadores_pushButton")
        self.operadores_pushButton.setGeometry(QRect(420, 90, 181, 51))
        self.operadores_pushButton.setFont(font1)
        self.operadores_pushButton.setStyleSheet(u"QPushButton{\n"
"   background: #1061C4;\n"
"   color:WHITE;\n"
"   border:none;\n"
"   border-radius: 8px;\n"
"   font-weight: bold;\n"
"   font-size: 25px;\n"
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
        icon4.addFile(u":/recursos/Icons/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operadores_pushButton.setIcon(icon4)
        self.operadores_pushButton.setIconSize(QSize(25, 25))
        self.autobuses_pushButton = QPushButton(self.widget_header)
        self.autobuses_pushButton.setObjectName(u"autobuses_pushButton")
        self.autobuses_pushButton.setGeometry(QRect(630, 90, 181, 51))
        self.autobuses_pushButton.setFont(font1)
        self.autobuses_pushButton.setStyleSheet(u"QPushButton{\n"
"   background: #1061C4;\n"
"   color:WHITE;\n"
"   border:none;\n"
"   border-radius: 8px;\n"
"   font-weight: bold;\n"
"   font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/recursos/Icons/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.autobuses_pushButton.setIcon(icon5)
        self.autobuses_pushButton.setIconSize(QSize(30, 30))
        self.pasajeros_pushButton = QPushButton(self.widget_header)
        self.pasajeros_pushButton.setObjectName(u"pasajeros_pushButton")
        self.pasajeros_pushButton.setGeometry(QRect(840, 90, 181, 51))
        self.pasajeros_pushButton.setFont(font1)
        self.pasajeros_pushButton.setStyleSheet(u"QPushButton{\n"
"   background: #1061C4;\n"
"   color:WHITE;\n"
"   border:none;\n"
"   border-radius: 8px;\n"
"   font-weight: bold;\n"
"   font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/recursos/Icons/pasajero.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pasajeros_pushButton.setIcon(icon6)
        self.pasajeros_pushButton.setIconSize(QSize(30, 30))
        self.reservaciones_pushButton = QPushButton(self.widget_header)
        self.reservaciones_pushButton.setObjectName(u"reservaciones_pushButton")
        self.reservaciones_pushButton.setGeometry(QRect(1050, 90, 251, 51))
        self.reservaciones_pushButton.setFont(font1)
        self.reservaciones_pushButton.setStyleSheet(u"QPushButton{\n"
"   background: #1061C4;\n"
"   color:WHITE;\n"
"   border:none;\n"
"   border-radius: 8px;\n"
"   font-weight: bold;\n"
"   font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"recursos/icono_reservaciones.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reservaciones_pushButton.setIcon(icon7)
        self.reservaciones_pushButton.setIconSize(QSize(30, 30))
        self.pushButton = QPushButton(self.widget_header)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1830, 10, 51, 51))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"background: #fff; border-radius: 15%;\n"
"padding: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #eee;    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"recursos/icono_cuenta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(40, 40))
        MainWindow.setCentralWidget(self.widget_central)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stacked_principal.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)



    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total Reservaciones", None))
        self.label_total_reservaciones.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_3.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Total Reservaciones", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Total Reservaciones", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Reservaciones", None))
        self.comboBox_filtros.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Todos los estados", None))
        self.boton_mas_filtros.setText(QCoreApplication.translate("MainWindow", u"Mas filtros", None))
        
        # INICIO: Traducción del LineEdit y el nuevo Botón
        self.line_edit_buscar_corrida.setInputMask("")
        self.line_edit_buscar_corrida.setText("")
        self.line_edit_buscar_corrida.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Burcar por numero o corrida...", None))
        self.boton_buscar_corrida.setText(QCoreApplication.translate("MainWindow", u"", None))
        # FIN: Traducción del LineEdit y el nuevo Botón
        
        self.boton_crear_reservacion.setText(QCoreApplication.translate("MainWindow", u" Crear Reservaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"FECHA", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"LIMITE DE PAGO", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"CORRIDA", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"PASAJEROS", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ORIGEN", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"DESTINO", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"ACCIONES", None))
        self.rutas_pushButton.setText(QCoreApplication.translate("MainWindow", u"Rutas", None))
        self.label_icono.setText("")
        self.label_seccion.setText(QCoreApplication.translate("MainWindow", u"Sistema de Reservaciones", None))
        self.corridas_pushButton.setText(QCoreApplication.translate("MainWindow", u"Corridas", None))
        self.operadores_pushButton.setText(QCoreApplication.translate("MainWindow", u"Operadores", None))
        self.autobuses_pushButton.setText(QCoreApplication.translate("MainWindow", u"Autobuses", None))
        self.pasajeros_pushButton.setText(QCoreApplication.translate("MainWindow", u"Pasajeros", None))
        self.reservaciones_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reservaciones", None))
        self.pushButton.setText("")
        # retranslateUi




from PySide6.QtWidgets import (
    QFrame, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QScrollArea, QApplication
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont

class TarjetaReservacion(QFrame):
    def __init__(self, datos_registro):
        super().__init__()
        
        # 1. Estilización del QFrame (la tarjeta)
        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Raised)
        self.setLineWidth(1)
        self.setFixedHeight(40) # Altura fija para la tarjeta
        self.setStyleSheet("""
            TarjetaReservacion { 
                border: 1px solid #ddd; 
                border-radius: 0px; 
                margin: 0;
                padding: 0 30px;
                background-color: white;
            }
                           
            TarjetaReservacion:hover { 
                margin: 0;
                background-color: #E7F1FD;
            }
        """)

        # 2. Layout Horizontal (Simula 10 columnas)
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignLeft | Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(10, 0, 10, 0) # Margen horizontal
        layout.setSpacing(5) # Espacio reducido entre "columnas"

        # Definición de anchos y datos para 9 Labels
        # Los anchos son en pixeles. Esto fuerza la "columna" a tener ese tamaño.
        column_specs = [175,160,185,173,175,180,200,195,120]

        # 3. Crear y añadir los 9 QLabels (Columnas 1 a 9)
        contador = 0
        for i in column_specs:    
            valor = datos_registro[contador]
            lbl = QLabel(str(valor))
            contador+=1                    
            lbl.setMinimumWidth(i)
            lbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            lbl.setStyleSheet("""
            QLabel { 
                border: None;
                background: transparent;
            }
        """)
            layout.addWidget(lbl)
        contador = 0
        contador2 = 0

        # Añadir un Stretch intermedio (opcional) para empujar el botón más a la derecha
        layout.addStretch(1) 

        # 4. Crear y añadir el QPushButton (Columna 10)
        btn_acciones = QPushButton() 
        btn_acciones.setFixedSize(QSize(30, 30)) # Botón pequeño y cuadrado
        btn_acciones.setIcon(QIcon("recursos/icono_acciones.png"))
        btn_acciones.setIconSize(QSize(24, 24))  # opcional

        btn_acciones.setCursor(QCursor(Qt.PointingHandCursor))
        btn_acciones.setStyleSheet("""
            QPushButton {
                border-radius: 8px; 
                border:None;
                background: transparent;
            }
            QPushButton:hover {
            }
            QPushButton:pressed {
                background: #68A6F3;

            }
        """)
        
        # Columna 10
        layout.addWidget(btn_acciones)




from ui.dialog_mensaje import DialogoMensajePersonalizado

# --- CLASE QUE HEREDA ESTA VENTANA PARA MAS FACIL MANIPULACION -- #
class VentanaReservaciones(QMainWindow, Ui_MainWindow):
    def __init__(self, AppManager):
        super().__init__()

        self.setupUi(self)
        self.controlador_ve_reservaciones = AppManager.controlador_ve_reservaciones


        self.label_10.setText('Reservaciones Activas')
        self.label_11.setText('158')
        self.label_13.setText('Reservaciones Pasadas')
        self.label_14.setText('20')
        self.label_total_reservaciones.setText(str(self.controlador_ve_reservaciones.getTotalReservaciones()))

        self.cargar_registros()
        #agragando evento a boton buscar
        self.boton_buscar_corrida.clicked.connect(self.buscar_corrida)


    def cargar_registros(self):
        #self.controlador_ve_reservaciones)

        while self.reservaciones_v_layout.count() > 0:
            item = self.reservaciones_v_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            elif item.spacerItem() is not None:
                # Si encontramos el stretch, lo volvemos a añadir al final
                pass    

        for reservacion in self.controlador_ve_reservaciones.consultarTodasReservacionesParaTabla():
            datos_reservacion = [reservacion[0],reservacion[1],reservacion[2],reservacion[3],
                                reservacion[4],reservacion[5],reservacion[6],reservacion[7]
                                ,reservacion[8]]
            tarjeta = TarjetaReservacion(datos_reservacion)
            self.reservaciones_v_layout.addWidget(tarjeta)  
        
        # El stretch (espaciador) es necesario para que las tarjetas se agrupen en la parte superior.
        self.reservaciones_v_layout.addStretch(1)


    def cargar_registros_despues(self,datos):
        #self.controlador_ve_reservaciones)

        while self.reservaciones_v_layout.count() > 0:
            item = self.reservaciones_v_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            elif item.spacerItem() is not None:
                # Si encontramos el stretch, lo volvemos a añadir al final
                pass    

        for reservacion in datos:
            datos_reservacion = [reservacion[0],reservacion[1],reservacion[2],reservacion[3],
                                reservacion[4],reservacion[5],reservacion[6],reservacion[7]
                                ,reservacion[8]]
            tarjeta = TarjetaReservacion(datos_reservacion)
            self.reservaciones_v_layout.addWidget(tarjeta)  
        
        # El stretch (espaciador) es necesario para que las tarjetas se agrupen en la parte superior.
        self.reservaciones_v_layout.addStretch(1)

        """ Este metodo muestra un mesaje personalizado """
    def mostrar_mensaje_tcn(self,mensaje, tipo="info", parent=None):
        dialogo = DialogoMensajePersonalizado(mensaje, tipo, parent)
        dialogo.exec()
        

    def buscar_corrida(self):
        #si el usuario ingresa '' es por que quiere de vuelta todos las reservaciones
        if self.line_edit_buscar_corrida.text() == '':
            respuesta = self.controlador_ve_reservaciones.consultarTodasReservacionesParaTabla()
            self.cargar_registros_despues(respuesta)
            return
        
        #checar si el numero fue validado correctamente

        respuesta = self.controlador_ve_reservaciones.buscarReservacionPorNumero(self.line_edit_buscar_corrida.text())
        if respuesta == False:
            self.mostrar_mensaje_tcn('Solo se permiten numeros.',tipo="error",parent=self)
            return
        self.cargar_registros_despues(respuesta)

    


