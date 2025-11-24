import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QFrame, QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QHeaderView, QComboBox
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QColor, QIcon

class ReservationsDashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ReservationsDashboardPage")
        self.setStyleSheet("background-color: #f5f5f5;") # Fondo gris claro

        # --- LAYOUT PRINCIPAL VERTICAL ---
        main_v_layout = QVBoxLayout(self)
        main_v_layout.setContentsMargins(30, 30, 30, 30)
        main_v_layout.setSpacing(20)

        # -----------------------------------------------------------
        # 1. TARJETAS DE MÉTRICAS SUPERIORES
        # -----------------------------------------------------------
        metrics_h_layout = QHBoxLayout()
        metrics_h_layout.setSpacing(20)

        # Función auxiliar para crear tarjetas
        def create_metric_card(title, value, icon_color, icon_char, value_color=None):
            card = QFrame()
            card.setFixedSize(280, 100)
            card.setStyleSheet(f"""
                QFrame {{
                    background-color: white;
                    border: 1px solid #e0e0e0;
                    border-radius: 8px;
                }}
            """)
            card_layout = QHBoxLayout(card)

            # Contenido (Título y Valor)
            text_v_layout = QVBoxLayout()
            lbl_title = QLabel(title)
            lbl_title.setStyleSheet("color: #888; font-size: 14px;")
            
            lbl_value = QLabel(value)
            lbl_value.setFont(QFont("Arial", 24, QFont.Bold))
            if value_color:
                 lbl_value.setStyleSheet(f"color: {value_color};")

            text_v_layout.addWidget(lbl_title)
            text_v_layout.addWidget(lbl_value)
            
            # Icono (simulado con QLabel)
            lbl_icon = QLabel(icon_char)
            lbl_icon.setFont(QFont("Arial", 30))
            lbl_icon.setStyleSheet(f"color: {icon_color}; padding: 10px; background-color: #fff; border-radius: 5px;")
            lbl_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl_icon.setFixedSize(50, 50)


            card_layout.addLayout(text_v_layout, 1) # 1: para que ocupe más espacio
            card_layout.addWidget(lbl_icon)
            
            return card

        # Tarjeta 1: Total Reservaciones (Púrpura)
        metrics_h_layout.addWidget(create_metric_card("Total Reservaciones", "5", "#8E44AD", "🗑️"))

        # Tarjeta 2: Confirmadas (Verde)
        metrics_h_layout.addWidget(create_metric_card("Confirmadas", "3", "#2ECC71", "✅", value_color="#2ECC71"))

        # Tarjeta 3: Ingresos (Azul)
        metrics_h_layout.addWidget(create_metric_card("Ingresos (Confirmadas)", "$ 1.252.800", "#3498DB", "ℹ️", value_color="#3498DB"))

        main_v_layout.addLayout(metrics_h_layout)

        # -----------------------------------------------------------
        # 2. SECCIÓN DE TABLA (Reservaciones)
        # -----------------------------------------------------------
        table_container_frame = QFrame()
        table_container_frame.setStyleSheet("background-color: white; border-radius: 8px; padding: 15px;")
        table_container_layout = QVBoxLayout(table_container_frame)
        table_container_layout.setSpacing(15)

        # Título y Botón "Crear Reservación"
        table_header_h_layout = QHBoxLayout()
        lbl_reservaciones_title = QLabel("Reservaciones")
        lbl_reservaciones_title.setFont(QFont("Arial", 18, QFont.Bold))
        
        btn_crear = QPushButton("+ Crear Reservación")
        btn_crear.setFixedSize(160, 35)
        btn_crear.setStyleSheet("""
            QPushButton {
                background-color: #8E44AD;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #9B59B6;
            }
        """)
        table_header_h_layout.addWidget(lbl_reservaciones_title)
        table_header_h_layout.addStretch(1)
        table_header_h_layout.addWidget(btn_crear)
        table_container_layout.addLayout(table_header_h_layout)
        
        # --- Barra de Búsqueda y Filtros ---
        search_filter_h_layout = QHBoxLayout()
        
        # Búsqueda
        le_search = QLineEdit()
        le_search.setPlaceholderText("Buscar por número o corrida...")
        le_search.setMinimumWidth(500)
        le_search.setFixedSize(500, 35)
        le_search.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 5px; padding: 5px; }")
        
        # Dropdowns (Simulación)
        cbo_estados = QComboBox()
        cbo_estados.addItems(["Todos los estados", "Confirmada", "Pendiente", "Cancelada"])
        cbo_estados.setFixedSize(140, 35)
        
        btn_filtros = QPushButton("Más filtros")
        btn_filtros.setFixedSize(100, 35)
        
        search_filter_h_layout.addWidget(le_search)
        search_filter_h_layout.addStretch(1) # Espacio central
        search_filter_h_layout.addWidget(cbo_estados)
        search_filter_h_layout.addWidget(btn_filtros)
        table_container_layout.addLayout(search_filter_h_layout)
        
        # --- TABLA DE DATOS (QTableWidget) ---
        self.table_widget = self._create_reservations_table()
        table_container_layout.addWidget(self.table_widget)
        
        # Pie de Tabla (Paginación)
        footer_h_layout = QHBoxLayout()
        lbl_count = QLabel("Mostrando 5 de 5 reservaciones")
        btn_anterior = QPushButton("Anterior")
        btn_siguiente = QPushButton("Siguiente")
        btn_anterior.setFixedSize(80, 25)
        btn_siguiente.setFixedSize(80, 25)
        
        footer_h_layout.addWidget(lbl_count)
        footer_h_layout.addStretch(1)
        footer_h_layout.addWidget(btn_anterior)
        footer_h_layout.addWidget(btn_siguiente)
        table_container_layout.addLayout(footer_h_layout)
        
        # Añadir el contenedor de la tabla al layout principal
        main_v_layout.addWidget(table_container_frame)
        
        # Stretch final para que el QWidget ocupe todo el espacio vertical
        main_v_layout.addStretch(1)


    def _create_reservations_table(self):
        """Crea y popula el QTableWidget con datos de ejemplo."""
        table = QTableWidget(5, 7) # 5 filas, 7 columnas
        table.setEditTriggers(QTableWidget.NoEditTriggers) # No editable
        
        # 1. Definir encabezados
        headers = ["NÚMERO", "FECHA", "CORRIDA", "PASAJEROS", "TOTAL", "ESTADO", "ACCIONES"]
        table.setHorizontalHeaderLabels(headers)

        # 2. Ajustar encabezados para llenar el ancho
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents) # Columna de número fija
        table.horizontalHeader().setSectionResizeMode(6, QHeaderView.Fixed)
        table.setColumnWidth(6, 80)
        
        # 3. Datos de ejemplo
        data = [
            ["RES-2024-001", "24/11/2024", "Bogotá-Medellín", "4", "$ 556.800", "Confirmada", "---"],
            ["RES-2024-002", "25/11/2024", "Cali-Bogotá", "2", "$ 278.400", "Confirmada", "---"],
            ["RES-2024-003", "26/11/2024", "Medellín-Cali", "6", "$ 835.200", "Pendiente", "---"],
            ["RES-2024-004", "27/11/2024", "Bogotá-Cali", "3", "$ 417.600", "Confirmada", "---"],
            ["RES-2024-005", "28/11/2024", "Cartagena-Bogotá", "5", "$ 696.000", "Cancelada", "---"]
        ]

        # 4. Poblar la tabla
        for row, row_data in enumerate(data):
            for col, item in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(item))
                
                # Estilos para columnas específicas
                if col == 0: # NÚMERO (púrpura)
                    item = table.item(row, col)
                    item.setForeground(QColor("#8E44AD"))
                elif col == 4: # TOTAL (negrita)
                    item = table.item(row, col)
                    item.setFont(QFont("Arial", 10, QFont.Bold))
                elif col == 5: # ESTADO (con fondo de color)
                    self._set_status_cell_style(table, row, col, item)

        return table

    def _set_status_cell_style(self, table, row, col, text):
        """Aplica estilos de fondo y borde a la celda de estado."""
        status_text = text.lower()
        
        if "confirmada" in status_text:
            bg_color, text_color = "#E8F5E9", "#2ECC71" # Verde claro
        elif "pendiente" in status_text:
            bg_color, text_color = "#FFFDE7", "#F39C12" # Amarillo claro
        elif "cancelada" in status_text:
            bg_color, text_color = "#FBE9E7", "#E74C3C" # Rojo claro
        else:
            bg_color, text_color = "white", "black"

        status_label = QLabel(text)
        status_label.setStyleSheet(f"""
            QLabel {{
                background-color: {bg_color};
                color: {text_color};
                padding: 4px 8px;
                border-radius: 12px;
                font-size: 10px;
                font-weight: bold;
                margin: 5px;
            }}
        """)
        status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        table.setCellWidget(row, col, status_label)
        table.setRowHeight(row, 35) # Aumentar alto de fila para el estilo


