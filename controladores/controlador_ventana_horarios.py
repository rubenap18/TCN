from mysql.connector import Error

class ControladorVentanaHorarios:
    def __init__(self, servicios_de_consulta):
        self.servicios_de_consulta = servicios_de_consulta

    def consultarCorridasDisponibles(self):
        try:
            return self.servicios_de_consulta.consultarCorridasDisponibles()
        except Error as e:
            print(f'Error en ControladorVentanaHorarios (consultarCorridasDisponibles): {e}')
            raise e
