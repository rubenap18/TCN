import logo
import menu
import val
#While que inicia todo

opcion = -1
opcBoletos = -1
opcReservaciones = -1
opcCorridas = -1
opcRutas = - 1
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
      while opcCorridas != 0:
        opcCorridas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5 , menu.mCorridas) #Llamando al MENU Corridas y tarifas
        while opcCorridas != 0:
            match opcCorridas:
                case 0:
                    print("╔═══════════════════════════════════════════╗")
                    print("║                REGRESANDO...              ║")
                    print("╚═══════════════════════════════════════════╝")
                case 1:
                    print("Consultar tarifas")
                case 2:
                    print("Consultar tarifas")    
                case 3:   
                    print("Consultar tarifas")
                case 4:
                    print("Consultar tarifas")
                case 5:
                    print("Consultar tarifas")
                                                       
    case 4:
        while opcRutas != 0:
            opcRutas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5 , menu.mRutas) #Llamando al MENU Corridas y tarifas
            match opcRutas:
                case 0:
                    print("╔═══════════════════════════════════════════╗")
                    print("║                REGRESANDO...              ║")
                    print("╚═══════════════════════════════════════════╝")
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
                case 4:
                    print("╔═══════════════════════════════════════╗")
                    print("║            EN CONSTRUCCION...         ║")
                    print("╚═══════════════════════════════════════╝")
                case 5:
                    print("╔═══════════════════════════════════════╗")
                    print("║            EN CONSTRUCCION...         ║")
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