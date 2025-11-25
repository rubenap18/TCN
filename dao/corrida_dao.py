from dao.db import Connection
from mysql.connector import Error

from objetos.corrida import Corrida
from datetime import date,time


class CorridaDAO:
    conn = None
    
    def consultarCorridasDisponibles(self):
        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = 'SELECT * FROM corrida'
            cursor = conn.cursor()
            cursor.execute(query)
            corridas = cursor.fetchall()

            tupla_corridas = []

            #mapeando respuestas a una lista de objetos
            for corrida in corridas:
                tupla_corridas.append(Corrida(corrida[0],corrida[1],corrida[2],corrida[3],corrida[4],corrida[5],corrida[6],corrida[7],corrida[8]))

            cursor.close()
            return tupla_corridas
        
        except Error as e:
            print(f'Error en RutaDAO (consultarCorridasDisponibles): {e}')
            raise e

    def getCorridaPorID(self, id:int):
        """
        Busca una corrida por su numero (ID).
        
        """
        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = f'SELECT numero, fecha, hora_salida, hora_llegada, tarifaBase, lugaresDisp, autobus, ruta, operador, estado FROM corrida WHERE numero = {id}'
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchone()

            cursor.close()
            
            #mapeando respuestas a una lista de objetos
            return Corrida(respuesta[0],respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[5],respuesta[6],respuesta[7],respuesta[8])

        
        except Error as e:
            print(f'Error en respuestaDAO (getCorridaPorID): {e}')
            raise e

        
    
