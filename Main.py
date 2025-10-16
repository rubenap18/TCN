import logo
import menu
import val
import Rutas
import Tarifas
#While que inicia todo

opcion = -1
opcBoletos = -1
opcReservaciones = -1
opcCorridas = -1
opcRutas = - 1
opcTarifas = -1
opcAutobuses = -1

logo.logo()

while opcion != 0:
  opcion = val.vOpciones(" ▶  ELIGE UNA OPCION: ",0 , 5, menu.mPrincipal)
  match opcion:
    case 0:
      print("╔═══════════════════════════════════════════╗")
      print("║      GRACIAS POR UTILIZAR EL PROGRAMA     ║")
      print("╚═══════════════════════════════════════════╝")
    case 1:
        pass
    
    case 2:
        pass  
      
    case 3:
      while opcRutas != 0:
            opcRutas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5 , menu.mRutas) #Llamando al MENU Corridas y tarifas
            match opcRutas:
                case 0:
                    print("╔═══════════════════════════════════════════╗")
                    print("║                REGRESANDO...              ║")
                    print("╚═══════════════════════════════════════════╝")
                case 1:
                    Rutas.CRutas()
                    
                case 2:
                    Rutas.ARuta()
                case 3:  
                    menu.mTarifas() 
                    while opcTarifas != 0:
                        opcTarifas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5 , menu.mRutas) #Llamando al MENU Corridas y tarifas
                        match opcTarifas:
                            case 0:
                                print("╔═══════════════════════════════════════════╗")
                                print("║                REGRESANDO...              ║")
                                print("╚═══════════════════════════════════════════╝")
                            case 1:
                                Tarifas.CTarifas()
                                
                            case 2:
                                Tarifas.ATarifa()
                            case 3:   
                                Rutas.Eruta()
                                                       
    case 4:
        while opcRutas != 0:
            opcRutas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5 , menu.mRutas) #Llamando al MENU Corridas y tarifas
            match opcRutas:
                case 0:
                    print("╔═══════════════════════════════════════════╗")
                    print("║                REGRESANDO...              ║")
                    print("╚═══════════════════════════════════════════╝")
                case 1:
                    Rutas.CRutas()
                    
                case 2:
                    Rutas.ARuta()
                case 3:   
                    Rutas.Eruta()
                
                    print("╚═══════════════════════════════════════╝")
        
    case 5:
        opcAutobuses = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5, menu.mAutobuses) #Llamando al MENU Autobes
        while opcAutobuses!=0:
            match opcAutobuses:
                case 0:
                    print("╔═══════════════════════════════════════════╗")
                    print("║                REGRESANDO...              ║")
                    print("╚═══════════════════════════════════════════╝")
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass                     

