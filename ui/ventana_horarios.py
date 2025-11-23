import sys
from datetime import date

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QSizePolicy, QScrollArea, QApplication, QMainWindow, QSpacerItem, QComboBox, QDateEdit
)
from PySide6.QtCore import Qt, QSize,  QDate
from PySide6.QtGui import QFont, QPixmap, QIcon # Necesario para QPixmap y QIcon si usas imágenes



class HorariosPage(QWidget):
    def __init__(self, app_manager):
        super().__init__()
        self.__app_manager = app_manager

        self.setObjectName("HorariosPage")
        self.setStyleSheet("background-color: #fff;") # Un gris muy claro para el fondo general

        # --- LAYOUT PRINCIPAL VERTICAL DE LA PÁGINA ---
        # Este layout contendrá todas las secciones (Cabecera, Datos, ScrollArea)
        main_v_layout = QVBoxLayout(self)
        main_v_layout.setContentsMargins(20, 20, 20, 20) # Márgenes alrededor de la página
        main_v_layout.setSpacing(20) # Espacio entre secciones principales

        # --- 1. SECCIÓN DE CABECERA (Regresar | HORARIOS | LOGO) ---
        header_h_layout = QHBoxLayout()
        header_h_layout.setSpacing(10)

        # Botón Regresar
        btn_regresar = QPushButton("Regresar")
        btn_regresar.setObjectName("btnRegresar")
        btn_regresar.setFixedSize(120, 40)
        btn_regresar.setStyleSheet("""
            #btnRegresar {
                background-color: #fff;
                border: 1px solid #c0c0c0;
                border-radius: 4px;
                font-size: 14px;
                padding: 5px;
                color: #555;
            }
            #btnRegresar:hover {
                background-color: #d0d0d0;
            }
        """)
        header_h_layout.addWidget(btn_regresar)
