#Modulo encargardo de la conexion con la BD.
import mysql.connector
from mysql.connector import Error

class Connection:

    #parametros
    host = 'localhost'
    port = 3306
    user = 'root'
    password = ''
    database = 'tcn'

    _conexion = None


    @classmethod
    def getConnection(cls):
        if cls._conexion == None or not cls._conexion.is_connected():
            try:
                cls._conexion = mysql.connector.connect(
                host = cls.host,
                port = cls.port, 
                user = cls.user, 
                password = cls.password, 
                database = cls.database,
                use_pure = True)
            except Error as e:
                cls._conexion = None
                print(f'Error: Fallo conectar con la DB.{e}')
                raise Error(f'Error de MySQL al intectar conectar con la BD. {e}')
        #si no hay falla se regresa la conexion
        return cls._conexion
    
    @classmethod
    def closeConnection(cls):
        if cls._conexion and cls._conexion.is_connected():
            print('Cerrando la conexion con la BD.')
            cls._conexion.close()
        cls._conexion = None
            
'''
    # CREATE    
    def registrar(self, comando):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(comando)
                self.conexion.commit()
                print("Registro exitoso")
                return 1  
            except Error as valError:
                print("Error en registro")
                print(valError)
                return -1  
        return -1
                
                
    #READ - select
    def lista(self, comando):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() 
                cursor.execute(comando) 
                resultados = cursor.fetchall() 
                return resultados
            except Error as valError:
                print("Error en conexión")
                print(valError)
        return 0 
    
                
                
    # UPDATE
    def actualizar(self, comando):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() 
                cursor.execute(comando) 
                self.conexion.commit()
                contador = cursor.rowcount
                return contador
            except Error as valError:
                print("Error en actualización")
                print(valError)
        return -1         
    
'''


