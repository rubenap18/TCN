from mysql.connector import Error

from utilidades.app_contenedor import AppContenedor
from controladores.controlador_ruta import ControladorRuta
from controladores.controlador_ventana_horarios import ControladorVentanaHorarios
from servicios.servicios_de_consulta import ServiciosDeConsulta
from dao.ruta_dao import RutaDAO
from dao.corrida_dao import CorridaDAO


from dao.db import Connection


from objetos.ruta import Ruta

from ui.main_ui import MainUI

import sys
from PySide6.QtWidgets import QApplication

def main():
    print('Iniciando Transportes Cuervo Negro')
    #Iniciando conexion
    try:
        Connection.getConnection()
        print('Conexion con la BD hecha.')

    except Error as e:
        print(f"ERROR IMPORTANTE: No se pudo iniciar el programita. {e}")
        Connection.closeConnection() #cerrando por si acaso algo quedo abierto en la conexion
        return #terminando la ejecucion del programa

    #Iniciando dao's
    ruta_dao = RutaDAO()
    corrida_dao = CorridaDAO()

    #Iniciando servicios
    servicios_de_consulta = ServiciosDeConsulta(ruta_dao,corrida_dao)

    #Iniciando controladores
    controlador_ruta = ControladorRuta(servicios_de_consulta)
    controlador_ventana_horarios = ControladorVentanaHorarios(servicios_de_consulta)

    
    app_manejador = AppContenedor(ruta_controlador=controlador_ruta,controlador_ventana_horarios=controlador_ventana_horarios)

    #iniciando UI
    print('Iniciando UI')
    app = QApplication(sys.argv)
    ventana = MainUI(app_manejador)
    ventana.show()
    
    exit_code = app.exec()

    #cerrando conexion
    Connection.closeConnection()

    sys.exit(exit_code)


if __name__ == '__main__':
    main()


