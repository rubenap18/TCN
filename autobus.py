def ListarAutobuses():
    while True:
        print("╔═══════════════════════════════════════════╗")
        print("║             AUTOBUSES ACTIVOS             ║")
        print("╠═══════════════════════════════════════════╣")
        print("║        Para regresar digite 0             ║")
        print("║        Autobús #104                       ║")
        print("║        Autobús #106                       ║")
        print("║        Autobús #502                       ║")
        print("║        Autobús #509                       ║")
        print("╚═══════════════════════════════════════════╝")
        consultaAutobus = int(input("Número de autobús a consultar: "))
    
        match consultaAutobus:
            case 0:
                print("╔═══════════════════════════════════════════╗")
                print("║               Regresando...               ║")
                print("╚═══════════════════════════════════════════╝")
                break
            case 104:
                opc1 = -1
                while opc1!=0:
                    print("╔═══════════════════════════════════════════╗")
                    print("║               AUTOBUS #104                ║")
                    print("╠═══════════════════════════════════════════╣")
                    print("║ Servicio: PLUS                            ║")
                    print("║ Asientos: 44                              ║")
                    print("║ Estado: ACTIVO                            ║")
                    print("║ Corridas asignadas: 02, 03, 04            ║")
                    print("╚═══════════════════════════════════════════╝")
                    opc1 = int(input("Para regresar digite 0: "))
            case 106:
                opc2 = -1
                while opc2!=0:
                    print("╔═══════════════════════════════════════════╗")
                    print("║               AUTOBUS #106                ║")
                    print("╠═══════════════════════════════════════════╣")
                    print("║ Servicio: PLUS                            ║")
                    print("║ Asientos: 44                              ║")
                    print("║ Estado: ACTIVO                            ║")
                    print("║ Corridas asignadas: 05, 06, 07            ║")
                    print("╚═══════════════════════════════════════════╝")
                    opc2 = int(input("Para regresar digite 0:"))
            case 502:
                opc3 = -1
                while opc3!=0:
                    print("╔═══════════════════════════════════════════╗")
                    print("║               AUTOBUS #502                ║")
                    print("╠═══════════════════════════════════════════╣")
                    print("║ Servicio: PLATINO                         ║")
                    print("║ Asientos: 36                              ║")
                    print("║ Estado: ACTIVO                            ║")
                    print("║ Corridas asignadas: 11, 12, 13            ║")
                    print("╚═══════════════════════════════════════════╝")
                    opc3 = int(input("Para regresar digite 0:"))
            case 509:
                opc4 = -1
                while opc4!=0:
                    print("╔═══════════════════════════════════════════╗")
                    print("║               AUTOBUS #509                ║")
                    print("╠═══════════════════════════════════════════╣")
                    print("║ Servicio: PLATINO                         ║")
                    print("║ Asientos: 36                              ║")
                    print("║ Estado: ACTIVO                            ║")
                    print("║ Corridas asignadas: 20, 21, 22            ║")
                    print("╚═══════════════════════════════════════════╝")
                    opc4 = int(input("Para regresar digite 0:"))
            case _:
                print("╔═══════════════════════════════════════════╗")
                print("║           Autobús inexistente             ║")
                print("╚═══════════════════════════════════════════╝")
              
def AsignarAutobus():
    numCorrida = -1
    
    while numCorrida != 0:
        print("╔═══════════════════════════════════════════╗")
        print("║          ASIGNAR AUTOBÚS A CORRIDA        ║")
        print("╚═══════════════════════════════════════════╝")
        numCorrida = int(input("Digite 0 para regresar\nDigite el numero de corrida: "))
        
        match numCorrida:
            case 0:
                print("╔═══════════════════════════════════════════╗")
                print("║               REGRESANDO.....             ║")
                print("╚═══════════════════════════════════════════╝")
            case 1:
                print("╔═══════════════════════════════════════════╗")
                print("║           LOCALIZANDO CORRIDA.....        ║")
                print("╠═══════════════════════════════════════════╣")
                print("║ CORRIDA: 01                               ║")
                print("║ RUTA: 01                                  ║")
                print("║ ORIGEN: TIJUANA                           ║")
                print("║ DESTINO: MEXICALI                         ║")
                print("║ HORA DE SALIDA: 12:00pm                   ║")
                print("║ HORA DE LLEGADA: 2:30pm                   ║")
                print("║ AUTOBUS: NO ASIGNADO                      ║")
                print("╚═══════════════════════════════════════════╝")
                numBus = int(input("Digite el numero de autobus a asignar: "))
                print("╔════════════════════════════════════════════════════════╗")
                print(f"║ Autobus #{numBus} asignado con éxito a la             ║")
                print(f"║ corrida #{numCorrida}                                 ║")
                print("╚════════════════════════════════════════════════════════╝")
            case 2:
                print("╔═══════════════════════════════════════════╗")
                print("║           LOCALIZANDO CORRIDA.....        ║")
                print("╠═══════════════════════════════════════════╣")
                print("║ ERROR. LA CORRIDA YA TIENE UN AUTOBÚS     ║")
                print("║               ASIGNADO                    ║")
                print("╠═══════════════════════════════════════════╣")
                print("║ CORRIDA: 02                               ║")
                print("║ RUTA: 01                                  ║")
                print("║ ORIGEN: TIJUANA                           ║")
                print("║ DESTINO: MEXICALI                         ║")
                print("║ HORA DE SALIDA: 2:00pm                    ║")
                print("║ HORA DE LLEGADA: 4:30pm                   ║")
                print("║ AUTOBUS: 502                              ║")
                print("╚═══════════════════════════════════════════╝")
            case _:
                print("╔═══════════════════════════════════════════╗")
                print("║        Numero de corrida inexistente      ║")
                print("╚═══════════════════════════════════════════╝")
                
def AgregarAutobus():
    print("╔═══════════════════════════════════════════╗")
    print("║           REGISTRAR NUEVO AUTOBUS         ║")
    print("╚═══════════════════════════════════════════╝")
    numAutobus = int(input("Numero de autobus: "))
    matricula = input("Matricula del autobus: ")
    tipoServicio = input("Tipo de servicio: ")
    numAsientos = int(input("Numero de asientos: "))
    print("╔═══════════════════════════════════════════════════╗")
    print("║              AUTOBUS REGISTRADO CON EXITO         ║")
    print("╠═══════════════════════════════════════════════════╣")
    print(f"║ Numero de autobus: {numAutobus}                  ║")
    print(f"║ Matricula: {matricula:<25}                       ║")
    print(f"║ Servicio: {tipoServicio:<26}                     ║")
    print(f"║ Numero de asientos: {numAsientos}                ║")
    print("╚═══════════════════════════════════════════════════╝")
    
def EliminarAutobus():
    print("╔═══════════════════════════════════════════╗")
    print("║              DAR DE BAJA AUTOBUS          ║")
    print("╚═══════════════════════════════════════════╝")
    numAutobus = int(input("Numero de autobus: "))
    print("╔═════════════════════════════════════════════════════╗")
    print(f"║ AUTOBUS #{numAutobus} DADO DE BAJA CON EXITO       ║")
    print("╚═════════════════════════════════════════════════════╝")