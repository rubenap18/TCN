def ListarAutobuses():
    while True:
        print("\n")
        print("* * * AUTOBUSES ACTIVOS * * *")
        print("Para regresar digite 0")
        print("Autobús #104")
        print("Autobús #106")
        print("Autobús #502")
        print("Autobús #509")
        consultaAutobus = int(input("Número de autobús a consultar: "))
    
        match consultaAutobus:
            case 0:
                print("\n")
                print("Regresando...")
                break
            case 104:
                opc1 = -1
                while opc1!=0:
                    print("\n")
                    print("AUTOBUS #104")
                    print("Servicio: PLUS")
                    print("Asientos: 44")
                    print("Estado: ACTIVO")
                    print("Corridas asignadas: 02, 03, 04")
                    opc1 = int(input("Para regresar digite 0: "))
            case 106:
                opc2 = -1
                while opc2!=0:
                    print("\n")
                    print("AUTOBUS #106")
                    print("Servicio: PLUS")
                    print("Asientos: 44")
                    print("Estado: ACTIVO")
                    print("Corridas asignadas: 05, 06, 07")
                    opc2 = int(input("Para regresar digite 0:"))
            case 502:
                opc3 = -1
                while opc3!=0:
                    print("\n")
                    print("AUTOBUS #502")
                    print("Servicio: PLATINO")
                    print("Asientos: 36")
                    print("Estado: ACTIVO")
                    print("Corridas asignadas: 11, 12, 13")
                    opc3 = int(input("Para regresar digite 0:"))
            case 509:
                opc4 = -1
                while opc4!=0:
                    print("\n")
                    print("AUTOBUS #509")
                    print("Servicio: PLATINO")
                    print("Asientos: 36")
                    print("Estado: ACTIVO")
                    print("Corridas asignadas: 20, 21, 22")
                    opc4 = int(input("Para regresar digite 0:"))
            case _:
                print("Autobús inexistente")
              
              
                
def AsignarAutobus():
    numCorrida = -1
    
    while numCorrida != 0:
        print("\n")
        numCorrida = int(input("Digite 0 para regresar\nDigite el numero de corrida: "))
        print("\n")
        
        match numCorrida:
            case 0:
                print("REGRESANDO.....")
                print("\n")
            case 1:
                print("LOCALIZANDO CORRIDA.....")
                print("CORRIDA: 01")
                print("RUTA: 01")
                print("ORIGEN: TIJUANA")
                print("DESTINO: MEXICALI")
                print("HORA DE SALIDA: 12:00pm")
                print("HORA DE LLEGADA: 2:30pm")
                print("AUTOBUS: NO ASIGNADO")
                numBus = int(input("Digite el numero de autobus a asignar: "))
                print("Autobus #"+str(numBus)+" asignado con éxito a la corrida #"+str(numCorrida))
            case 2:
                print("LOCALIZANDO CORRIDA.....")
                print("ERROR. LA CORRIDA YA TIENE UN AUTOBÚS ASIGNADO")
                print("CORRIDA: 02")
                print("RUTA: 01")
                print("ORIGEN: TIJUANA")
                print("DESTINO: MEXICALI")
                print("HORA DE SALIDA: 2:00pm")
                print("HORA DE LLEGADA: 4:30pm")
                print("AUTOBUS: 502")
            case _:
                print("Numero de corrida inexistente")
                
def AgregarAutobus():
    print("\n")
    print("* * * AREGISTRAR NUEVO AUTOBUS * * *")
    numAutobus = int(input("Numero de autobus: "))
    matricula = input("Matricula del autobus: ")
    tipoServicio = input("Tipo de servicio: ")
    numAsientos = int(input("Numero de asientos: "))
    print("\n")
    print("AUTOBUS REGISTRADO CON EXITO")
    print("Numero de autobus: "+str(numAutobus))
    print("Matricula: "+matricula)
    print("Servicio: "+tipoServicio)
    print("Numero de asientos: "+str(numAsientos))
    
def EliminarAutobus():
    print("\n")
    print("* * * DAR DE BAJA AUTOBUS * * *")
    numAutobus = int(input("Numero de autobus: "))
    print("\n")
    print("AUTOBUS #"+str(numAutobus)+" DADO DE BAJA CON EXITO")