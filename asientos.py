def dispAsiento():
    print("╔═══════════════════════════════════════════╗")
    print("║        DISPONIBILIDAD DEL ASIENTO         ║")
    print("╚═══════════════════════════════════════════╝")
    numAutobus = int(input("Numero de autobus: "))
    if numAutobus == 104:
        print("╔═══════════════════════════════════════════╗")
        print("║ Autobus #"+str(numAutobus)+" localizado con éxito     ║")
        print("╚═══════════════════════════════════════════╝")
        numAsiento = int(input("Número de asiento: "))
        if numAsiento>0 and numAsiento<=20:
            print("╔═══════════════════════════════════════════╗")
            print("║ ASIENTO #"+str(numAsiento)+"                           ║")
            print("║ ESTADO: DISPONIBLE                       ║")
            print("╚═══════════════════════════════════════════╝")
        elif numAsiento>20 and numAsiento<45:
            print("╔═══════════════════════════════════════════╗")
            print("║ ASIENTO #"+str(numAsiento)+"                           ║")
            print("║ ESTADO: OCUPADO                          ║")
            print("╚═══════════════════════════════════════════╝")
        else:
            print("╔═══════════════════════════════════════════╗")
            print("║           ASIENTO INEXISTENTE             ║")
            print("╚═══════════════════════════════════════════╝")
            
    elif numAutobus == 106:
        print("╔═══════════════════════════════════════════╗")
        print("║ Autobus #"+str(numAutobus)+" localizado con éxito     ║")
        print("╚═══════════════════════════════════════════╝")
        numAsiento = int(input("Número de asiento: "))
        if numAsiento>0 and numAsiento<=20:
            print("╔═══════════════════════════════════════════╗")
            print("║ ASIENTO #"+str(numAsiento)+"                           ║")
            print("║ ESTADO: DISPONIBLE                       ║")
            print("╚═══════════════════════════════════════════╝")
        elif numAsiento>20 and numAsiento<45:
            print("╔═══════════════════════════════════════════╗")
            print("║ ASIENTO #"+str(numAsiento)+"                           ║")
            print("║ ESTADO: OCUPADO                          ║")
            print("╚═══════════════════════════════════════════╝")
        else:
            print("╔═══════════════════════════════════════════╗")
            print("║           ASIENTO INEXISTENTE             ║")
            print("╚═══════════════════════════════════════════╝")
    elif numAutobus == 502:
        print("╔═══════════════════════════════════════════╗")
        print("║ Autobus #"+str(numAutobus)+" localizado con éxito     ║")
        print("╚═══════════════════════════════════════════╝")
        numAsiento = int(input("Número de asiento: "))
        if numAsiento>0 and numAsiento<=20:
            print("╔═══════════════════════════════════════════╗")
            print("║ ASIENTO #"+str(numAsiento)+"                           ║")
            print("║ ESTADO: DISPONIBLE                       ║")
            print("╚═══════════════════════════════════════════╝")
        elif numAsiento>20 and numAsiento<37:
            print("╔═══════════════════════════════════════════╗")
            print("║ ASIENTO #"+str(numAsiento)+"                           ║")
            print("║ ESTADO: OCUPADO                          ║")
            print("╚═══════════════════════════════════════════╝")
        else:
            print("╔═══════════════════════════════════════════╗")
            print("║           ASIENTO INEXISTENTE             ║")
            print("╚═══════════════════════════════════════════╝")
            
    elif numAutobus == 509:
        print("╔═══════════════════════════════════════════╗")
        print("║ Autobus #"+str(numAutobus)+" localizado con éxito     ║")
        print("╚═══════════════════════════════════════════╝")
        numAsiento = int(input("Número de asiento: "))
        if numAsiento>0 and numAsiento<=20:
            print("╔═══════════════════════════════════════════╗")
            print("║ ASIENTO #"+str(numAsiento)+"                           ║")
            print("║ ESTADO: DISPONIBLE                       ║")
            print("╚═══════════════════════════════════════════╝")
        elif numAsiento>20 and numAsiento<37:
            print("╔═══════════════════════════════════════════╗")
            print("║ ASIENTO #"+str(numAsiento)+"                           ║")
            print("║ ESTADO: OCUPADO                          ║")
            print("╚═══════════════════════════════════════════╝")
        else:
            print("╔═══════════════════════════════════════════╗")
            print("║           ASIENTO INEXISTENTE             ║")
            print("╚═══════════════════════════════════════════╝")
    else:
        print("╔═══════════════════════════════════════════╗")
        print("║           AUTOBUS INEXISTENTE             ║")
        print("╚═══════════════════════════════════════════╝")
        
        
