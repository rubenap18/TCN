#Esta es la clase Reservacion creada por Ruben Aguilar


class Reservacion:
    def __init__(self,numeroReservacion, fechaReservacion, fechaLimitePago, cantidad_pasajeros, subtotal, iva, total):
        self.__numeroReservacion = numeroReservacion
        self.__fecha_reservacion =  fechaReservacion
        self.__fecha_limite_pago = fechaLimitePago
        self.__cantidad_pasajeros = cantidad_pasajeros
        self.__subtotal = subtotal
        self.__iva = iva
        self.__total = total
        self.__pasajero = 0 #fk
        self.__corrida = 0 #fk

    def __init__(self,numeroReservacion, fechaReservacion, fechaLimitePago, cantidad_pasajeros, subtotal, iva, total, pasajero, corrida):
        self(numeroReservacion,fechaReservacion,fechaLimitePago,cantidad_pasajeros,subtotal,iva,total)
        self.__pasajero = pasajero #fk
        self.__corrida = corrida #fk
        
    #getters
    def getID(self):
        return self.__numeroReservacion
    
    def getFechaReservacion(self):
        return self.__fecha_reservacion

    def getFechaLimitePago(self):
        return self.__fecha_limite_pago
    
    def getCantPasajeros(self):
        return self.__cantidad_pasajeros
    
    def getSubtotal(self):
        return self.__subtotal
    
    def getTotal(self):
        return self.__total
    
    def getIVA(self):
        return self.__iva
    
    def getNumPasajero(self):
        return self.__pasajero
    
    def getNumCorrida(self):
        return self.__corrida


    #setters

    #def setFechaLimitePago(self,fecha):
    #    self.__fecha_limite_pago = fecha

    def setSubtotal(self, monto):
        self.__subtotal = monto

    def setTotal(self, montoTotal):
        self.__total = montoTotal

    def setIVA(self, iva):
        self.__iva = iva

    def setCantPasajeros(self, cantidad):
        self.__cantidad_pasajeros = cantidad


    def __str__(self):
        return (
            f"ID Reservación: {self.__numeroReservacion}\n"
            f"Fecha de Reservación: {self.__fecha_reservacion}\n"
            f"Fecha Límite de Pago: {self.__fecha_limite_pago}\n"
            f"Subtotal: ${self.__subtotal:.2f}\n"
            f"IVA: ${self.__iva:.2f}\n"
            f"Total: ${self.__total:.2f}\n"
            f"Cantidad de Pasajeros: {self.__cantidad_pasajeros}"
        )