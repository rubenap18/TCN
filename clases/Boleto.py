#Esta es la clase Boleto creada por Ruben Aguilar

class Boleto:

    def __init__(self, idBoleto, importe):
        self.__idBoleto = idBoleto
        self.__importe = importe
    
    def getIDBoleto(self):
        return self.__idBoleto
    
    def getImporte(self):
        return self.__importe

    def setImporte(self, importe):
        self.__importe = importe

    def __str__(self):
        return f'ID boleto: {str(self.__idBoleto)} \nImporte: {str(self.__importe)}'