def dispAsiento():
    print("\n")
    print("* * * DISPONIBILIDAD DEL ASIENTO * * *")
    numAutobus = int(input("Numero de autobus: "))
    if numAutobus == 104:
        print("Autobus #"+str(numAutobus)+" localizado con éxito")
        numAsiento = int(input("Número de asiento: "))
        if numAsiento>0 and numAsiento<=20:
            print("ASIENTO #"+str(numAsiento))
            print("ESTADO: DISPONIBLE")
        elif numAsiento>20 and numAsiento<45:
            print("ASIENTO #"+str(numAsiento))
            print("ESTADO: OCUPADO")
        else:
            print("ASIENTO INEXISTENTE")
            
    elif numAutobus == 106:
        print("Autobus #"+str(numAutobus)+" localizado con éxito")
        numAsiento = int(input("Número de asiento: "))
        if numAsiento>0 and numAsiento<=20:
            print("ASIENTO #"+str(numAsiento))
            print("ESTADO: DISPONIBLE")
        elif numAsiento>20 and numAsiento<45:
            print("ASIENTO #"+str(numAsiento))
            print("ESTADO: OCUPADO")
        else:
            print("ASIENTO INEXISTENTE")
    elif numAutobus == 502:
        print("Autobus #"+str(numAutobus)+" localizado con éxito")
        numAsiento = int(input("Número de asiento: "))
        if numAsiento>0 and numAsiento<=20:
            print("ASIENTO #"+str(numAsiento))
            print("ESTADO: DISPONIBLE")
        elif numAsiento>20 and numAsiento<37:
            print("ASIENTO #"+str(numAsiento))
            print("ESTADO: OCUPADO")
        else:
            print("ASIENTO INEXISTENTE")
            
    elif numAutobus == 509:
        print("Autobus #"+str(numAutobus)+" localizado con éxito")
        numAsiento = int(input("Número de asiento: "))
        if numAsiento>0 and numAsiento<=20:
            print("ASIENTO #"+str(numAsiento))
            print("ESTADO: DISPONIBLE")
        elif numAsiento>20 and numAsiento<37:
            print("ASIENTO #"+str(numAsiento))
            print("ESTADO: OCUPADO")
        else:
            print("ASIENTO INEXISTENTE")
    else:
        print("AUTOBUS INEXISTENTE")
        
        
        
def datosOcupante():
    print("\n")
    print("* * * DATOS DEL OCUPANTE * * *")
    numAutobus = int(input("Numero de autobus: "))
    if numAutobus == 104:
        numAsiento = int(input("Número de asiento: "))
        match numAsiento:
            case 1:
                print("AUTOBUS #"+str(numAutobus))
                print("ASIENTO #"+str(numAsiento))
                print("Numero de reservacion: 1")
                print("Nombre: Hector Armando")
                print("Apellido paterno: Figueroa")
                print("Apellido materno: Orozco")
                print("Tipo de tarifa: NORMAL")
                print("Telefono: 6643638418")
                print("Correo electronico: hfigaorozco@gmail.com")
            case _:
                print("ASIENTO NO OCUPADO")
    elif numAutobus == 106:
        numAsiento = int(input("Número de asiento: "))
        match numAsiento:
            case 1:
                print("AUTOBUS #"+str(numAutobus))
                print("ASIENTO #"+str(numAsiento))
                print("Numero de reservacion: 2")
                print("Nombre: Leonardo")
                print("Apellido paterno: Ivan")
                print("Apellido materno: -----")
                print("Tipo de tarifa: NORMAL")
                print("Telefono: 664666000")
                print("Correo electronico: leowhite@gmail.com")
            case _:
                print("ASIENTO NO OCUPADO")
    elif numAutobus == 502:
        numAsiento = int(input("Número de asiento: "))
        match numAsiento:
            case 1:
                print("AUTOBUS #"+str(numAutobus))
                print("ASIENTO #"+str(numAsiento))
                print("Numero de reservacion: 3")
                print("Nombre: Ruben Alejandro")
                print("Apellido paterno: Aguilar")
                print("Apellido materno: Perez")
                print("Tipo de tarifa: CON DESCUENTO")
                print("Telefono: 6641112222")
                print("Correo electronico: rubenpuntual@gmail.com")
            case _:
                print("ASIENTO NO OCUPADO")
    elif numAutobus == 509:
        numAsiento = int(input("Número de asiento: "))
        match numAsiento:
            case 1:
                print("AUTOBUS #"+str(numAutobus))
                print("ASIENTO #"+str(numAsiento))
                print("Numero de reservacion: 4")
                print("Nombre: Juan Manuel")
                print("Apellido paterno: Hernandez")
                print("Apellido materno: Medina")
                print("Tipo de tarifa: CON DESCUENTO")
                print("Telefono: 6648887777")
                print("Correo electronico: juanitoalcachofa@gmail.com")
            case _:
                print("ASIENTO NO OCUPADO")
    else:
        print("AUTOBUS INEXISTENTE")
        

def bloquearAsiento():
    print("\n")
    print("* * * BLOQUEAR ASIENTO * * *")
    numAutobus = int(input("Numero de autobus: "))
    match numAutobus:
        case 104:
            print("AUTOBUS #"+str(numAutobus)+" localizado con exito")
            numCorrida = int(input("Digite el numero de corrida: "))
            match numCorrida:
                case 1:
                    print("Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito para la corrida #"+str(numCorrida))
                case 2:
                    print("Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito para la corrida #"+str(numCorrida))
                case _:
                    print("CORRIDA NO ASIGNADA AL AUTOBUS #"+str(numAutobus))
        case 106:
            print("AUTOBUS #"+str(numAutobus)+" localizado con exito")
            numCorrida = int(input("Digite el numero de corrida: "))
            match numCorrida:
                case 1:
                    print("Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito para la corrida #"+str(numCorrida))
                case 2:
                    print("Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito para la corrida #"+str(numCorrida))
                case _:
                    print("CORRIDA NO ASIGNADA AL AUTOBUS #"+str(numAutobus))
        case 502:
            print("AUTOBUS #"+str(numAutobus)+" localizado con exito")
            numCorrida = int(input("Digite el numero de corrida: "))
            match numCorrida:
                case 1:
                    print("Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito para la corrida #"+str(numCorrida))
                case 2:
                    print("Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito para la corrida #"+str(numCorrida))
                case _:
                    print("CORRIDA NO ASIGNADA AL AUTOBUS #"+str(numAutobus))
        case 509:
            print("AUTOBUS #"+str(numAutobus)+" localizado con exito")
            numCorrida = int(input("Digite el numero de corrida: "))
            match numCorrida:
                case 1:
                    print("Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito para la corrida #"+str(numCorrida))
                case 2:
                    print("Corrida #"+str(numCorrida)+" del autobus #"+str(numAutobus)+" localizada con éxito")
                    numAsiento = int(input("Asiento a bloquear: "))
                    print("Asiento #"+str(numAsiento)+" del autobus "+str(numAutobus)+" bloqueado con éxito para la corrida #"+str(numCorrida))
                case _:
                    print("CORRIDA NO ASIGNADA AL AUTOBUS #"+str(numAutobus))
        case _:
            print("AUTOBUS INEXISTENTE")