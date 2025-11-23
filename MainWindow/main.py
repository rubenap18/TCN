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
from ui.index_ui import Ui_MainWindow 
from ui.RutasDialog import Ui_Dialog
from PySide6.QtWidgets import QDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() #crea una instancia de la interfaz generada
        self.ui.setupUi(self) #Toma todos los widgets definidos en el .ui y los "dibuja" en esta ventana

          # Ajusta la importación según tu proyecto
        self.db = Database()
        self.ciudades_map = {}
        self.codigos_map = {}
        self.ui.srch_line.textChanged.connect(self.buscar_operadores)

        # CONFIGURACIÓN INICIAL DE PÁGINAS
        self.ui.side_stackedWidget.setCurrentIndex(0)  # Primera página del sidebar
        self.ui.main_stackedWidget.setCurrentIndex(0)  # Primera página principal

        self.configurar_navegacion()
        self.cargar_dashboard()

    def on_page_changed(self, index):
        """Se ejecuta cuando cambia la página del stacked widget"""
        if index == 0:  # Página del dashboard (página 0)
            self.cargar_dashboard()

    def configurar_navegacion(self):
            # Ejemplo: conectar botones del sidebar
            #self.ui.rutas_pushButton4.connect(self.mostrar_pagina_inicio)
        self.ui.rutas_pushButton.clicked.connect(self.mostrar_pagina_rutas)
        self.ui.operadores_pushButton.clicked.connect(self.mostrar_pagina_operadores)

        #botones de rutas
        self.ui.addr_btn.clicked.connect(self.abrir_dialogo_agregar)
        self.ui.editr_bbtn.clicked.connect(self.editar_ruta_seleccionada)
        self.ui.forigen_comboBox.currentTextChanged.connect(self.filtrar_rutas)
        self.ui.fdestino_comboBox.currentTextChanged.connect(self.filtrar_rutas)
        self.cargar_ciudades()

        #botones de operadores
        self.ui.addo_btn.clicked.connect(self.abrir_dialogo_agregar_operador)
        self.ui.edito_btn.clicked.connect(self.editar_operador_seleccionado)
        
        # Buscador de operadores
        self.ui.srch_line.textChanged.connect(self.buscar_operadores)

    def mostrar_pagina_inicio(self):
        self.ui.main_stackedWidget.setCurrentIndex(0)
        self.ui.side_stackedWidget.setCurrentIndex(0)
        
    def mostrar_pagina_operadores(self):
        self.ui.main_stackedWidget.setCurrentIndex(1)
        self.ui.side_stackedWidget.setCurrentIndex(1)
        self.cargar_operadores_desde_bd()
        
    def mostrar_pagina_rutas(self):
        self.ui.main_stackedWidget.setCurrentIndex(2)
        self.ui.side_stackedWidget.setCurrentIndex(2)
        self.cargar_rutas_desde_bd()


    def cargar_corridas_dashboard(self):
        """Carga las corridas recientes o del día actual"""
        try:
            comando = """
            SELECT c.numero, c.fecha, c.hora_salida, 
                   co.nombre as origen, cd.nombre as destino
            FROM corrida c
            JOIN ruta r ON c.ruta = r.codigo
            JOIN ciudad co ON r.ciudadorigen = co.codigo
            JOIN ciudad cd ON r.ciudaddestino = cd.codigo
            WHERE c.fecha >= CURDATE()
            ORDER BY c.fecha, c.hora_salida
            """
            
            corridas = self.db.lista(comando)
            
            self.ui.corridasm_tableWidget.setRowCount(0)
            
            for fila_idx, corrida in enumerate(corridas):
                numero, fecha, hora_salida, origen, destino = corrida
                
                self.ui.corridasm_tableWidget.insertRow(fila_idx)
                
                self.ui.corridasm_tableWidget.setItem(fila_idx, 0, QTableWidgetItem(str(numero)))
                self.ui.corridasm_tableWidget.setItem(fila_idx, 1, QTableWidgetItem(str(fecha)))
                self.ui.corridasm_tableWidget.setItem(fila_idx, 2, QTableWidgetItem(str(hora_salida)))
                self.ui.corridasm_tableWidget.setItem(fila_idx, 3, QTableWidgetItem(f"{origen} - {destino}"))
                
            print(f"✓ {len(corridas)} corridas cargadas en dashboard")
            
        except Exception as e:
            print(f"Error al cargar corridas dashboard: {e}")

    def cargar_autobuses_dashboard(self):
        """Carga autobuses recientemente agregados"""
        try:
            comando = """
            SELECT numero, matricula, marca, modelo, tipoAutobus
            FROM autobus 
            ORDER BY numero DESC 
            """
            
            autobuses = self.db.lista(comando)
            
            self.ui.autobusm_tableWidget.setRowCount(0)
            
            for fila_idx, autobus in enumerate(autobuses):
                numero, matricula, marca, modelo, tipo = autobus
                
                self.ui.autobusm_tableWidget.insertRow(fila_idx)
                
                self.ui.autobusm_tableWidget.setItem(fila_idx, 0, QTableWidgetItem(str(numero)))
                self.ui.autobusm_tableWidget.setItem(fila_idx, 1, QTableWidgetItem(matricula))
                self.ui.autobusm_tableWidget.setItem(fila_idx, 2, QTableWidgetItem(f"{marca} {modelo}"))
                self.ui.autobusm_tableWidget.setItem(fila_idx, 3, QTableWidgetItem(tipo))
                
            print(f"✓ {len(autobuses)} autobuses cargados en dashboard")
            
        except Exception as e:
            print(f"Error al cargar autobuses dashboard: {e}")

    def cargar_pasajeros_dashboard(self):
        """Carga pasajeros recientemente registrados"""
        try:
            comando = """
            SELECT numero, nombre, apellPat, apellMat, 
                   TIMESTAMPDIFF(YEAR, fechaNac, CURDATE()) as edad,
                   telefono
            FROM pasajero 
            ORDER BY numero DESC 
            """
            
            pasajeros = self.db.lista(comando)
            
            self.ui.pasajerosm_tableWidget.setRowCount(0)
            
            for fila_idx, pasajero in enumerate(pasajeros):
                numero, nombre, apellPat, apellMat, edad, telefono = pasajero
                
                self.ui.pasajerosm_tableWidget.insertRow(fila_idx)
                
                self.ui.pasajerosm_tableWidget.setItem(fila_idx, 0, QTableWidgetItem(str(numero)))
                self.ui.pasajerosm_tableWidget.setItem(fila_idx, 1, QTableWidgetItem(f"{nombre} {apellPat} {apellMat}"))
                self.ui.pasajerosm_tableWidget.setItem(fila_idx, 2, QTableWidgetItem(str(edad)))
                self.ui.pasajerosm_tableWidget.setItem(fila_idx, 3, QTableWidgetItem(telefono))
                
            print(f"✓ {len(pasajeros)} pasajeros cargados en dashboard")
            
        except Exception as e:
            print(f"Error al cargar pasajeros dashboard: {e}")

    def cargar_dashboard(self):
        """Carga todos los datos del dashboard"""
        self.cargar_corridas_dashboard()
        self.cargar_autobuses_dashboard()
        self.cargar_pasajeros_dashboard()
        print("✓ Dashboard completamente cargado")

 
    def cargar_ciudades(self):
        """Cargar todas las ciudades para usar en diálogos"""
        try:
            ciudades = self.db.obtener_ciudades()
            self.ciudades_map = {}  # nombre -> código
            self.codigos_map = {}   # código -> nombre
            
            for codigo, nombre in ciudades:
                self.ciudades_map[nombre] = codigo
                self.codigos_map[codigo] = nombre
                
            print(f"✓ {len(ciudades)} ciudades cargadas")
            
        except Exception as e:
            print(f"Error al cargar ciudades: {e}")
    

    def cargar_rutas_desde_bd(self):
        """Carga las rutas desde la base de datos a la tabla"""
        try:
            rutas = self.db.obtener_rutas()  # ← Ya son objetos Ruta
            
            # Guardar para filtros
            self.todas_las_rutas = rutas
            
            # Llenar los ComboBox de filtro con ciudades
            self.llenar_filtros_ciudades()
            
            # Limpiar tabla
            self.ui.rutas_tableWidget.setRowCount(0)
            
            # Llenar tabla con datos de la BD
            for fila_idx, ruta in enumerate(rutas):
                self.ui.rutas_tableWidget.insertRow(fila_idx)
                
                # ↓↓↓ USAR GETTERS DEL OBJETO Ruta ↓↓↓
                self.ui.rutas_tableWidget.setItem(fila_idx, 0, QTableWidgetItem(str(ruta.get_codigo())))
                self.ui.rutas_tableWidget.setItem(fila_idx, 1, QTableWidgetItem(ruta.get_ciudadorigen()))
                self.ui.rutas_tableWidget.setItem(fila_idx, 2, QTableWidgetItem(ruta.get_ciudaddestino()))
                self.ui.rutas_tableWidget.setItem(fila_idx, 3, QTableWidgetItem(f"{ruta.get_distancia()} km"))
                
            print(f"✓ {len(rutas)} rutas cargadas (sin filtros)")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar las rutas: {e}")

    def abrir_dialogo_agregar(self):
        """Abre el diálogo para agregar nueva ruta"""
        try:
            from ui.RutasDialog import Ui_Dialog
            from PySide6.QtWidgets import QDialog, QMessageBox
            
            dialogo = QDialog(self)
            ui = Ui_Dialog()
            ui.setupUi(dialogo)
            
            # Llenar ComboBox con nombres de ciudades
            ui.cmb_origen.clear()
            ui.cmb_destino.clear()
            
            for nombre_ciudad in self.ciudades_map.keys():
                ui.cmb_origen.addItem(nombre_ciudad)
                ui.cmb_destino.addItem(nombre_ciudad)
            
            ui.addr_btn.clicked.connect(dialogo.accept)
            ui.btn_cancelar.clicked.connect(dialogo.reject)
            
            if dialogo.exec():
                nombre_origen = ui.cmb_origen.currentText()
                nombre_destino = ui.cmb_destino.currentText()
                distancia = ui.txt_distancia.text().strip()

                # Validar que no sean la misma ciudad
                if nombre_origen == nombre_destino:
                    QMessageBox.warning(
                        self, 
                        "Error de validación", 
                        "El origen y el destino no pueden ser la misma ciudad."
                    )
                    return
                
                # Validar campos obligatorios
                if not nombre_origen or not nombre_destino or not distancia:
                    QMessageBox.warning(
                        self,
                        "Error de validación",
                        "Todos los campos son obligatorios."
                    )
                    return
                
                # Validar que la distancia sea un número
                try:
                    float(distancia)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Error de validación", 
                        "La distancia debe ser un número válido."
                    )
                    return
                
                # Convertir nombres a códigos
                codigo_origen = self.ciudades_map.get(nombre_origen)
                codigo_destino = self.ciudades_map.get(nombre_destino)
                
                print(f"DEBUG - Agregando ruta:")
                print(f"  Origen: {nombre_origen} -> {codigo_origen}")
                print(f"  Destino: {nombre_destino} -> {codigo_destino}")
                print(f"  Distancia: {distancia}")
                
                if codigo_origen and codigo_destino:
                    # Insertar y manejar el resultado
                    resultado = self.db.insertar_ruta_completa(codigo_origen, codigo_destino, distancia)
                    
                    if resultado == True:
                        self.cargar_rutas_desde_bd()
                        QMessageBox.information(self, "Éxito", "Ruta agregada correctamente")
                        print("✓ Ruta agregada correctamente")
                    elif resultado == "duplicado":
                        # MOSTRAR MENSAJE AMIGABLE PARA RUTA DUPLICADA
                        QMessageBox.information(
                            self,
                            "Ruta ya existe",
                            f"La ruta {nombre_origen} - {nombre_destino} ya existe.\n\n"
                            f"Si desea modificar la distancia, por favor use la opción 'Editar'."
                        )
                        print("ℹ️ Ruta ya existe, mostrando mensaje al usuario")
                    else:
                        QMessageBox.critical(self, "Error", "No se pudo agregar la ruta en la BD")
                        print("✗ Error al agregar ruta en la BD")
                else:
                    QMessageBox.critical(self, "Error", "Error: Ciudad no encontrada")
                    print("✗ Error: Ciudad no encontrada")
                            
        except Exception as e:
            print(f"Error al abrir diálogo: {e}")
            QMessageBox.critical(self, "Error", f"Error al abrir diálogo: {e}")

    def closeEvent(self, event):
        """Se ejecuta al cerrar la ventana"""
        self.db.cerrar()
        event.accept()

    def abrir_dialogo_editar_operador(self, numero_operador):
        """Abrir diálogo para editar operador específico"""
        try:
            print("=== INICIANDO DIÁLOGO EDICIÓN - PASO 1 ===")
            
            # PRIMERO: Solo importaciones básicas
            from PySide6.QtCore import QDate
            from datetime import date
            
            print("=== PASO 2: OBTENER DATOS ===")
            operadores = self.db.obtener_operadores()
            operador_actual = None
            
            for op in operadores:
                if op[0] == numero_operador:
                    operador_actual = op
                    break
            
            if not operador_actual:
                print("Operador no encontrado")
                return
                
            numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato = operador_actual
            
            print(f"DEBUG - fechaNac: {fechaNac} (tipo: {type(fechaNac)})")
            
            print("=== PASO 3: CONVERTIR FECHAS ===")
            # Convertir ANTES de cualquier importación de diálogo
            if isinstance(fechaNac, date):
                qdate_nac = QDate(fechaNac.year, fechaNac.month, fechaNac.day)
                print(f"✓ fechaNac convertida a QDate: {qdate_nac}")
            else:
                qdate_nac = QDate.currentDate()
                print(f"⚠ fechaNac usando currentDate: {qdate_nac}")
                
            if isinstance(fechaContrato, date):
                qdate_cont = QDate(fechaContrato.year, fechaContrato.month, fechaContrato.day)
                print(f"✓ fechaContrato convertida a QDate: {qdate_cont}")
            else:
                qdate_cont = QDate.currentDate()
                print(f"⚠ fechaContrato usando currentDate: {qdate_cont}")
            
            print("=== PASO 4: IMPORTAR DIÁLOGO ===")
            from ui.OperadorDialog_ui import Ui_Dialog
            from PySide6.QtWidgets import QDialog
            from validaciones import Validador
            
            print("=== PASO 5: CREAR DIÁLOGO ===")
            validador = Validador()
            dialogo = QDialog(self)
            ui = Ui_Dialog()
            
            print("=== PASO 6: SETUP UI ===")
            ui.setupUi(dialogo)  # ← ¿FALLA AQUÍ?
            print("✓ Setup UI completado")
            
            print("=== PASO 7: CONFIGURAR CAMPOS ===")
            ui.name_lineEdit.setText(nombre)
            ui.ap_lineEdit.setText(apellPat)
            ui.am_lineEdit.setText(apellMat)
            ui.tel_lineEdit.setText(telefono)
            ui.dateEdit.setDate(qdate_nac)
            ui.dateEdit_2.setDate(qdate_cont)
            
            print("=== PASO 8: CONFIGURAR BOTONES ===")
            ui.addo_pushButton.clicked.connect(dialogo.accept)
            ui.cano_pushButton.clicked.connect(dialogo.reject)
            ui.addo_pushButton.setText("Actualizar Operador")
            
            print("=== PASO 9: EJECUTAR DIÁLOGO ===")
            if dialogo.exec():
                print("=== PASO 10: PROCESAR RESULTADOS ===")
                # ... resto del código
            
        except Exception as e:
            print(f"❌ ERROR en abrir_dialogo_editar_operador: {e}")
            import traceback
            traceback.print_exc()

    def editar_ruta_seleccionada(self):
        """Editar la ruta seleccionada en la tabla"""
        try:
            fila_seleccionada = self.ui.rutas_tableWidget.currentRow()
            
            
            if fila_seleccionada == -1:
                from PySide6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "Advertencia", "Selecciona una ruta para editar")
                return
            
            codigo_item = self.ui.rutas_tableWidget.item(fila_seleccionada, 0)
            if not codigo_item:
                print("✗ No se pudo obtener el código de la ruta")
                return
                
            # ↓↓↓ QUITAR int() - el código ya es string ↓↓↓
            codigo_ruta = codigo_item.text()  # ← SOLO .text(), sin int()
            
            # Obtener datos actuales de la tabla
            ciudadorigen = self.ui.rutas_tableWidget.item(fila_seleccionada, 1).text()
            ciudaddestino = self.ui.rutas_tableWidget.item(fila_seleccionada, 2).text()
            distancia_actual = self.ui.rutas_tableWidget.item(fila_seleccionada, 3).text().replace(" km", "")
            
            # Abrir diálogo de edición
            self.abrir_dialogo_editar(codigo_ruta, ciudadorigen, ciudaddestino, distancia_actual)
            
        except Exception as e:
            print(f"Error al editar ruta: {e}")

    def abrir_dialogo_editar(self, codigo_ruta, origen_actual, destino_actual, distancia_actual):
        """Abre diálogo para editar ruta existente - SOLO DISTANCIA"""
        try:
            from ui.RutasDialog import Ui_Dialog
            from PySide6.QtWidgets import QDialog, QMessageBox
            
            dialogo = QDialog(self)
            ui = Ui_Dialog()
            ui.setupUi(dialogo)
            
            # Título específico para edición
            dialogo.setWindowTitle(f"Editar Distancia - {origen_actual} a {destino_actual}")
            
            # Llenar ComboBox pero DESHABILITARLOS - no se pueden cambiar las ciudades
            ui.cmb_origen.clear()
            ui.cmb_destino.clear()
            
            for nombre_ciudad in self.ciudades_map.keys():
                ui.cmb_origen.addItem(nombre_ciudad)
                ui.cmb_destino.addItem(nombre_ciudad)
            
            # Establecer valores actuales
            ui.cmb_origen.setCurrentText(origen_actual)
            ui.cmb_destino.setCurrentText(destino_actual)
            ui.txt_distancia.setText(distancia_actual.replace(" km", ""))
            
            # **DESHABILITAR CAMBIO DE CIUDADES** - ya existen todas las combinaciones
            ui.cmb_origen.setEnabled(False)
            ui.cmb_destino.setEnabled(False)
            
            # Cambiar estilo para indicar que son de solo lectura
            ui.cmb_origen.setStyleSheet("background-color: #f5f5f5; color: #666;")
            ui.cmb_destino.setStyleSheet("background-color: #f5f5f5; color: #666;")
            
            # Cambiar textos para ser más claros
            ui.addr_btn.setText("Actualizar Distancia")
            
            # Actualizar labels si existen en tu diálogo
            try:
                if hasattr(ui, 'label'):
                    ui.label.setText(f"Editar Distancia - Ruta {codigo_ruta}")
                if hasattr(ui, 'label_3'):
                    ui.label_3.setText("Origen (fijo):")
                if hasattr(ui, 'label_4'):
                    ui.label_4.setText("Destino (fijo):")
                if hasattr(ui, 'label_5'):
                    ui.label_5.setText("Nueva Distancia (km):")
            except:
                pass
            
            ui.addr_btn.clicked.connect(dialogo.accept)
            ui.btn_cancelar.clicked.connect(dialogo.reject)
            
            if dialogo.exec():
                distancia = ui.txt_distancia.text().strip()

                # Validaciones
                if not distancia:
                    QMessageBox.warning(self, "Error", "La distancia es obligatoria.")
                    return
                
                # Validar que sea un número válido
                try:
                    distancia_numero = float(distancia)
                    if distancia_numero <= 0:
                        QMessageBox.warning(self, "Error", "La distancia debe ser mayor a 0.")
                        return
                except ValueError:
                    QMessageBox.warning(self, "Error", "La distancia debe ser un número válido.")
                    return
                
                print(f"DEBUG - Actualizando distancia de ruta {codigo_ruta}:")
                print(f"  Ruta: {origen_actual} -> {destino_actual}")
                print(f"  Nueva distancia: {distancia} km")
                
                # **SOLO ACTUALIZAR LA DISTANCIA** - las ciudades se mantienen igual
                resultado = self.db.actualizar_distancia_ruta(codigo_ruta, distancia)
                
                if resultado:
                    self.cargar_rutas_desde_bd()
                    QMessageBox.information(self, "Éxito", f"Distancia de {origen_actual} a {destino_actual} actualizada correctamente")
                    print(f"✓ Distancia actualizada: {distancia} km")
                else:
                    QMessageBox.critical(self, "Error", "No se pudo actualizar la distancia en la base de datos")
                            
        except Exception as e:
            print(f"Error al abrir diálogo de edición: {e}")
            QMessageBox.critical(self, "Error", f"No se pudo abrir el diálogo: {e}")
        
    
    
    def filtrar_rutas(self):
        """Filtrar rutas según los ComboBox seleccionados"""
        try:
            filtro_origen = self.ui.forigen_comboBox.currentText()
            filtro_destino = self.ui.fdestino_comboBox.currentText()
            
            if not hasattr(self, 'todas_las_rutas') or not self.todas_las_rutas:
                return
            
            rutas_filtradas = []
            for ruta in self.todas_las_rutas:  # ← ruta es objeto Ruta
                # ↓↓↓ USAR GETTERS PARA FILTRAR ↓↓↓
                coincide_origen = (filtro_origen == "Todos" or filtro_origen == "" or 
                                ruta.get_ciudadorigen() == filtro_origen)
                
                coincide_destino = (filtro_destino == "Todos" or filtro_destino == "" or 
                                ruta.get_ciudaddestino() == filtro_destino)
                
                if coincide_origen and coincide_destino:
                    rutas_filtradas.append(ruta)
            
            self.mostrar_rutas_en_tabla(rutas_filtradas)
            
        except Exception as e:
            print(f"Error al filtrar rutas: {e}")

    
    def mostrar_rutas_en_tabla(self, rutas):
        """Mostrar rutas en la tabla"""
        try:
            self.ui.rutas_tableWidget.setRowCount(0)
            
            for fila_idx, ruta in enumerate(rutas):
                self.ui.rutas_tableWidget.insertRow(fila_idx)
                
                # ↓↓↓ USAR GETTERS DEL OBJETO ↓↓↓
                self.ui.rutas_tableWidget.setItem(fila_idx, 0, QTableWidgetItem(str(ruta.get_codigo())))
                self.ui.rutas_tableWidget.setItem(fila_idx, 1, QTableWidgetItem(ruta.get_ciudadorigen()))
                self.ui.rutas_tableWidget.setItem(fila_idx, 2, QTableWidgetItem(ruta.get_ciudaddestino()))
                self.ui.rutas_tableWidget.setItem(fila_idx, 3, QTableWidgetItem(f"{ruta.get_distancia()} km"))
                
            print(f"✓ Mostrando {len(rutas)} rutas filtradas")
            
        except Exception as e:
            print(f"Error al mostrar rutas en tabla: {e}")

    def llenar_filtros_ciudades(self):
        """Llenar los ComboBox de filtro con ciudades únicas"""
        try:
            # Obtener todas las rutas para extraer ciudades únicas
            rutas = self.db.obtener_rutas()
            
            # Extraer orígenes y destinos únicos (ahora son objetos Ruta)
            origenes = set()
            destinos = set()
            
            for ruta in rutas:
                # ↓↓↓ USAR GETTERS EN LUGAR DE DESEMPAQUETAR ↓↓↓
                origenes.add(ruta.get_ciudadorigen())
                destinos.add(ruta.get_ciudaddestino())
            
            # Ordenar alfabéticamente
            origenes = sorted(list(origenes))
            destinos = sorted(list(destinos))
            
            # Limpiar ComboBox
            self.ui.forigen_comboBox.clear()
            self.ui.fdestino_comboBox.clear()
            
            # Agregar opción "Todos"
            self.ui.forigen_comboBox.addItem("Todos")
            self.ui.fdestino_comboBox.addItem("Todos")
            
            # Llenar con ciudades únicas
            for origen in origenes:
                self.ui.forigen_comboBox.addItem(origen)
            
            for destino in destinos:
                self.ui.fdestino_comboBox.addItem(destino)
                
            print(f"✓ Filtros llenados - {len(origenes)} orígenes, {len(destinos)} destinos")
            
        except Exception as e:
            print(f"Error al llenar filtros: {e}")



    #fun de operadores
    def cargar_operadores_desde_bd(self):
        try:
            operadores = self.db.obtener_operadores()  # ← Ya son objetos Operador
            
            self.ui.o_tableWidget.setRowCount(0)
            
            for fila_idx, operador in enumerate(operadores):
                self.ui.o_tableWidget.insertRow(fila_idx)
                
                # ↓↓↓ USAR GETTERS DEL OBJETO ↓↓↓
                self.ui.o_tableWidget.setItem(fila_idx, 0, QTableWidgetItem(str(operador.get_numero())))
                self.ui.o_tableWidget.setItem(fila_idx, 1, QTableWidgetItem(operador.get_nombre_completo()))
                self.ui.o_tableWidget.setItem(fila_idx, 2, QTableWidgetItem(str(operador.get_fechaNac())))
                self.ui.o_tableWidget.setItem(fila_idx, 3, QTableWidgetItem(operador.get_telefono()))
                self.ui.o_tableWidget.setItem(fila_idx, 4, QTableWidgetItem(str(operador.get_fechaContrato())))
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los operadores: {e}")


    def abrir_dialogo_agregar_operador(self):
        try:
            from ui.OperadorDialog_ui import Ui_Dialog
            from PySide6.QtWidgets import QDialog
            from validaciones.validaciones import Validador  # ← IMPORTACIÓN SIMPLE
            
            dialogo = QDialog(self)
            ui = Ui_Dialog()
            ui.setupUi(dialogo)
            
            validador = Validador()  # ← Ahora funciona
            
            ui.addo_pushButton.clicked.connect(dialogo.accept)
            ui.cano_pushButton.clicked.connect(dialogo.reject)
            
            if dialogo.exec():
                nombre = ui.name_lineEdit.text().strip()
                apellPat = ui.ap_lineEdit.text().strip()
                apellMat = ui.am_lineEdit.text().strip()
                telefono = ui.tel_lineEdit.text().strip()
                fechaNac = ui.dateEdit.date().toString("yyyy-MM-dd")
                fechaContrato = ui.dateEdit_2.date().toString("yyyy-MM-dd")
                
                valido, errores = validador.validar_operador_completo(
                    nombre, apellPat, apellMat, telefono, fechaNac, fechaContrato
                )
                
                if valido:
                    if self.db.insertar_operador(nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato):
                        self.cargar_operadores_desde_bd()
                        print("✓ Operador agregado correctamente")
                    else:
                        QMessageBox.critical(self, "Error", "No se pudo agregar el operador")
                else:
                    validador.mostrar_errores(self, errores)
                        
        except Exception as e:
            print(f"Error al abrir diálogo operador: {e}")

    def editar_operador_seleccionado(self):
        try:
            fila_seleccionada = self.ui.o_tableWidget.currentRow()
            
            if fila_seleccionada == -1:
                QMessageBox.warning(self, "Advertencia", "Selecciona un operador para editar")
                return
            
            numero_item = self.ui.o_tableWidget.item(fila_seleccionada, 0)
            if not numero_item:
                print("✗ No se pudo obtener el número del operador")
                return
                
            # ↓↓↓ DEJAR COMO STRING - se convertirá en abrir_dialogo_editar_operador ↓↓↓
            numero_operador = numero_item.text()
            
            self.abrir_dialogo_editar_operador(numero_operador)
            
        except Exception as e:
            print(f"Error al editar operador: {e}")

    def abrir_dialogo_editar_operador(self, numero_operador):
        try:
            from ui.OperadorDialog_ui import Ui_Dialog
            from PySide6.QtWidgets import QDialog
            from PySide6.QtCore import QDate
            from validaciones.validaciones import Validador
            from datetime import date
            
            validador = Validador()
            
            # Obtener datos actuales del operador (ahora son objetos)
            operadores = self.db.obtener_operadores()
            operador_actual = None
            
            numero_operador_int = int(numero_operador)
            
            for operador in operadores:  # ← operador es objeto Operador
                if operador.get_numero() == numero_operador_int:  # ← USAR GETTER
                    operador_actual = operador
                    break
            
            if not operador_actual:
                print(f"Operador no encontrado: {numero_operador_int}")
                return
                
            # ↓↓↓ USAR GETTERS PARA OBTENER DATOS ↓↓↓
            dialogo = QDialog(self)
            ui = Ui_Dialog()
            ui.setupUi(dialogo)
            
            dialogo.setWindowTitle("Editar Operador")
            ui.label.setText("Editar Operador Existente")
            
            # Llenar con datos actuales usando getters
            ui.name_lineEdit.setText(operador_actual.get_nombre())
            ui.ap_lineEdit.setText(operador_actual.get_apellPat())
            ui.am_lineEdit.setText(operador_actual.get_apellMat())
            ui.tel_lineEdit.setText(operador_actual.get_telefono())
            
            # Convertir fechas usando getters
            fechaNac = operador_actual.get_fechaNac()
            if isinstance(fechaNac, date):
                ui.dateEdit.setDate(QDate(fechaNac.year, fechaNac.month, fechaNac.day))
            else:
                ui.dateEdit.setDate(QDate.currentDate())
                
            fechaContrato = operador_actual.get_fechaContrato()
            if isinstance(fechaContrato, date):
                ui.dateEdit_2.setDate(QDate(fechaContrato.year, fechaContrato.month, fechaContrato.day))
            else:
                ui.dateEdit_2.setDate(QDate.currentDate())
        
        # ... resto del código igual (las validaciones siguen funcionando)
            
            ui.addo_pushButton.clicked.connect(dialogo.accept)
            ui.cano_pushButton.clicked.connect(dialogo.reject)
            ui.addo_pushButton.setText("Actualizar Operador")  # ← Ya está cambiado
            
            if dialogo.exec():
                nuevo_nombre = ui.name_lineEdit.text().strip()
                nuevo_apellPat = ui.ap_lineEdit.text().strip()
                nuevo_apellMat = ui.am_lineEdit.text().strip()
                nuevo_telefono = ui.tel_lineEdit.text().strip()
                nueva_fechaNac = ui.dateEdit.date().toString("yyyy-MM-dd")
                nueva_fechaContrato = ui.dateEdit_2.date().toString("yyyy-MM-dd")
                
                valido, errores = validador.validar_operador_completo(
                    nuevo_nombre, nuevo_apellPat, nuevo_apellMat, nuevo_telefono, 
                    nueva_fechaNac, nueva_fechaContrato
                )
                
                if valido:
                    if self.db.actualizar_operador_completo(numero_operador_int, nuevo_nombre, nuevo_apellPat, nuevo_apellMat, nueva_fechaNac, nuevo_telefono, nueva_fechaContrato):
                        self.cargar_operadores_desde_bd()
                        print(f"✓ Operador {numero_operador_int} actualizado correctamente")
                else:
                    validador.mostrar_errores(self, errores)
                    
        except Exception as e:
            print(f"Error al abrir diálogo de edición operador: {e}")

    
    def buscar_operadores(self):
        """Buscar operadores según el texto en el QLineEdit"""
        try:
            criterio = self.ui.srch_line.text().strip()  # ← NOMBRE CORREGIDO
            
            print(f" DEBUG: Buscando con criterio: '{criterio}'")
            
            if not criterio:
                self.cargar_operadores_desde_bd()
                return
            
            resultados = self.db.buscar_operadores(criterio)
            
            print(f"🔍 DEBUG: {len(resultados)} resultados obtenidos")
            
            self.ui.o_tableWidget.setRowCount(0)
            
            for fila_idx, operador in enumerate(resultados):
                # Usar getters del objeto Operador
                numero = operador.get_numero()
                nombre_completo = operador.get_nombre_completo()
                fechaNac = operador.get_fechaNac()
                telefono = operador.get_telefono()
                fechaContrato = operador.get_fechaContrato()
                
                self.ui.o_tableWidget.insertRow(fila_idx)
                self.ui.o_tableWidget.setItem(fila_idx, 0, QTableWidgetItem(str(numero)))
                self.ui.o_tableWidget.setItem(fila_idx, 1, QTableWidgetItem(nombre_completo))
                self.ui.o_tableWidget.setItem(fila_idx, 2, QTableWidgetItem(str(fechaNac)))
                self.ui.o_tableWidget.setItem(fila_idx, 3, QTableWidgetItem(telefono))
                self.ui.o_tableWidget.setItem(fila_idx, 4, QTableWidgetItem(str(fechaContrato)))
                
            print(f"✓ {len(resultados)} operadores encontrados para '{criterio}'")
            
        except Exception as e:
            print(f"Error al buscar operadores: {e}")
        
    

# Llama esta función en tu __init__
        

        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())



