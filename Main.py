import logo
import menu
import val

#While que inicia todo
opcion = -1
opcRutas = -1
opcCorridas = -1
opcAutobuses = -1
opcAsientos = -1
opcBoleto = -1
opcReservacion = -1
opcPasajeros = -1
opcTarifa = -1

logo.logo()

while opcion != 0:  
    opcion = val.vOpciones(" ▶  ELIGE UNA OPCION: ",0 , 8, menu.mPrincipal) #Llamando al MENU PRINCIPAL
    match opcion: 
        case 0:
            print("╔═══════════════════════════════════════════╗")
            print("║      GRACIAS POR UTILIZAR EL PROGRAMA     ║")
            print("╚═══════════════════════════════════════════╝")
        case 1:
            while opcRutas != 0:
                opcRutas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5 , menu.mRutas) #Llamando al MENU RUTAS
                match opcRutas:
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        print("╔═══════════════════════════════════════════╗")
                        print("║Aquí se podrá revisar o consultar las rutas║")
                        print("║ disponibles (solo incluirá origen y       ║")
                        print("║ destino)                                  ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 2:
                        print("╔═══════════════════════════════════════════╗")
                        print("║Aquí se podrá agregar una ruta nueva       ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 3:
                        print("╔═══════════════════════════════════════════╗")
                        print("║Aquí se va a poder consultar o ver las     ║")
                        print("║escalas de cada ruta por medio del número  ║")
                        print("║o clave de ruta                            ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 4:
                        print("╔═══════════════════════════════════════════╗")
                        print("║Aquí se van a poder cambiar las escalas de ║")
                        print("║una ruta                                   ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 5:
                        print("╔═══════════════════════════════════════════╗")
                        print("║Aquí se va a poder borrar las rutas antes  ║")
                        print("║establecidas                               ║")
                        print("╚═══════════════════════════════════════════╝")
                    case _:
                        print("╔═══════════════════════════════════════════╗")
                        print("║     OPCION INVALIDA, INTENTA DE NUEVO     ║")
                        print("╚═══════════════════════════════════════════╝")
                    
        case 2:
            while opcCorridas != 0:
                opcCorridas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 3, menu.mCorridas)
                match opcCorridas:
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        print("╔═══════════════════════════════════════════╗")
                        print("║Aquí se van a poder ver o consultar todas  ║")
                        print("║las corridas establecidas                  ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 2:
                        print("╔═══════════════════════════════════════════╗")
                        print("║Aquí se va a poder agregar una nueva       ║")
                        print("║corrida                                    ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 3:
                        print("╔═══════════════════════════════════════════╗")
                        print("║Aquí se va a poder eliminar corridas       ║")
                        print("║ya existentes                              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case _:
                        print("╔═══════════════════════════════════════════╗")
                        print("║     OPCION INVALIDA, INTENTA DE NUEVO     ║")
                        print("╚═══════════════════════════════════════════╝")
                        
        case 3:
            while opcAutobuses != 0:
                opcAutobuses = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 4, menu.mAutobuses)
                match opcAutobuses: 
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 2:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 3:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 4:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case _:
                        print("╔═══════════════════════════════════════════╗")
                        print("║     OPCION INVALIDA, INTENTA DE NUEVO     ║")
                        print("╚═══════════════════════════════════════════╝")
                        
        case 4:
            while opcAsientos != 0:
                opcAsientos = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 3, menu.mAsientos)
                match opcAsientos:
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 2:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 3:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case _:
                        print("╔═══════════════════════════════════════════╗")
                        print("║     OPCION INVALIDA, INTENTA DE NUEVO     ║")
                        print("╚═══════════════════════════════════════════╝")
        
        case 5:
            while opcBoleto != 0:
                opcBoleto = val.vOpciones("\n ▶  ELIGE UNA OPCION: ", 0, 3, menu.mBoletos)
                match opcBoleto: 
                    case 0:
                        print("╔═══════════════════════════════════════╗")
                        print("║               REGRESANDO...           ║")
                        print("╚═══════════════════════════════════════╝")
                    case 1:
                        print("╔═══════════════════════════════════════╗")
                        print("║            EN CONSTRUCCION...         ║")
                        print("╚═══════════════════════════════════════╝")
                    case 2:
                        print("╔═══════════════════════════════════════╗")
                        print("║            EN CONSTRUCCION...         ║")
                        print("╚═══════════════════════════════════════╝")
                    case 3:
                        print("╔═══════════════════════════════════════╗")
                        print("║            EN CONSTRUCCION...         ║")
                        print("╚═══════════════════════════════════════╝")
                    case _:
                        print("╔═══════════════════════════════════════╗")
                        print("║   OPCION INVALIDA, INTENTA DE NUEVO   ║")
                        print("╚═══════════════════════════════════════╝")
                        
        case 6:
            while opcReservacion != 0:
                opcReservacion = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 4, menu.mReservacion)
                match opcReservacion: 
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 2:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 3:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 4:
                        print("╔═══════════════════════════════════════════╗")
                        print("║              EN CONSTRUCCION...           ║")
                        print("╚═══════════════════════════════════════════╝")
                    case _:
                        print("╔═══════════════════════════════════════════╗")
                        print("║     OPCION INVALIDA, INTENTA DE NUEVO     ║")
                        print("╚═══════════════════════════════════════════╝")

        case 7:
            while opcPasajeros != 0:
                opcPasajeros = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 4, menu.mPasajeros)
                match opcPasajeros: 
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        print("╔════════════════════════════════════════════════════════════════════════════════╗")
                        print("║ Aqui podras consultar datos importantes sobre el pasajero como nombre compreto ║")
                        print("║ fecha de nacimiento y contacto                                                 ║")
                        print("╚════════════════════════════════════════════════════════════════════════════════╝")
                    case 2:
                        print("╔═════════════════════════════════════════════════════════════════════════════════╗")
                        print("║ Esta opcion permite registrar a un pasajero  manualmente y asi ayudandole para  ║")
                        print("║ generar su boleto                                                               ║")
                        print("╚═════════════════════════════════════════════════════════════════════════════════╝")
                    case 3:
                        print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                        print("║ Aquí puedes modificar los datos del pasajero cuando sea necesario                   ║")
                        print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                    case 4:
                        print("╔════════════════════════════════════════════════════════════════════════════════╗")
                        print("║ Esta opcion permite  eliminar los pasajaros, ten en cuenta que todos los datos ║")
                        print("║ seran eliminados                                                               ║")
                        print("╚════════════════════════════════════════════════════════════════════════════════╝")
                    case _:
                        print("╔═══════════════════════════════════════════╗")
                        print("║     OPCION INVALIDA, INTENTA DE NUEVO     ║")
                        print("╚═══════════════════════════════════════════╝")
                        
        case 8:
            while opcTarifa != 0:
                opcTarifa = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0 , 4, menu.mTarifas)
                match opcTarifa: 
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        print("╔════════════════════════════════════════════════════════════════════════════════╗")
                        print("║ Aqui podras consultar las difrentes tarifas viegentes tanto de los pasajeros   ║")
                        print("║ como el precio de diferetes rutas con sus repectivos tipo de autobus           ║")
                        print("╚════════════════════════════════════════════════════════════════════════════════╝")
                    case 2:
                        print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                        print("║ Aqui podras agregar una nueva tarifa a los pasajeros o colocar precio a un ruta   ║")
                        print("╚═══════════════════════════════════════════════════════════════════════════════════╝")
                    case 3:
                        print("╔═════════════════════════════════════════════════════════════════════════════════════╗")
                        print("║ Aquí puedes modificar los datos de la tarifa cuando sea necesario                   ║")
                        print("╚═════════════════════════════════════════════════════════════════════════════════════╝")
                    case 4:
                        print("╔════════════════════════════════════════════════════════════════════════════════╗")
                        print("║ Esta opcion permite  eliminar las tarifas, ten en cuenta que todos los datos ║")
                        print("║ seran eliminados                                                               ║")
                        print("╚════════════════════════════════════════════════════════════════════════════════╝")
                    case _:
                        print("╔═══════════════════════════════════════════╗")
                        print("║     OPCION INVALIDA, INTENTA DE NUEVO     ║")
                        print("╚═══════════════════════════════════════════╝")
                        
        case _:
            print("╔═══════════════════════════════════════════╗")
            print("║     OPCION INVALIDA, INTENTA DE NUEVO     ║")
            print("╚═══════════════════════════════════════════╝")