def datosOcupante():
    print("╔═══════════════════════════════════════════╗")
    print("║             DATOS DEL OCUPANTE            ║")
    print("╚═══════════════════════════════════════════╝")
    numAutobus = int(input("Numero de autobus: "))
    if numAutobus == 104:
        numAsiento = int(input("Número de asiento: "))
        match numAsiento:
            case 1:
                print("╔═══════════════════════════════════════════════════╗")
                print("║ AUTOBUS #"+str(numAutobus)+"                      ║")
                print("║ ASIENTO #"+str(numAsiento)+"                      ║")
                print("╠═══════════════════════════════════════════════════╣")
                print("║ Numero de reservacion: 1                          ║")
                print("║ Nombre: Hector Armando                            ║")
                print("║ Apellido paterno: Figueroa                        ║")
                print("║ Apellido materno: Orozco                          ║")
                print("║ Tipo de tarifa: NORMAL                            ║")
                print("║ Telefono: 6643638418                              ║")
                print("║ Correo electronico: hfigaorozco@gmail.com         ║")
                print("╚═══════════════════════════════════════════════════╝")
            case _:
                print("╔═══════════════════════════════════════════╗")
                print("║           ASIENTO NO OCUPADO              ║")
                print("╚═══════════════════════════════════════════╝")
    elif numAutobus == 106:
        numAsiento = int(input("Número de asiento: "))
        match numAsiento:
            case 1:
                print("╔════════════════════════════════════════════════════╗")
                print("║ AUTOBUS #"+str(numAutobus)+"                       ║")
                print("║ ASIENTO #"+str(numAsiento)+"                       ║")
                print("╠════════════════════════════════════════════════════╣")
                print("║ Numero de reservacion: 2                           ║")
                print("║ Nombre: Leonardo                                   ║")
                print("║ Apellido paterno: Ivan                             ║")
                print("║ Apellido materno: -----                            ║")
                print("║ Tipo de tarifa: NORMAL                             ║")
                print("║ Telefono: 664666000                                ║")
                print("║ Correo electronico: leowhite@gmail.com             ║")
                print("╚════════════════════════════════════════════════════╝")
            case _:
                print("╔═══════════════════════════════════════════╗")
                print("║           ASIENTO NO OCUPADO              ║")
                print("╚═══════════════════════════════════════════╝")
    elif numAutobus == 502:
        numAsiento = int(input("Número de asiento: "))
        match numAsiento:
            case 1:
                print("╔═══════════════════════════════════════════════════╗")
                print("║ AUTOBUS #"+str(numAutobus)+"                      ║")
                print("║ ASIENTO #"+str(numAsiento)+"                      ║")
                print("╠═══════════════════════════════════════════════════╣")
                print("║ Numero de reservacion: 3                          ║")
                print("║ Nombre: Ruben Alejandro                           ║")
                print("║ Apellido paterno: Aguilar                         ║")
                print("║ Apellido materno: Perez                           ║")
                print("║ Tipo de tarifa: CON DESCUENTO                     ║")
                print("║ Telefono: 6641112222                              ║")
                print("║ Correo electronico: rubenpuntual@gmail.com        ║")
                print("╚═══════════════════════════════════════════════════╝")
            case _:
                print("╔═══════════════════════════════════════════╗")
                print("║           ASIENTO NO OCUPADO              ║")
                print("╚═══════════════════════════════════════════╝")
    elif numAutobus == 509:
        numAsiento = int(input("Número de asiento: "))
        match numAsiento:
            case 1:
                print("╔════════════════════════════════════════════════════╗")
                print("║ AUTOBUS #"+str(numAutobus)+"                       ║")
                print("║ ASIENTO #"+str(numAsiento)+"                       ║")
                print("╠════════════════════════════════════════════════════╣")
                print("║ Numero de reservacion: 4                           ║")
                print("║ Nombre: Juan Manuel                                ║")
                print("║ Apellido paterno: Hernandez                        ║")
                print("║ Apellido materno: Medina                           ║")
                print("║ Tipo de tarifa: CON DESCUENTO                      ║")
                print("║ Telefono: 6648887777                               ║")
                print("║ Correo electronico: juanitoalcachofa@gmail.com     ║")
                print("╚════════════════════════════════════════════════════╝")
            case _:
                print("╔═══════════════════════════════════════════╗")
                print("║           ASIENTO NO OCUPADO              ║")
                print("╚═══════════════════════════════════════════╝")
    else:
        print("╔═══════════════════════════════════════════╗")
        print("║           AUTOBUS INEXISTENTE             ║")
        print("╚═══════════════════════════════════════════╝")
        

