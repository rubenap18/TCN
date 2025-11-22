from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QTableWidgetItem
from ui.RutasDialog import Ui_Dialog
from PySide6.QtWidgets import QTableWidgetItem 
import sys
import os
from dao.Database import Database
os.environ["QT_QPA_PLATFORM"] = "xcb"
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog
#from ui.Operadores_ui import Ui_Form as Ui_Operadores
from ui.index import Ui_MainWindow 
from ui.RutasDialog import Ui_Dialog
from PySide6.QtWidgets import QDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() #crea una instancia de la interfaz generada
        self.ui.setupUi(self) #Toma todos los widgets definidos en el .ui y los "dibuja" en esta ventana

          # Ajusta la importación según tu proyecto
        self.db = Database()

        # CONFIGURACIÓN INICIAL DE PÁGINAS
        self.ui.side_stackedWidget.setCurrentIndex(0)  # Primera página del sidebar
        self.ui.main_stackedWidget.setCurrentIndex(0)  # Primera página principal

        self.configurar_navegacion()

    def configurar_navegacion(self):
            # Ejemplo: conectar botones del sidebar
            #self.ui.rutas_pushButton4.connect(self.mostrar_pagina_inicio)
        self.ui.rutas_pushButton.clicked.connect(self.mostrar_pagina_rutas)
        self.ui.operadores_pushButton.clicked.connect(self.mostrar_pagina_operadores)
        self.ui.addr_btn.clicked.connect(self.abrir_dialogo_agregar)

    def mostrar_pagina_inicio(self):
        self.ui.main_stackedWidget.setCurrentIndex(0)
        self.ui.side_stackedWidget.setCurrentIndex(0)
        
    def mostrar_pagina_operadores(self):
        self.ui.main_stackedWidget.setCurrentIndex(1)
        self.ui.side_stackedWidget.setCurrentIndex(1)
        
    def mostrar_pagina_rutas(self):
        self.ui.main_stackedWidget.setCurrentIndex(2)
        self.ui.side_stackedWidget.setCurrentIndex(2)
        self.cargar_rutas_desde_bd()

    def cargar_rutas_desde_bd(self):
            """Carga las rutas desde la base de datos a la tabla"""
            try:
                rutas = self.db.obtener_rutas()
                
                # Limpiar tabla
                self.ui.rutas_tableWidget.setRowCount(0)  # CAMBIADO: tableWidget
                
                # Llenar tabla con datos de la BD
                for fila_idx, ruta in enumerate(rutas):
                    codigo, origen, destino, distancia = ruta
                    self.ui.rutas_tableWidget.insertRow(fila_idx)  # CAMBIADO: tableWidget
                    
                    self.ui.rutas_tableWidget.setItem(fila_idx, 0, QTableWidgetItem(str(codigo)))  # CAMBIADO: tableWidget
                    self.ui.rutas_tableWidget.setItem(fila_idx, 1, QTableWidgetItem(origen))  # CAMBIADO: tableWidget
                    self.ui.rutas_tableWidget.setItem(fila_idx, 2, QTableWidgetItem(destino))  # CAMBIADO: tableWidget
                    self.ui.rutas_tableWidget.setItem(fila_idx, 3, QTableWidgetItem(f"{distancia} km"))  # CAMBIADO: tableWidget
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudieron cargar las rutas: {e}")

    def abrir_dialogo_agregar(self):
        try:
            
            
            # Crear el diálogo directamente
            dialogo = QDialog(self)
            ui_dialogo = Ui_Dialog()
            ui_dialogo.setupUi(dialogo)

            ui_dialogo.addr_btn.clicked.connect(dialogo.accept)    # "Añadir Ruta" = Aceptar
            ui_dialogo.btn_cancelar.clicked.connect(dialogo.reject)  # "Cancelar" = Cancelar

            
            
            # Mostrar el diálogo y esperar respuesta
            if dialogo.exec():
                # Obtener datos directamente del UI
                origen = ui_dialogo.cmb_origen.currentText()
                destino = ui_dialogo.cmb_destino.currentText()
                distancia = ui_dialogo.txt_distancia.text()
                
                # Validar campos
                if origen and destino and distancia:
                    # Guardar en BD
                    if self.db.insertar_ruta(origen, destino, distancia):
                        self.cargar_rutas_desde_bd()
                        print("✓ Ruta agregada correctamente")
                    else:
                        print("✗ Error al agregar ruta en la BD")
                else:
                    print("✗ Todos los campos son obligatorios")
                    
        except Exception as e:
            print(f"Error al abrir diálogo: {e}")
        
    def closeEvent(self, event):
        """Se ejecuta al cerrar la ventana"""
        self.db.cerrar()
        event.accept()
        

        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())



