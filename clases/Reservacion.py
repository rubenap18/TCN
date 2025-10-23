#Esta es la clase Reservacion creada por Ruben Aguilar

class Reservacion:
    def __init__(self, idReservacion, montoTotal, fechaReservacion):
        self.__idReservacion = idReservacion
        self.__montoTotal = montoTotal
        self.__fecha_reservacion = fechaReservacion

    #getters
    def getID(self):
        return self.__idReservacion

    def getMontoTotal(self):
        return self.__montoTotal

    def getFechaDeReservacion(self):
        return self.__fecha_reservacion

    #setters
    def setMontoTotal(self, montoTotal):
        self.__montoTotal = montoTotal

    def setFechaDeReservacion(self,fechaDeReservacion):
        self.__fecha_reservacion = fechaDeReservacion

    def __str__(self):
        return f'ID RESERVACION: {str(self.__idReservacion)}\nMonto total: {str(self.__montoTotal)}\nFecha de Reservacion: {str(self.__fecha_reservacion)}'