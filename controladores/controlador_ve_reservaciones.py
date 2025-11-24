from mysql.connector import Error


class ControladorVEReservaciones:
    def __init__(self, servicioDeConsulta):
        self.servicio_de_consulta = servicioDeConsulta

    def getTotalReservaciones(self):
        try:
            return self.servicio_de_consulta.consultarNumeroReservaciones()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTotalReservaciones()): {e}')
            raise e

