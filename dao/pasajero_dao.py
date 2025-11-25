from dao.db import Connection
from mysql.connector import Error

from objetos.pasajeros import Pasajero
from datetime import date,time


class PasajeroDAO:
    conn = None

    def getPasajeroPorId(self, numero_pasajero: int):
        """
        Busca un pasajero por su numero (ID).
        
        """
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            # La consulta selecciona todos los campos (*) de la tabla pasajero
            query = f'SELECT numero, nombre, apellPat, apellMat, fechaNac, edad, correoElect, telefono FROM pasajero WHERE numero = {numero_pasajero}'
            
            cursor = conn.cursor()
            cursor.execute(query)
            
            # fetchone() devuelve una sola tupla con la fila o None
            respuesta = cursor.fetchone() 
            
            cursor.close()
            return Pasajero(respuesta[0],respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[5],respuesta[6],respuesta[7])
        
        except Error as e:
            print(f'Error en PasajeroDAO (getPasajeroPorId): {e}')
            raise e
    
