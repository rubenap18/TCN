import logo 
import menu
import val
import autobus 
import asientos 
import fBoleto 
import funciones_reservacion 
import corridas 
import rutas 
import tarifas 

opcion = -1
opcBoletos = -1
opcReservaciones = -1
opcCorridas = -1
opcRutas = - 1
opcTarifas = -1
opcAutobuses = -1
opcAsientos = -1

logo.mostrarLogo()

while opcion != 0:
    opcion = val.vOpciones(" ▶  ELIGE UNA OPCION: ",0 , 5, menu.mPrincipal)
    match opcion:
        case 0:
            print("╔═══════════════════════════════════════════╗")
            print("║      GRACIAS POR UTILIZAR EL PROGRAMA     ║")
            print("╚═══════════════════════════════════════════╝")

        case 1:
            while opcBoletos != 0:
                opcBoletos = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 4 , menu.mBoletos) #Llamando al MENU Corridas y tarifas
                match opcBoletos:
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        fBoleto.comprarBoleto()
                    case 2:
                        fBoleto.localizarBoleto()
                        fBoleto.menuOpcionesBoleto()
                    case 3:   
                        fBoleto.localizarBoleto()
                        fBoleto.modificarDatosBoleto()
                    case 4:
                        fBoleto.localizarBoleto()
                        opcion = int(input('▶ Confirma cancelacion: 1)Si 2)No'))
                        if opcion == 1:
                            fBoleto.cancelarBoleto()
                        else:
                            fBoleto.imprimirConMarco("Cancelando accion")
                            fBoleto.menuOpcionesBoleto()

        case 2:
            while opcReservaciones != 0:
                opcReservaciones = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 4 , menu.mReservacion) #Llamando al MENU Corridas y tarifas
                match opcReservaciones:
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        funciones_reservacion.verReservacionesActivas()
                    case 2:
                        funciones_reservacion.verReservacionesPasadas()
                    case 3:   
                        funciones_reservacion.cancelarReservacion()
                    case 4:
                        pass
                    case _:
                        funciones_reservacion.imprimirConMarco('Opcion invalida. Intente de nuevo.')

        case 3:
            while opcCorridas != 0:
                opcCorridas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5 , menu.mCorridas) #Llamando al MENU Corridas y tarifas
                match opcCorridas:
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")       
                    case 1:
                        corridas.consultCorridas()       
                    case 2:
                        corridas.consultPasajeros()  
                    case 3:  
                        menu.mTarifas() 
                        while opcTarifas != 0:
                            opcTarifas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 2, menu.mTarifas) 
                            match opcTarifas:
                                case 0:
                                    print("╔═══════════════════════════════════════════╗")
                                    print("║                REGRESANDO...              ║")
                                    print("╚═══════════════════════════════════════════╝")
                                case 1:
                                    tarifas.CTarifas() 
                                case 2:
                                    tarifas.mTarifa()        
                    case 4:
                        corridas.agregarCorrida()      
                    case 5:
                        corridas.elimCorrida()     
                    case _:
                        print("╔═══════════════════════════════════════════╗")
                        print("║     OPCION INVALIDA, INTENTA DE NUEVO     ║")
                        print("╚═══════════════════════════════════════════╝")

        case 4:
            while opcRutas != 0:
                opcRutas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 3, menu.mRutas) #Llamando al MENU Corridas y tarifas
                match opcRutas:
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        rutas.CRutas()

                    case 2:
                        rutas.ARuta()

                    case 3:   
                        rutas.Eruta()

        case 5:
            opcAutobuses = -1  
            while opcAutobuses != 0:
                opcAutobuses = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5, menu.mAutobuses) #Llamando al MENU Autobes
                match opcAutobuses:
                    case 0:
                        print("╔═══════════════════════════════════════════╗")
                        print("║                REGRESANDO...              ║")
                        print("╚═══════════════════════════════════════════╝")
                    case 1:
                        opcAsientos = -1
                        while opcAsientos != 0:
                            opcAsientos = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 3, menu.mAsientos)
                            match opcAsientos:
                                case 0:
                                    print("╔═══════════════════════════════════════════╗")
                                    print("║                REGRESANDO...              ║")
                                    print("╚═══════════════════════════════════════════╝")
                                case 1:
                                    asientos.dispAsiento()
                                case 2:
                                    asientos.datosOcupante()
                                case 3:
                                    asientos.bloquearAsiento()
                    case 2:
                        autobus.ListarAutobuses()
                    case 3:
                        autobus.AsignarAutobus()
                    case 4:
                        autobus.AgregarAutobus()
                    case 5:
                        autobus.EliminarAutobus()   