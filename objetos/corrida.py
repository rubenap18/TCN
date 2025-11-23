from datetime import date, time

class Corrida:

    def __init__(self, codigo: str, fecha: date, hora_salida: time, hora_llegada: time, 
                tarifa_base: float, autobus: str, ruta: str, 
                operador: int, estado: str):
        
        # Atributos internos (privados o "protegidos" por convención)
        self._codigo = codigo
        self._fecha = fecha
        self._hora_salida = hora_salida
        self._hora_llegada = hora_llegada
        self._tarifa_base = tarifa_base
        #self._lugares_disp = lugares_disp
        self._autobus = autobus
        self._ruta = ruta
        self._operador = operador
        self._estado = estado

    def __repr__(self):
        return (f'Codigo: {self._codigo} | Fecha: {self._fecha}')


    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def fecha(self):
        return self._fecha

    @property
    def hora_salida(self):
        return self._hora_salida

    @property
    def hora_llegada(self):
        return self._hora_llegada

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @property
    def lugares_disp(self):
        return self._lugares_disp

    @property
    def autobus(self):
        return self._autobus

    @property
    def ruta(self):
        return self._ruta

    @property
    def operador(self):
        return self._operador

    @property
    def estado(self):
        return self._estado

    # Setters con validación
    @codigo.setter
    def codigo(self, nuevo_codigo):
        self._codigo = nuevo_codigo
        
    @fecha.setter
    def fecha(self, nueva_fecha):
        if not isinstance(nueva_fecha, date):
            raise TypeError("La fecha debe ser un objeto datetime.date.")
        self._fecha = nueva_fecha

    @tarifa_base.setter
    def tarifa_base(self, nueva_tarifa):
        if not isinstance(nueva_tarifa, (int, float)) or nueva_tarifa < 0:
            raise ValueError("La tarifa debe ser un numero positivo.")
        self._tarifa_base = nueva_tarifa

    '''@lugares_disp.setter
    def lugares_disp(self, nuevos_lugares):
        if not isinstance(nuevos_lugares, int) or nuevos_lugares < 0:
            raise ValueError("Los lugares disponibles deben ser un entero no negativo.")
        self._lugares_disp = nuevos_lugares'''

    @autobus.setter
    def autobus(self, nuevo_autobus):
        if not isinstance(nuevo_autobus, str) or len(nuevo_autobus) > 3:
            raise ValueError("El codigo de autobus debe ser una cadena de hasta 3 caracteres.")
        self._autobus = nuevo_autobus

    @ruta.setter
    def ruta(self, nueva_ruta):
        if not isinstance(nueva_ruta, str) or len(nueva_ruta) > 9:
            raise ValueError("El codigo de ruta debe ser una cadena de hasta 9 caracteres.")
        self._ruta = nueva_ruta

    @operador.setter
    def operador(self, nuevo_operador):
        if nuevo_operador is not None and (not isinstance(nuevo_operador, int) or nuevo_operador <= 0):
            raise ValueError("El operador debe ser un entero positivo o None.")
        self._operador = nuevo_operador

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado not in ['ACT', 'PRG', 'INA']:
            raise ValueError("El estado debe ser 'ACT', 'PRG' o 'INA'.")
        self._estado = nuevo_estado
