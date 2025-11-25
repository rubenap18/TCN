from mysql.connector import Error

class ServiciosDeConsulta:
    def __init__(self, ruta_dao,corrida_dao, reservacion_dao):
        self.ruta_dao = ruta_dao
        self.corrida_dao = corrida_dao
        self.reservacion_dao = reservacion_dao

    def consultarRutas(self):
        return self.ruta_dao.consultarTodasRutas()
    
    def consultarCiudadesOrigen(self):
        return self.ruta_dao.consultarCiudadesOrigen()
        
    def consultarCiudadesDestino(self):
        return self.ruta_dao.consultarCiudadesDestino()
    
    def consultarCorridasDisponibles(self):
        return self.corrida_dao.consultarCorridasDisponibles()
    




    # --- COnsultas Reservaciones -- #
    
    def consultarNumeroReservaciones(self):
        try:
            return self.reservacion_dao.getNumeroDeReservaciones()        
        except Error as e:
            print(f'Error en ServiciosDeConsulta (consultarNumeroReservaciones): {e}')
            raise e

    def consultarTodasReservacionesParaTabla(self):
        try:
            reservaciones = []
            return self.reservacion_dao.getTodasReservacionesParaTabla()
        except Error as e:
            print(f'Error en ServiciosDeConsulta (consultarTodasReservaciones): {e}')
            raise e

    def buscarReservacionPorNumero(self,numero):
        return self.reservacion_dao.buscarReservacionPorNumero(numero)
        
    def llenarTablaReservacionesActuales(self):
        pass
    
    def llenarTablaReservacionesPasadas(self):
        pass
    
