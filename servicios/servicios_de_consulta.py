
class ServiciosDeConsulta:
    def __init__(self, ruta_dao,corrida_dao):
        self.ruta_dao = ruta_dao
        self.corrida_dao = corrida_dao

    def consultarRutas(self):
        return self.ruta_dao.consultarTodasRutas()
    
    def consultarCiudadesOrigen(self):
        return self.ruta_dao.consultarCiudadesOrigen()
        
    def consultarCiudadesDestino(self):
        return self.ruta_dao.consultarCiudadesDestino()
    
    def consultarCorridasDisponibles(self):
        return self.corrida_dao.consultarCorridasDisponibles()
    
    