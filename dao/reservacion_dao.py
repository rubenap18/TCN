from objetos.reservacion import Reservacion
from dao.db import Connection
from mysql.connector import Error

class ReservacionDAO:
    conn = None

    def getNumeroDeReservaciones(self):

        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = 'SELECT COUNT(*) FROM reservacion'
            cursor = conn.cursor()
            cursor.execute(query)
            respuesta = cursor.fetchall()

            cursor.close()
            return respuesta[0][0]
        
        except Error as e:
            print(f'Error en ReservacionDAO (getNumeroDeReservaciones): {e}')
            raise e

