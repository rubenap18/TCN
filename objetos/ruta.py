class Ruta:

    #Atributos y constructor
    def __init__(self,codigo_ruta ,distancia ,origen,destino,):
        self.__codigo_ruta = codigo_ruta
        self.__distancia = distancia
        self.__origen = origen #FK
        self.__destino = destino #FK
        
    def __str__(self):
        return f"ID Ruta: {self.__codigo_ruta} \nOrigen: {self.__origen} \nDestino:{self.__destino}  \nDistancia: {self.__distancia} km "
    
    def getidruta(self):
        return self.__codigo_ruta
    
    def setidruta(self, idruta):
        self.__codigo_ruta = idruta
    
    def getorigen(self):
        return self.__origen
    def setorigen(self,origen):
        self.__origen = origen
    
    def getdestino(self):
        return self.__destino
    def setdestino(self, destino):
        self.__destino = destino
    
    
    def getdistancia(self):
        return self.__distancia
    
    def setdistancia(self, distancia):
        self.__distancia = distancia
