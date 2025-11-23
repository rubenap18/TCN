
#Clase pasajeros by Leonardo Valdez
class Pasajero:
    
    __num = ""
    __nombrePila = ""
    __primerApell = ""
    __segApell = ""
    __fechaNacimiento = ""
    __edad = ""
    __correo = ""
    __telefono = ""
    
    def __init__(self, numeroPasajero, nombrePila, primerApell, segApell, fechaNacimiento, edad, correo, telefono):
        self.__num = numeroPasajero
        self.__nombrePila = nombrePila
        self.__primerApell = primerApell
        self.__segApell = segApell
        self.__fechaNacimiento = fechaNacimiento
        self.__edad = edad
        self.__telefono = telefono
        self.__correo = correo
        
    
    def __str__(self):
        return (f"Numero de pasajero: {self.__num}" + " Nombre de pila: " + self.__nombrePila + " Primer apellido: " 
                + self.__primerApell + " Segundo apellido: " + self.__segApell + " Fecha de nacimiento: " 
                + self.__fechaNacimiento + " Edad: " + self.__edad + " Telefono: " + self.__telefono
                + " Correo electronico: " + self.__correo + " Estado: " + self.__estado)
    
    def set_num(self, num):
        self.__num = num
    
    def set_nombrePila(self, nombrePila):
        self.__nombrePila = nombrePila
    
    def set_primerApell(self, primerApell):
        self.__primerApell = primerApell
    
    def set_segApell(self, segApell):
        self.__segApell = segApell
    
    def set_correo(self, fechaNacimiento):
        self.__correo = fechaNacimiento
    
    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def set_fechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento
        
    def set_edad(self, edad):
        self.__edad = edad
    
    def get_num(self):
        return self.__num
    
    def get_edad(self):
        return self.__edad
    
    def get_nombrePila(self):
        return self.__nombrePila
    
    def get_primerApell(self):
        return self.__primerApell
    
    def get_segApell(self):
        return self.__segApell
    
    def get_correo(self):
        return self.__correo
    
    def get_telefono(self):
        return self.__telefono
    
    def get_fechaNacimiento(self):
        return self.__fechaNacimiento