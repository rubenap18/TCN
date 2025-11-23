# CLASE AUTOBUS

class Autobus:
    
    # Atributos
    __numAutobus = 0
    __matricula = ""
    __marca = ""
    __modelo = ""
    __tipoAutobus = ""
    __estado = ""
    __claveWIFI = ""
    __cantAsientos = 0
    #falta asientos disponibles
    
    
    # Constructor
    def __init__(self, numAutobus, matricula, claveWIFI, cantAsientos, tipoAutobus, estado, marca, modelo):
        self.__numAutobus = numAutobus
        self.__matricula = matricula
        self.__claveWIFI = claveWIFI
        self.__cantAsientos = cantAsientos
        self.__estado = estado
        self.__tipoAutobus = tipoAutobus
        self.__marca = marca 
        self.__modelo = modelo
    
    # toString
    def __str__(self):
        return f"* * * DATOS DEL NUEVO AUTOBÚS * * *\nNúmero de autobus: {self.__numAutobus}\nMatricula: {self.__matricula}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nServicio: {self.__tipoAutobus}\nClave WIFI: {self.__claveWIFI}\nAsientos: {self.__cantAsientos}\nEstado: {self.__estado}"
        
    # Getters
    def getNumAutobus(self):
        return self.__numAutobus
    
    def getMatricula(self):
        return self.__matricula
    
    def getClaveWIFI(self):
        return self.__claveWIFI
    
    def getCantAsientos(self):
        return self.__cantAsientos
    
    def getEstado(self):
        return self.__estado
    
    def getTipoAutobus(self):
        return self.__tipoAutobus
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    
    # Setters
    def setNumAutobus(self, numAutobus):
        self.__numAutobus = numAutobus
    
    def setMatricula(self, matricula):
        self.__matricula = matricula
        
    def setClaveWIFI(self, claveWIFI):
        self.__claveWIFI = claveWIFI
        
    def setCantAsientos(self, cantAsientos):
        self.__cantAsientos = cantAsientos
        
    def setEstado(self, estado):
        self.__estado = estado
        
    def setTipoAutobus(self, tipoAutobus):
        self.__tipoAutobus = tipoAutobus
        
    def setMarca(self, marca):
        self.__marca = marca
        
    def setModelo(self, modelo):
        self.__modelo = modelo      