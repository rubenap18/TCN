#Modulo Controlador de Reservaciones
from reservacion import Reservacion
from datetime import date, datetime
import crudReservacion

import crudReservacion


#FUNCIONES CREATE/INSERTAR
def insertarReservacion(fechaR,fechaLimitePago,subtotal,total,iva,cantPasajeros):
    mi_reservacion = Reservacion(fechaR,fechaLimitePago,subtotal,total,iva,cantPasajeros)
    

eservacion = Reservacion(datetime.now())