# connection.py
import mysql.connector
from mysql.connector import Error

class Database:
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                db="TCN")
            print("Conectado a MySQL - Base de datos TCN")
        except Error as variable:
            print("Error en conexion a MySQL")
            print(variable)

    # Metodos especificos para rutas
    def insertar_ruta(self, origen, destino, distancia):
        # Quitar " km" del texto si existe
        distancia_numero = distancia.replace(" km", "")
        comando = f"INSERT INTO ruta (origen, destino, distancia) VALUES ('{origen}', '{destino}', {distancia_numero})"
        return self.registrar(comando)
    
    def obtener_rutas(self):
        comando = "SELECT codigo, origen, destino, distancia FROM ruta"  # ← ruta (sin s)
        return self.lista(comando)
    
    def eliminar_ruta(self, codigo_ruta):
        comando = f"DELETE FROM ruta WHERE codigo = {codigo_ruta}"  # ← ruta (sin s)
        return self.actualizar(comando)

    #READ - Select
    def lista(self, comando):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(comando)
                resultados = cursor.fetchall()
                print("Listado correcto")
                return resultados
            except Error as valError:
                print("Error en consulta SELECT")
                print(valError)
        return []
    
    #CREATE - Insert
    def registrar(self, comando):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(comando)
                self.conexion.commit()
                print("Registrado correctamente")
                return True
            except Error as valError:
                print("Error en INSERT")
                print(valError)
        return False

    #Update
    def actualizar(self, comando):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(comando)
                self.conexion.commit()
                contador = cursor.rowcount
                print(f"Actualizado - Filas afectadas: {contador}")
                return contador
            except Error as valError:
                print("Error en UPDATE/DELETE")
                print(valError)
                return -1
        return 0
    
    def cerrar(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexion cerrada")