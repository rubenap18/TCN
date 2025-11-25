import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon, QPixmap

# =========================================================================
# COLORES UTILIZADOS EN TU CÓDIGO ANTERIOR
# =========================================================================
COLOR_EXITO_PRIMARIO = "#1061C4" # Azul del botón de filtros
COLOR_ERROR_SECUNDARIO = "#EE8C30" # Naranja del botón de crear reservación
COLOR_FONDO = "#FFFFFF" 
COLOR_TEXTO = "#000000"

class DialogoMensajePersonalizado(QDialog):
    """
    Diálogo personalizado para mostrar mensajes de información, éxito o error,
    manteniendo la estética de la aplicación (TCN).
    """
    def __init__(self, mensaje, tipo="info", parent=None):
        super().__init__(parent)
        
        # 1. Configuración de la Ventana
        self.setWindowTitle("Mensaje - TCN")
        self.setFixedSize(400, 200) 
        self.setStyleSheet(f"QDialog {{ background-color: {COLOR_FONDO}; border-radius: 10px; }}")
        
        # Ocultar el botón de cerrar [X] de la ventana
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint | Qt.WindowStaysOnTopHint) 

        # 2. Layout Principal (Vertical)
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        
        # 3. Widget Contenedor de Ícono y Título (para alineación)
        widget_header = QWidget()
        layout_header = QHBoxLayout(widget_header)
        layout_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_header.setContentsMargins(0, 0, 0, 10)
        
        # 4. Ícono y Título Dinámico
        
        # Definición de estilos y rutas de íconos según el tipo
        if tipo == "exito":
            color_borde = COLOR_EXITO_PRIMARIO
            # Usa un ícono de "check" si lo tienes, o un símbolo de información
            icon_path = "recursos/icono_check_success.png" 
            titulo_texto = "¡Operación Exitosa!"
        elif tipo == "error":
            color_borde = COLOR_ERROR_SECUNDARIO
            # Usa un ícono de "advertencia" o "cruz" si lo tienes
            icon_path = "recursos/icono_error.png"
            titulo_texto = "Error de Validación"
        else: # "info" o cualquier otro
            color_borde = "#666666" 
            icon_path = "recursos/icono_info.png" 
            titulo_texto = "Información del Sistema"

        # Puedes usar QPixmap si tienes los íconos guardados, o QStyle si usas íconos estándar de Qt.
        # Asumiendo que usarás tus propios recursos para el look and feel.
        try:
            lbl_icono = QLabel()
            pixmap = QPixmap(icon_path)
            # Escalar el ícono
            lbl_icono.setPixmap(pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            layout_header.addWidget(lbl_icono)
        except Exception:
             # Si no tienes los íconos, puedes omitir esta parte
             pass

        lbl_titulo = QLabel(titulo_texto)
        font_titulo = QFont("Arial", 14)
        font_titulo.setBold(True)
        lbl_titulo.setFont(font_titulo)
        lbl_titulo.setStyleSheet(f"color: {color_borde}; border: none;")
        layout_header.addWidget(lbl_titulo)
        
        layout_principal.addWidget(widget_header)

        # 5. Mensaje (Centrado)
        lbl_mensaje = QLabel(mensaje)
        lbl_mensaje.setWordWrap(True)
        lbl_mensaje.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font_msg = QFont("Arial", 11)
        lbl_mensaje.setFont(font_msg)
        lbl_mensaje.setStyleSheet(f"color: {COLOR_TEXTO}; border: none;")
        layout_principal.addWidget(lbl_mensaje)
        
        # Añadir un espacio flexible para empujar el boton hacia abajo
        layout_principal.addStretch(1)

        # 6. Botón Aceptar (Centrado y Personalizado)
        btn_aceptar = QPushButton("Aceptar")
        btn_aceptar.clicked.connect(self.accept)
        btn_aceptar.setFixedSize(120, 35)
        
        # Estilo del boton usando el color de éxito
        btn_aceptar.setStyleSheet(f"""
            QPushButton {{
               background: {COLOR_EXITO_PRIMARIO};
               color: WHITE;
               border: none;
               border-radius: 8px;
               font-weight: bold;
               font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: #0D4FAB;    
            }}
        """)

        # Contenedor para centrar el botón
        widget_btn_contenedor = QWidget()
        layout_btn = QHBoxLayout(widget_btn_contenedor)
        layout_btn.setContentsMargins(0, 0, 0, 0)
        layout_btn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_btn.addWidget(btn_aceptar)
        
        layout_principal.addWidget(widget_btn_contenedor)
        
        # 7. Centrar el Dialogo en la Pantalla
        self.move_to_center()

    def move_to_center(self):
        """Mueve el diálogo al centro de la pantalla principal."""
        if self.parent():
            # Centrar respecto a la ventana padre
            parent_rect = self.parent().geometry()
            self.move(parent_rect.x() + (parent_rect.width() - self.width()) // 2,
                      parent_rect.y() + (parent_rect.height() - self.height()) // 2)
        else:
            # Centrar respecto a la pantalla si no hay padre
            screen = QApplication.primaryScreen()
            center = screen.geometry().center()
            self.move(center.x() - self.width() // 2, center.y() - self.height() // 2)

# =========================================================================
# FUNCION DE LLAMADA DE EJEMPLO
# =========================================================================

def mostrar_mensaje_tcn(mensaje, tipo="info", parent=None):
    """
    Función de utilidad para mostrar el diálogo.
    
    :param mensaje: El texto que se mostrará.
    :param tipo: 'exito', 'error', o 'info'.
    :param parent: La ventana padre (MainWindow), para centrarse correctamente.
    """
    dialogo = DialogoMensajePersonalizado(mensaje, tipo, parent)
    dialogo.exec()

# =========================================================================
# EJEMPLO DE USO
# =========================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 1. Ejemplo de mensaje de ÉXITO
    mostrar_mensaje_tcn(
        "El nuevo registro de reservación ha sido guardado exitosamente en la base de datos.", 
        tipo="exito"
    )

    # 2. Ejemplo de mensaje de ERROR/ADVERTENCIA
    mostrar_mensaje_tcn(
        "El formato del DNI es inválido. Por favor, verifique el campo e intente de nuevo.", 
        tipo="error"
    )
    
    # 3. Ejemplo de mensaje de INFORMACIÓN
    mostrar_mensaje_tcn(
        "Esta función requiere privilegios de administrador para ser ejecutada.", 
        tipo="info"
    )

    # Nota: Si usas esto dentro de tu VentanaReservaciones, 
    # debes pasarle 'self' como argumento 'parent'.

    sys.exit(app.exec())