#Esta es la clase Boleto creada por Ruben Aguilar

class Boleto:

    def __init__(self, precio):
        self.__idBoleto = 0
        self.__precio = precio
    

    #getters
    def getIDBoleto(self):
        return self.__idBoleto
    
    def getPrecio(self):
        return self.__precio


    #setters
    def setPrecio(self, precio):
        self.__precio = precio

    def __str__(self):
        return (
            f'ID Boleto: {self.__idBoleto}\n'
            f'Precio: ${self.__precio:.2f}'
        )