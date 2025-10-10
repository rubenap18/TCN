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
            print("Gracias por utilizar el programa")
        case 1:
            while opcRutas != 0:
                opcRutas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5 , menu.mRutas) #Llamando al MENU RUTAS
                match opcRutas:
                    case 0:
                        print("Saliendo")
                    case 1:
                        print("En contrucción")
                    case 2:
                        print("En construcción")
                    case 3:
                        print("En construcción")
                    case 4:
                        print("En construcción")
                    case 5:
                        print("En construcción")
                    case _:
                        print("Opcion inválida. Vuelva a intentar.")
                    
        case 2:
            while opcCorridas != 0:
                opcCorridas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 3, menu.mCorridas)
                match opcCorridas:
                    case 0:
                        print("Saliendo")
                    case 1:
                        print("En construccion")
                    case 2:
                        print("En construccion")
                    case 3:
                        print("En construccion")
                    case _:
                        print("Opcion inválida. Vuelva a intentar.")
                        
        case 3:
            while opcAutobuses != 0:
                opcAutobuses = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 4, menu.mAutobuses)
                match opcAutobuses: 
                    case 0:
                        print("Saliendo")
                    case 1:
                        print("En construcción")
                    case 2:
                        print("En construcción")
                    case 3:
                        print("En construcción")
                    case 4:
                        print("En construcción")
                    case _:
                        print("Opcion inválida. Vuelva a intentar.")
                        
        case 4:
            while opcAsientos != 0:
                opcAsientos = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 3, menu.mAsientos)
                match opcAsientos:
                    case 0:
                        print("Saliendo") 
                    case 1:
                        print("En construcción")
                    case 2:
                        print("En construcción")
                    case 3:
                        print("En construcción")
                    case _:
                        print("Opcion inválida. Vuelva a intentar.")
        
        case 5:
            while opcBoleto != 0:
                opcBoleto = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 3, menu.mBoletos)
                match opcBoleto: 
                    case 0:
                        print("Saliendo")
                    case 1:
                        print("En contruccioin")
                    case 2:
                        print("En construccion")
                    case 3:
                        print("En construccion")
                    case _:
                        print("Opcion inválida. Vuelva a intentar.")
                        
        case 6:
            while opcReservacion != 0:
                opcReservacion = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 4, menu.mReservacion)
                match opcReservacion: 
                    case 0:
                        print("Saliendo")
                    case 1:
                        print("En contruccioin")
                    case 2:
                        print("En construccion")
                    case 3:
                        print("En construccion")
                    case 4:
                        print("En construccion")    
                    case _:
                        print("Opcion inválida. Vuelva a intentar.")

        case 7:
            while opcPasajeros != 0:
                opcPasajeros = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 4, menu.mPasajeros)
                match opcPasajeros: 
                    case 0:
                        print("Regresando")
                    case 1:
                        print("En contruccioin")
                    case 2:
                        print("En construccion")
                    case 3:
                        print("En construccion")
                    case 4:
                        print("En construcción")
                    case _:
                        print("Opcion inválida. Vuelva a intentar.")
                        
        case 8:
            while opcTarifa != 0:
                opcTarifa = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0 , 4, menu.mTarifas)
                match opcTarifa: 
                    case 0:
                        print("Regresando")
                    case 1:
                        print("En contruccioin")
                    case 2:
                        print("En construccion")
                    case 3:
                        print("En construccion")
                    case 4:
                        print("En construccion")
                    case _:
                        print("Opcion inválida. Vuelva a intentar.")
                        
        case _:
            print("Opcion inválida. Vuelva a intentar.")