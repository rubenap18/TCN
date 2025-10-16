import logo
import menu
import val
import autobus
import asientos


opcion = -1
opcBoletos = -1
opcReservaciones = -1
opcCorridas = -1
opcRutas = - 1
opcTarifas = -1
opcAutobuses = -1
opcAsientos = -1

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
      opcCorridas = -1  
      while opcCorridas != 0:
        opcCorridas = val.vOpciones(" ▶  ELIGE UNA OPCION: ", 0, 5 , menu.mCorridas) 
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
        opcRutas = -1  
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