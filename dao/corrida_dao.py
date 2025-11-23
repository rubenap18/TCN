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

        
    