#        header_h_layout.addStretch(1) # Empuja el botón y título a los lados

        # Título "HORARIOS"
        lbl_horarios_title = QLabel("HORARIOS")
        lbl_horarios_title.setObjectName("lblHorariosTitle")
        font_horarios = QFont("Arial", 40, QFont.Bold) # Fuente más grande y negrita
        lbl_horarios_title.setFont(font_horarios)
        lbl_horarios_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_h_layout.addWidget(lbl_horarios_title)

        #header_h_layout.addStretch(1) # Empuja el título y logo a los lados

        # Placeholder para LOGO (puedes reemplazarlo con un QLabel con QPixmap)
        lbl_logo = QLabel()
        lbl_logo.setObjectName("lblLogo")
        pixmap = QPixmap("recursos/logo.png")   # PNG, JPG, SVG, lo que sea
        lbl_logo.setPixmap(pixmap)
        #lbl_logo.setFont(QFont("Arial", 20, QFont.Bold))
        lbl_logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        lbl_logo.setFixedSize(100, 40) # Tamaño fijo para el placeholder
        header_h_layout.addWidget(lbl_logo)
        
        header_h_layout.setStretch(0,1)
        header_h_layout.setStretch(1,4)
        header_h_layout.setStretch(2,1)

        main_v_layout.addLayout(header_h_layout)
        

        # --- 2. SECCIÓN DE DATOS DE BÚSQUEDA (Origen, Destino, Fecha) ---
        search_data_h_layout = QHBoxLayout()
        search_data_h_layout.setSpacing(30) # Espacio entre Origen, Destino, Fecha
        search_data_h_layout.setContentsMargins(10, 10, 10, 20) # Margen arriba y abajo

        font_data = QFont("Arial", 16)
        
        # Origen
        layout_origen_h = QHBoxLayout()

        lbl_origen = QLabel("Origen:")
        lbl_origen.setAlignment(Qt.AlignCenter)
        lbl_origen.setFont(font_data)
        layout_origen_h.addWidget(lbl_origen,1)
        #Creando combobox origen
        combobox_origen = QComboBox()
        combobox_origen.setObjectName('cbb_origen')

        for ciudad in self.__app_manager.ruta_controlador.consultarCiudadesOrigen():
            combobox_origen.addItem(ciudad[0])
        #combobox_origen.addItem('Tijuana')
        #combobox_origen.addItem('Mexicali')
        layout_origen_h.addWidget(combobox_origen,1)

        

        # Destino
        layout_destino_h = QHBoxLayout()

        lbl_destino = QLabel("Destino:")
        lbl_destino.setAlignment(Qt.AlignCenter)
        lbl_destino.setFont(font_data)
        layout_destino_h.addWidget(lbl_destino,1)
        #Creando combobox destino
        combobox_destino = QComboBox()
        combobox_destino.setObjectName('cbb_origen')
        for ciudad in self.__app_manager.ruta_controlador.consultarCiudadesDestino():
            combobox_destino.addItem(ciudad[0])
        #combobox_destino.addItem('Tijuana')
        #combobox_destino.addItem('Mexicali')
        layout_destino_h.addWidget(combobox_destino,1)

        
        # Fecha
        layout_fecha_h = QHBoxLayout()

        lbl_fecha = QLabel("Fecha:")
        lbl_fecha.setFont(font_data)
        lbl_fecha.setAlignment(Qt.AlignCenter)
        layout_fecha_h.addWidget(lbl_fecha,1)
        #Creando combobox destino
        fecha_edit = QDateEdit()
        fecha_edit.setDate(QDate(2025,2,24))
        fecha_edit.setDisplayFormat("dd/MM/yyyy")
        # No permitir fechas anteriores al 1 de enero de 2025
        fecha_edit.setMinimumDate(QDate.currentDate()) 

        # No permitir fechas posteriores al 31 de diciembre de 2027
        fecha_edit.setMaximumDate(QDate(2030, 1, 1))
        layout_fecha_h.addWidget(fecha_edit,1)

        #Dividiendo porciones 33% a cada uno
        search_data_h_layout.setStretch(0,1)
        search_data_h_layout.setStretch(1,1)
        search_data_h_layout.setStretch(2,1)

        #Anandiendo layout de los componenetes origen
        search_data_h_layout.addLayout(layout_origen_h)
        search_data_h_layout.addLayout(layout_destino_h)
        search_data_h_layout.addLayout(layout_fecha_h)

        main_v_layout.addLayout(search_data_h_layout)
        
        # --- 3. SECCIÓN DE HORARIOS DESLIZABLES (QScrollArea) ---
        
        # Contenedor para los items de horario (dentro del QScrollArea)
        self.horarios_container_widget = QWidget()
        self.horarios_v_layout = QVBoxLayout(self.horarios_container_widget)
        self.horarios_v_layout.setSpacing(20) # Espacio entre cada tarjeta de horario
        self.horarios_v_layout.setAlignment(Qt.AlignmentFlag.AlignTop) # Alinear tarjetas arriba

        # Añadir tarjetas de ejemplo
        for corrida in self.__app_manager.controlador_ventana_horarios.consultarCorridasDisponibles():
            self._add_horario_card(self.horarios_v_layout, "PLUS", "TIJ-MXL", "104", "9:00", "12:00", "$300.00")

        self.horarios_v_layout.addStretch(1) # Importante para que las tarjetas se agrupen arriba y el scroll funcione

        # QScrollArea que contendrá el widget de horarios
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True) # Hace que el widget interno se redimensione con el scrollArea
        scroll_area.setWidget(self.horarios_container_widget)
        #scroll_area.setStyleSheet("QScrollArea { border: none; }") # Sin borde para el scrollArea mismo
        scroll_area.setStyleSheet("""
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
        }
""")


        main_v_layout.addWidget(scroll_area)
        
        # --- Asegurar que la página ocupe todo el espacio ---
        # Este addStretch es para la página HorariosPage, no para el scrollArea
        main_v_layout.setStretch(0,1)
        main_v_layout.setStretch(1,1)
        main_v_layout.setStretch(2,1)




    def _add_horario_card(self, layout, tipo_servicio, ruta, bus_num, salida, llegada, precio):
        """
        Crea y añade una tarjeta de horario al layout dado.
        """
        card_frame = QFrame()
        card_frame.setFrameShape(QFrame.StyledPanel)
        card_frame.setFrameShadow(QFrame.Plain)
        card_frame.setObjectName("horarioCard")
        card_frame.setStyleSheet("""
            #horarioCard {
                background-color: white;
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                padding: 15px;
            }
        """)
        
        card_h_layout = QHBoxLayout(card_frame)
        card_h_layout.setSpacing(10)
        card_h_layout.setContentsMargins(15, 10, 15, 10) # Relleno interno de la tarjeta

        # Icono/Placeholder de Imagen (izquierda)
        img_placeholder = QLabel("🖼️") # Puedes reemplazarlo con un QLabel que muestre una QPixmap
        img_placeholder.setFont(QFont("Arial", 24))
        img_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        img_placeholder.setFixedSize(60, 60)
        img_placeholder.setStyleSheet("background-color: #e0e0e0; border-radius: 5px;")
        card_h_layout.addWidget(img_placeholder)

        # Detalles del Servicio y Ruta (izquierda-centro)
        service_details_v_layout = QVBoxLayout()
        lbl_tipo_servicio = QLabel(f"<b>{tipo_servicio}</b>")
        lbl_tipo_servicio.setFont(QFont("Arial", 12))
        
        lbl_ruta_bus = QLabel(f"{ruta}<br>🚌 {bus_num}")
        lbl_ruta_bus.setFont(QFont("Arial", 10))
        
        service_details_v_layout.addWidget(lbl_tipo_servicio)
        service_details_v_layout.addWidget(lbl_ruta_bus)
        service_details_v_layout.addStretch(1) # Empuja el texto hacia arriba
        card_h_layout.addLayout(service_details_v_layout)
        card_h_layout.addSpacing(20) # Espacio entre servicio y horarios

        # Horarios (Salida y Llegada)
        times_v_layout = QVBoxLayout()
        
        lbl_salida = QLabel(f"<b>Salida:</b> {salida}")
        lbl_salida.setFont(QFont("Arial", 12))
        
        lbl_llegada = QLabel(f"<b>Llegada:</b> {llegada}")
        lbl_llegada.setFont(QFont("Arial", 12))
        
        times_v_layout.addWidget(lbl_salida)
        times_v_layout.addWidget(lbl_llegada)
        times_v_layout.addStretch(1) # Empuja los textos hacia arriba
        card_h_layout.addLayout(times_v_layout)
        card_h_layout.addStretch(1) # Empuja horarios hacia la izquierda

        # Precio (derecha)
        price_v_layout = QVBoxLayout()
        
        price_frame = QFrame()
        price_frame.setObjectName("priceFrame")
        price_frame.setStyleSheet("""
            #priceFrame {
                background-color: #e0e0e0;
                border-radius: 5px;
                padding: 8px;
            }
        """)
        price_frame_layout = QVBoxLayout(price_frame)
        lbl_precio_title = QLabel("Precio:")
        lbl_precio_title.setFont(QFont("Arial", 10))
        lbl_precio_value = QLabel(f"<b>{precio}</b>")
        lbl_precio_value.setFont(QFont("Arial", 14, QFont.Bold))
        lbl_precio_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        price_frame_layout.addWidget(lbl_precio_title, alignment=Qt.AlignmentFlag.AlignHCenter)
        price_frame_layout.addWidget(lbl_precio_value)
        price_v_layout.addWidget(price_frame)
        price_v_layout.addStretch(1) # Empuja el precio hacia arriba
        card_h_layout.addLayout(price_v_layout)

        layout.addWidget(card_frame)


# --- CÓDIGO PARA PROBAR LA PÁGINA ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Crear una ventana principal (QMainWindow) para contener la página
    # como si fuera parte de un QStackedWidget
    main_window = QMainWindow()
    main_window.setWindowTitle("Diseño de Horarios con PySide6")
    main_window.resize(1000, 700) # Tamaño inicial de la ventana
    
    # Instanciar tu página de horarios
    horarios_page = HorariosPage()
    
    # Establecer la página de horarios como el widget central de la ventana principal
    main_window.setCentralWidget(horarios_page)
    
    main_window.show()
    sys.exit(app.exec())