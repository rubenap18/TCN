class ControladorRuta:
    def __init__(self,servicios):
        self.__servicios = servicios

    def consultarTodasRutas(self):
        return self.__servicios.consultarRutas()
    
    def consultarCiudadesOrigen(self):
        return self.__servicios.consultarCiudadesOrigen()

    def consultarCiudadesDestino(self):
        return self.__servicios.consultarCiudadesDestino()
        