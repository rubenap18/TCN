from mysql.connector import Error
from utilidades.validaciones import Validaciones

class ControladorVEReservaciones:
    def __init__(self, servicioDeConsulta):
        self.servicio_de_consulta = servicioDeConsulta

    def getTotalReservaciones(self):
        try:
            return self.servicio_de_consulta.consultarNumeroReservaciones()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTotalReservaciones()): {e}')
            raise e


    def consultarTodasReservacionesParaTabla(self):
        try:
            return self.servicio_de_consulta.consultarTodasReservacionesParaTabla()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservaciones()): {e}')
            raise e
        

    def buscarReservacionPorNumero(self,numero):
        validaciones = Validaciones()
        if not validaciones.validar_id(numero):
            return False
        try:
            return self.servicio_de_consulta.buscarReservacionPorNumero(numero)
        except Error as e:
            print(f'Error en ControladorVEReservaciones (buscarReservacionesPorNUmero()): {e}')
            raise e