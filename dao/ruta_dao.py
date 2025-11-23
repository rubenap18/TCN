from objetos.ruta import Ruta
from dao.db import Connection
from mysql.connector import Error

class RutaDAO:
    conn = None

    def consultarTodasRutas(self):

        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = 'SELECT * FROM ruta'
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()

            #mapeando respuestas a una lista de objetos
            lista_rutas = []
            for fila in resultado:
                lista_rutas.append(Ruta(fila[0],fila[1],fila[2],fila[3]))

            cursor.close()
            return lista_rutas
        
        except Error as e:
            print(f'Error en RutaDAO (consultarTodasRutas): {e}')
            raise e


    
    def consultarCiudadesOrigen(self):

        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = 'SELECT DISTINCT c.nombre AS Nombre FROM ruta INNER JOIN ciudad AS c ON ruta.ciudadOrigen = c.codigo ORDER BY c.nombre ASC'
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()
            
            cursor.close()
            return resultado
        
        except Error as e:
            print(f'Error en RutaDAO (consultar ciudades origen): {e}')
            raise e

        
    
    def consultarCiudadesDestino(self):
            
        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = 'SELECT DISTINCT c.nombre AS Nombre FROM ruta INNER JOIN ciudad AS c ON ruta.ciudadDestino = c.codigo ORDER BY c.nombre ASC'
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()
            
            cursor.close()
            return resultado
        
        except Error as e:
            print(f'Error en RutaDAO (consultarCiudadesDestino): {e}')
            raise e
