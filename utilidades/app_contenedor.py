#Este modulo contiene todas las referencias a los controladores del programa.
class AppContenedor:
    def __init__(self, ruta_controlador, controlador_ventana_horarios):
        # Almacena los controladores como atributos
        self.ruta_controlador = ruta_controlador
        self.controlador_ventana_horarios = controlador_ventana_horarios