def bloquearAsiento():
    print("╔═══════════════════════════════════════════╗")
    print("║                BLOQUEAR ASIENTO           ║")
    print("╚═══════════════════════════════════════════╝")
    numAutobus = int(input("Numero de autobus: "))
    match numAutobus:
        case 104:
            print("╔══════════════════════════════════════════════════════╗")
            print("║ AUTOBUS #"+str(numAutobus)+" localizado con exito    ║")
            print("╚══════════════════════════════════════════════════════╝")
            numCorrida = int(input("Digite el numero de corrida: "))
            match numCorrida:
                case 1:
                    print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito║")
                    print("╚═══════════════════════════════════════════════════════════════════════════════════╝")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("╔══════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito ║")
                    print("║ para la corrida #"+str(numCorrida)+"                                             ║")
                    print("╚══════════════════════════════════════════════════════════════════════════════════╝")
                case 2:
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito  ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("╔══════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito ║")
                    print("║ para la corrida #"+str(numCorrida)+"                                             ║")
                    print("╚══════════════════════════════════════════════════════════════════════════════════╝")
                case _:
                    print("╔═══════════════════════════════════════════════════════╗")
                    print("║ CORRIDA NO ASIGNADA AL AUTOBUS #"+str(numAutobus)+"   ║")
                    print("╚═══════════════════════════════════════════════════════╝")
        case 106:
            print("╔══════════════════════════════════════════════════════╗")
            print("║ AUTOBUS #"+str(numAutobus)+" localizado con exito    ║")
            print("╚══════════════════════════════════════════════════════╝")
            numCorrida = int(input("Digite el numero de corrida: "))
            match numCorrida:
                case 1:
                    print("╔════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito ║")
                    print("╚════════════════════════════════════════════════════════════════════════════════════╝")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("╔════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito   ║")
                    print("║ para la corrida #"+str(numCorrida)+"                                               ║")
                    print("╚════════════════════════════════════════════════════════════════════════════════════╝")
                case 2:
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito  ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito  ║")
                    print("║ para la corrida #"+str(numCorrida)+"                                              ║")
                    print("╚═══════════════════════════════════════════════════════════════════════════════════╝")
                case _:
                    print("╔═════════════════════════════════════════════════════════╗")
                    print("║ CORRIDA NO ASIGNADA AL AUTOBUS #"+str(numAutobus)+"     ║")
                    print("╚═════════════════════════════════════════════════════════╝")
        case 502:
            print("╔═════════════════════════════════════════════════════════╗")
            print("║ AUTOBUS #"+str(numAutobus)+" localizado con exito       ║")
            print("╚═════════════════════════════════════════════════════════╝")
            numCorrida = int(input("Digite el numero de corrida: "))
            match numCorrida:
                case 1:
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito  ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito    ║")
                    print("║ para la corrida #"+str(numCorrida)+"                                                ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                case 2:
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito  ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito    ║")
                    print("║ para la corrida #"+str(numCorrida)+"                                                ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                case _:
                    print("╔═════════════════════════════════════════════════════════╗")
                    print("║ CORRIDA NO ASIGNADA AL AUTOBUS #"+str(numAutobus)+"     ║")
                    print("╚═════════════════════════════════════════════════════════╝")
        case 509:
            print("╔═════════════════════════════════════════════════════════╗")
            print("║ AUTOBUS #"+str(numAutobus)+" localizado con exito       ║")
            print("╚═════════════════════════════════════════════════════════╝")
            numCorrida = int(input("Digite el numero de corrida: "))
            match numCorrida:
                case 1:
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito  ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito    ║")
                    print("║ para la corrida #"+str(numCorrida)+"                                                ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                case 2:
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito  ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                    print("║ Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito    ║")
                    print("║ para la corrida #"+str(numCorrida)+"                                                ║")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                case _:
                    print("╔═════════════════════════════════════════════════════════╗")
                    print("║ CORRIDA NO ASIGNADA AL AUTOBUS #"+str(numAutobus)+"     ║")
                    print("╚═════════════════════════════════════════════════════════╝")
        case _:
            print("╔═══════════════════════════════════════════╗")
            print("║           AUTOBUS INEXISTENTE             ║")
            print("╚═══════════════════════════════════════════╝")