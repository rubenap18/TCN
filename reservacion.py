#Este modulo fue creada por Ruben Aguilar
#Este modulo contiene las funciones del menu Reservacion

def verReservacionesActivas():
    nCompleto = input(" ▶ Ingresa nombre completo: ")
    edad = input(' ▶ Ingresa edad: ')
    correo = input(' ▶ Ingresa un correo electronico: ')
    telefono = input(' ▶ Ingresa un numero de telefono: ')
    imprimirConMarco('Mostrando reservaciones activas del pasajero')
    

def verReservacionesPasadas():
    nCompleto = input(" ▶ Ingresa nombre completo: ")
    edad = input(' ▶ Ingresa edad: ')
    correo = input(' ▶ Ingresa un correo electronico: ')
    telefono = input(' ▶ Ingresa un numero de telefono: ')
    imprimirConMarco('Mostrando reservaciones pasadas del pasajero')

def cancelarReservacion():
    nombre = input(' ▶ Ingresa nombre completo: ')
    edad = input(' ▶ Ingresa edad: ')
    origen = input(' ▶ Ingresa origen del viaje: ')
    destino = input(' ▶ Ingresa destino del viaje: ')
    imprimirConMarco("Mostrando reservacion")
    opcion = int(input('▶ Confirmar cancelacion 1)Si 2)No: '))
    if opcion == 1:
        imprimirConMarco('Cancelando reservacion...')
        imprimirConMarco('Cancelado con exito')
    else:
        imprimirConMarco("Cancelando accion")


def imprimirConMarco(mensaje):
    largo = len(mensaje) + 2  # espacio a los lados

    # Linea arriba
    print("╔" + "═" * largo + "╗")

    # Mensaje al centro
    print("║ " + mensaje + " ║")

    # Linea abajo
    print("╚" + "═" * largo + "╝")

def getMensajeEntrada(msg):
    mensaje = ' ▶ ' + msg + ': '
    return mensaje