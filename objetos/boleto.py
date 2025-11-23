#Esta es la clase Boleto creada por Ruben Aguilar

class Boleto:

    def __init__(self, precio):
        self.__numeroBoleto = 0
        self.__precio = precio
        #self.__asiento = asiento FK
        #self.__tipo_pasajero = tipo_pasajero FK
        #self.__corrida = corrida FK

    #getters
    def getIDBoleto(self):
        return self.__numeroBoleto
    
    def getPrecio(self):
        return self.__precio


    #setters
    def setPrecio(self, precio):
        self.__precio = precio

    def __str__(self):
        return (
            f'ID Boleto: {self.__numeroBoleto}\n'
            f'Precio: ${self.__precio:.2f}'
        )