# --- CÓDIGO PARA PROBAR EL DASHBOARD EN UNA VENTANA ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = QMainWindow()
    main_window.setWindowTitle("Dashboard de Reservaciones")
    main_window.resize(1300, 800)
    
    dashboard_page = ReservationsDashboardPage()
    
    # Establecer la página como el widget central (Expandible)
    main_window.setCentralWidget(dashboard_page)
    
    main_window.show()
    sys.exit(app.exec())
    '''

# requirements: PySide6
# Guarda esto como reservations_page.py y ejecútalo para ver la ventana de ejemplo.
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox,
    QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView,
    QFrame, QSpacerItem, QSizePolicy, QStackedWidget, QToolButton, QSpinBox
)
from PySide6.QtWidgets import QAbstractItemView
import sys
import os

IMAGE_PATH = "/mnt/data/Captura desde 2025-11-23 00-25-05.png"  # si quieres usar la captura

class SummaryCard(QFrame):
    def __init__(self, title: str, value: str, color="#ffffff", parent=None):
        super().__init__(parent)
        self.setObjectName("summaryCard")
        self.setStyleSheet("""
            QFrame#summaryCard{
                background: #ffffff;
                border-radius: 10px;
                padding: 12px;
            }
        """)
        layout = QVBoxLayout(self)
        label_title = QLabel(title)
        label_title.setStyleSheet("color: #6b7280;")  # gris suave
        label_value = QLabel(value)
        label_value.setFont(QFont("", 20, QFont.Bold))
        layout.addWidget(label_title)
        layout.addWidget(label_value)
        layout.addStretch()

class StatusBadge(QLabel):
    def __init__(self, text, bg="#eef2ff", color="#0f172a", parent=None):
        super().__init__(text, parent)
        self.setContentsMargins(8, 3, 8, 3)
        self.setStyleSheet(f"""
            QLabel{{
                background-color: {bg};
                color: {color};
                border-radius: 10px;
                font-weight: 600;
            }}
        """)

class ReservationsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(16, 16, 16, 16)

        # Top summary cards
        top_row = QHBoxLayout()
        top_row.setSpacing(12)
        top_row.addWidget(SummaryCard("Total Reservaciones", "5"))
        top_row.addWidget(SummaryCard("Confirmadas", "3"))
        top_row.addWidget(SummaryCard("Ingresos (Confirmadas)", "$ 1.252.800"))
        top_row.addStretch()
        # si existe imagen: mostrarla en la esquina superior derecha (opcional)
        if os.path.exists(IMAGE_PATH):
            pix = QPixmap(IMAGE_PATH).scaledToHeight(80, Qt.SmoothTransformation)
            img_label = QLabel()
            img_label.setPixmap(pix)
            top_row.addWidget(img_label, alignment=Qt.AlignRight | Qt.AlignVCenter)
        main_layout.addLayout(top_row)

        # Search + actions row
        controls_frame = QFrame()
        controls_layout = QHBoxLayout(controls_frame)
        controls_layout.setSpacing(8)

        # left: título y buscador
        left_controls = QVBoxLayout()
        title = QLabel("Reservaciones")
        title.setFont(QFont("", 14, QFont.Bold))
        left_controls.addWidget(title)

        search_row = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar por número o corrida...")
        search_row.addWidget(self.search_input)
        left_controls.addLayout(search_row)
        controls_layout.addLayout(left_controls, stretch=3)

        # right: filtros y botón crear
        right_controls = QHBoxLayout()
        self.state_combo = QComboBox()
        self.state_combo.addItems(["Todos los estados", "Confirmada", "Pendiente", "Cancelada"])
        right_controls.addWidget(self.state_combo)

        more_filters_btn = QToolButton()
        more_filters_btn.setText("Más filtros")
        right_controls.addWidget(more_filters_btn)

        create_btn = QPushButton("+  Crear Reservación")
        create_btn.setStyleSheet("background-color:#7c3aed;color:white;padding:8px;border-radius:6px;")
        right_controls.addWidget(create_btn)

        controls_layout.addLayout(right_controls, stretch=2)
        main_layout.addWidget(controls_frame)

        # Table
        self.table = QTableWidget(0, 7)
        headers = ["NÚMERO", "FECHA", "CORRIDA", "PASAJEROS", "TOTAL", "ESTADO", "ACCIONES"]
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)
        self.table.setStyleSheet("""
            QTableWidget { background: white; }
            QHeaderView::section { background: #f3f4f6; padding: 8px; border: none; }
        """)
        main_layout.addWidget(self.table, stretch=1)

        # Pagination row (simple)
        pagination_row = QHBoxLayout()
        pagination_row.addStretch()
        self.prev_btn = QPushButton("Anterior")
        self.next_btn = QPushButton("Siguiente")
        pagination_row.addWidget(self.prev_btn)
        pagination_row.addWidget(self.next_btn)
        main_layout.addLayout(pagination_row)

        # Populate sample data
        self.load_sample_data()

        # conexiones sencillas
        self.search_input.textChanged.connect(self.filter_rows)
        self.state_combo.currentTextChanged.connect(self.filter_rows)
        self.prev_btn.clicked.connect(lambda: print("Prev page"))
        self.next_btn.clicked.connect(lambda: print("Next page"))

    def add_row(self, numero, fecha, corrida, pasajeros, total, estado):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(numero))
        self.table.setItem(row, 1, QTableWidgetItem(fecha))
        self.table.setItem(row, 2, QTableWidgetItem(corrida))
        self.table.setItem(row, 3, QTableWidgetItem(str(pasajeros)))
        self.table.setItem(row, 4, QTableWidgetItem(total))

        # badge como widget en la celda
        if estado == "Confirmada":
            badge = StatusBadge(estado, bg="#dcfce7", color="#166534")
        elif estado == "Pendiente":
            badge = StatusBadge(estado, bg="#fef3c7", color="#92400e")
        else:
            badge = StatusBadge(estado, bg="#fee2e2", color="#991b1b")
        self.table.setCellWidget(row, 5, badge)

        # acciones (botón)
        btn = QPushButton("...")
        btn.setMaximumWidth(40)
        self.table.setCellWidget(row, 6, btn)

    def load_sample_data(self):
        # datos sacados de tu captura (cinco filas)
        sample = [
            ("RES-2024-001", "24/11/2024", "Bogotá-Medellín", 4, "$ 556.800", "Confirmada"),
            ("RES-2024-002", "25/11/2024", "Cali-Bogotá", 2, "$ 278.400", "Confirmada"),
            ("RES-2024-003", "26/11/2024", "Medellín-Cali", 6, "$ 835.200", "Pendiente"),
            ("RES-2024-004", "27/11/2024", "Bogotá-Cali", 3, "$ 417.600", "Confirmada"),
            ("RES-2024-005", "28/11/2024", "Cartagena-Bogotá", 5, "$ 696.000", "Cancelada"),
        ]
        for r in sample:
            self.add_row(*r)

    def filter_rows(self):
        text = self.search_input.text().lower()
        estado_filter = self.state_combo.currentText()
        for r in range(self.table.rowCount()):
            numero_item = self.table.item(r, 0)
            corrida_item = self.table.item(r, 2)
            # si alguno coincide con el texto y estado coincide
            matches_text = (text in numero_item.text().lower()) or (text in corrida_item.text().lower()) or text == ""
            if estado_filter == "Todos los estados":
                matches_state = True
            else:
                # obtener texto del badge
                widget = self.table.cellWidget(r, 5)
                matches_state = (widget.text() == estado_filter)
            self.table.setRowHidden(r, not (matches_text and matches_state))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Ejemplo: agregar la página a un QStackedWidget
    stacked = QStackedWidget()
    reservations_page = ReservationsPage()
    stacked.addWidget(reservations_page)
    stacked.setFixedSize(1100, 680)
    stacked.show()

    sys.exit(app.exec())
'''