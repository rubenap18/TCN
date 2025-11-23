# connection.py
import mysql.connector
from mysql.connector import Error
from objetos.Operador import Operador
from objetos.Ruta import Ruta

class Database:
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                db="tcn")
            print("Conectado a MySQL - Base de datos tcn")
        except Error as variable:
            print("Error en conexion a MySQL")
            print(variable)

    def obtener_rutas(self):
        """Obtiene todas las rutas como objetos Ruta (VERSIÓN MEJORADA)"""
        try:
            comando = """
            SELECT r.codigo, r.ciudadorigen, r.ciudaddestino, r.distancia, co.nombre, cd.nombre 
            FROM ruta r 
            JOIN ciudad co ON r.ciudadorigen = co.codigo 
            JOIN ciudad cd ON r.ciudaddestino = cd.codigo
            """
            resultados = self.lista(comando)
            
            rutas = []
            for fila in resultados:
                # Crear objeto Ruta normal
                ruta = Ruta(fila[0], fila[4], fila[5], fila[3])  # codigo, nombre_origen, nombre_destino, distancia
                
                # Agregar códigos reales como atributos adicionales
                ruta.codigo_origen_real = fila[1]  # "TIJ" 
                ruta.codigo_destino_real = fila[2]  # "ENS"
                rutas.append(ruta)
            
            return rutas
            
        except Exception as e:
            print(f"Error al obtener rutas: {e}")
            return []
        
    
    def obtener_ciudades(self):
        comando = "SELECT codigo, nombre FROM ciudad ORDER BY nombre"
        return self.lista(comando)

# Método para insertar rutas
    def insertar_ruta_completa(self, codigo_origen, codigo_destino, distancia):
        """Método original modificado para generar código de ruta"""
        try:
            distancia_numero = distancia.replace(" km", "")
            # Generar código de ruta
            codigo_ruta = f"{codigo_origen}-{codigo_destino}"
            
            comando = f"INSERT INTO ruta (codigo, ciudadorigen, ciudaddestino, distancia) VALUES ('{codigo_ruta}', '{codigo_origen}', '{codigo_destino}', {distancia_numero})"
            
            print(f"DEBUG - Insertando: {comando}")
            return self.registrar(comando)
            
        except Exception as e:
            print(f"Error en insertar_ruta: {e}")
            return False
    
    

    #READ - Select
    def lista(self, comando):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(comando)
                resultados = cursor.fetchall()
                
                # ↓↓↓ BUSCA SI HAY ALGO ASÍ Y ELIMÍNALO ↓↓↓
                # from PySide6.QtCore import QDate
                # QDate.fromString(...)  # ← ESTO CAUSA EL ERROR
                
                print("Listado correcto")
                return resultados
            except Error as valError:
                print("Error en consulta SELECT")
                print(valError)
        return []
    
    #CREATE - Insert
    def registrar(self, comando):
        """Método para INSERT - MANEJA ERROR DE DUPLICADO"""
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(comando)
                self.conexion.commit()
                print("Registrado correctamente")
                return True
            except Error as valError:
                # MANEJAR ERROR DE CLAVE DUPLICADA
                if "1062" in str(valError) or "Duplicate entry" in str(valError):
                    print(f"Error: Ya existe una ruta con ese código")
                    return "duplicado"
                else:
                    print("Error en INSERT")
                    print(valError)
                    return False
        return False
    
    def actualizar(self, comando):
        """Método para UPDATE/DELETE - VERSIÓN DEBUG"""
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                print(f"DEBUG - Ejecutando: {comando}")
                cursor.execute(comando)
                self.conexion.commit()
                contador = cursor.rowcount
                print(f"DEBUG - Filas afectadas: {contador}")
                return contador
            except Error as valError:
                print(f"ERROR en actualizar: {valError}")
                return -1
        return 0

    def actualizar_distancia_ruta(self, codigo_ruta, distancia):
        """Actualiza solo la distancia de una ruta existente"""
        try:
            distancia_limpia = str(distancia).replace(" km", "").strip()
            
            comando = f"UPDATE ruta SET distancia = {distancia_limpia} WHERE codigo = '{codigo_ruta}'"
            
            print(f"DEBUG - SQL: {comando}")
            resultado = self.actualizar(comando)
            print(f"DEBUG - Filas afectadas: {resultado}")
            
            return resultado > 0
            
        except Exception as e:
            print(f"Error en actualizar_distancia_ruta: {e}")
        return False
    

    def cerrar(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexion cerrada")

    # Métodos para operadores
    def obtener_operadores(self):
        comando = "SELECT numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato FROM operador"
        resultados = self.lista(comando)
        
        operadores = []
        for fila in resultados:
            operador = Operador(*fila)
            operadores.append(operador)
        
        return operadores
        
        return operadores

    def insertar_operador(self, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato):
        """Inserta un nuevo operador en la base de datos"""
        try:
            comando = f"INSERT INTO operador (nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato) VALUES ('{nombre}', '{apellPat}', '{apellMat}', '{fechaNac}', '{telefono}', '{fechaContrato}')"
            
            print(f" DEBUG - SQL a ejecutar: {comando}")
            resultado = self.registrar(comando)
            print(f" DEBUG - Resultado registrar: {resultado}")
            
            return resultado
            
        except Exception as e:
            print(f"❌ ERROR en insertar_operador: {e}")
            return False

    def actualizar_operador_completo(self, numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato):
        comando = f"UPDATE operador SET nombre = '{nombre}', apellPat = '{apellPat}', apellMat = '{apellMat}', fechaNac = '{fechaNac}', telefono = '{telefono}', fechaContrato = '{fechaContrato}' WHERE numero = {numero}"
        return self.actualizar(comando)

    def buscar_operadores(self, criterio):
        """Busca operadores y devuelve objetos Operador"""
        try:
            comando = f"""
            SELECT numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato 
            FROM operador 
            WHERE nombre LIKE '%{criterio}%' 
            OR apellPat LIKE '%{criterio}%' 
            OR apellMat LIKE '%{criterio}%' 
            OR numero LIKE '%{criterio}%'
            """
            
            resultados = self.lista(comando)
            
            # Convertir a objetos Operador
            operadores = []
            for fila in resultados:
                operador = Operador(*fila)
                operadores.append(operador)
            
            return operadores
            
        except Exception as e:
            print(f"Error al buscar operadores: {e}")
            return []
    
    
    
    