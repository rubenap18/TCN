#Este modulo fue creada por Ruben Aguilar
#Este modulo contiene las funciones del menu Boleto
import validaciones.val

def comprarBoleto():
    origen = input('▶ Ingresa el origen: ')
    destino = input('▶ Ingresa el destino: ')
    fecha = input('▶ Ingresa el dia de tu viaje: ')
    hora = input('▶ Ingresa la hora de tu viaje: ')
    cantidadPasajeros = input('▶ Ingresa la cantidad de boletos que compraras: ')

    #ahora se listan las corridas con sus boletos respectivos
    #autobuses plus o platino, horario, etc
    
    for i in range(1,int(cantidadPasajeros)+1):
        #mas adelante guardare datos en arreglos
        
        print(f"╔═════════════════════════════════╗")
        print(f"║      DATOS DEL PASAJERO {i}     ║")
        print(f"╚═════════════════════════════════╝")
        
        nPila = input(" ▶ Ingresa el nombre: ")
        apellidoPat = input(" ▶ Ingresa el apellido paterno: ")
        apellidoMat = input(" ▶ Ingresa el apellido materno (en caso de tenerlo): ")
        edad = input(' ▶ Ingresa la edad: ')
        correo = input(' ▶ Ingresa un correo electronico: ')
        telefono = input(' ▶ Ingresa un numero de telefono: ')
        asiento = input(' ▶ Elige el asiento del pasajero: ')
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║ Mostrando un menu o simulacion de eleccion de asiento...  ║")
        print("╚═══════════════════════════════════════════════════════════╝")
    
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║               Mostrando vista previa de todo...           ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print("╔═════════════════════════════════╗")
    print("║     PROCEDIENDO CON EL PAGO...  ║")
    print("╚═════════════════════════════════╝")
    imprimirConMarco('RESERVACION REALIZADA CON EXITO')
    imprimirConMarco('EN BREVE LLEGARAN LOS BOLETOS A LOS CORREOS ELECTRONICOS QUE SE PROPORCIONARON')

def localizarBoleto():
    nombre = input(' ▶ Ingresa nombre completo: ')
    edad = input(' ▶ Ingresa edad: ')
    origen = input(' ▶ Ingresa origen del viaje: ')
    destino = input(' ▶ Ingresa destino del viaje: ')
    imprimirConMarco("Mostrando posibles boletos del pasajero...")
    numBoleto = input(' ▶ Selecciona uno de los boletos: ')
    imprimirConMarco('Mostrando boleto del pasajero...')

#=====METODOS DE localizarBoleto()=========

def modificarDatosBoleto():
    print('      Ingresa los datos a modificar      ')
    print("╔═══════════════════════════════════════╗")
    print("║  1. ▶  Nombre                         ║")
    print("║  2. ▶  Fecha de nacimiento            ║")
    print("║  3. ▶  Correo Electronico             ║")
    print("║  4. ▶  Telefono                       ║")
    print("║  0. ▶  Regresar                       ║")
    print("╚═══════════════════════════════════════╝")

    opcion = int(input(" ▶  ELIGE UNA OPCION: "))
    match opcion:
        case 0:
            imprimirConMarco('Regresando...')
            menuOpcionesBoleto()
        case 1:
            imprimirConMarco('Aqui se modifica el nombre. En construccion...')
            modificarDatosBoleto()
        case 2:
            imprimirConMarco('Aqui se modifica la fecha de nacimiento. En construccion...')
            modificarDatosBoleto()
        case 3:
            imprimirConMarco('Aqui se modifica el correo. En construccion...')
            modificarDatosBoleto()
        case 4:
            imprimirConMarco('Aqui se modifica el telefono. En construccion...')
            modificarDatosBoleto()
        case _:
            imprimirConMarco('Opcion fuera de los limites. Intente de nuevo.')
            modificarDatosBoleto()


def cancelarBoleto():
    #Aqui se valida que no se pueda cancelar un boleto 24h antes de la corrida.s
    imprimirConMarco('Cancelando boleto...')
    imprimirConMarco('Cancelado con exito')
    imprimirConMarco('Inicia proceso de rembolso...')

def menuOpcionesBoleto():
    print("╔═══════════════════════════════════════╗")
    print("║  1. ▶  Modificar datos                ║")
    print("║  2. ▶  Cancelar boleto                ║")
    print("║  0. ▶  Regresar                       ║")
    print("╚═══════════════════════════════════════╝")

    opcion = int(input(" ▶  ELIGE UNA OPCION: "))
    match opcion:
        case 0:
            imprimirConMarco('Regresando...')
        case 1:
            modificarDatosBoleto()
        case 2:
            opcion = int(input('▶ Confirma cancelacion: 1)Si 2)No'))
            if opcion == 1:
                cancelarBoleto()
            else:
                imprimirConMarco("Cancelando accion")
                menuOpcionesBoleto()
        case _:
            imprimirConMarco('Opcion fuera de los limites. Intente de nuevo.')
            menuOpcionesBoleto()



def imprimirConMarco(mensaje):
    largo = len(mensaje) + 2  # espacio a los lados

    # Linea arriba
    print("╔" + "═" * largo + "╗")

    # Mensaje al centro
    print("║ " + mensaje + " ║")

    # Linea abajo
    print("╚" + "═" * largo + "╝")
