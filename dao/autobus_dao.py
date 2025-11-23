from objetos.autobus import Autobus

class AutobusDAO:
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def consultarAutobusById(self, id_autobus):
        query = f'SELECT * FROM autobus WHERE id_autobus = {id_autobus}'
        cursor = self.__db_connection.cursor()
        cursor.execute(query)
        respuesta = cursor.fetchall()
        autobus = Autobus(respuesta[0],respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[5],respuesta[6],respuesta[7])
        return autobus