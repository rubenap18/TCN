class ControladorVentanaHorarios:
    def __init__(self, servicios_de_consulta):
        self.servicios_de_consulta = servicios_de_consulta

    def consultarCorridasDisponibles(self):
        return self.servicios_de_consulta.consultarCorridasDisponibles()
    
    