def consultCorridas():
    origenes = ["Tijuana", "Tecate", "Ensenada", "Mexicali", "Rosarito", "San Quintin", "San Felipe"]
    print("╔══════════════════════════════════════════╗")
    print("║Ingresa origen de las corridas a consultar║")
    print("╠══════════════════════════════════════════╣")
    print("║1. Tijuana                                ║")
    print("║2. Ensenada                               ║")
    print("║3. Rosarito                               ║")
    print("║4. Mexicali                               ║")
    print("║5. Tecate                                 ║")
    print("║6. San Felipe                             ║")
    print("║7. San Quintin                            ║")
    print("╚══════════════════════════════════════════╝")
    origen = int(input())
    if origen in origenes:
        match origen:
            case 1:
                print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
                print(F"║                                       CORRIDAS DESDE TIJUANA                                                         ║")
                print("╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
                print("║  ORIGEN     │ DESTINO   │ AUTOBÚS   │  Salida     │  LLegada    │ Fecha de salida   │ Fecha de llegada  │ No. corrida ║")
                print("╟─────────────┼───────────┼───────────┼─────────────┼─────────────┼───────────────────┼───────────────────┼─────────────╢")
                print("║  Tijuana    │ Mexicali  │ PLUS      │  07:00      │  9:00       │ 15/10/2025        │ 15/10/2025        │ 123456      ║")
                print("║  Tijuana    │ Ensenada  │ PLATINO   │  15:00      │  17:00      │ 15/10/2025        │ 15/10/2025        │ 654321      ║")
                print("║  Tijuana    │ Rosarito  │ PLUS      │  14:00      │  16:00      │ 15/10/2025        │ 15/10/2025        │ 612543      ║")
                print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def consultPasajeros():
    print("╔═══════════════════════════════════════╗")
    print("║Ingresa numero de corrida              ║")
    print("╚═══════════════════════════════════════╝")
    numCorrida = int(input())

def agregarCorrida():
    print("╔═══════════════════════════════════════╗")
    print("║Ingresa ciudad de origen               ║")
    print("╚═══════════════════════════════════════╝")
    origen = input()
    print("╔═══════════════════════════════════════╗")
    print("║Ingresa ciudad de destino              ║")
    print("╚═══════════════════════════════════════╝")
    destino = input()
    print("╔═══════════════════════════════════════╗")
    print("║Ingresa hora de salida                 ║")
    print("╚═══════════════════════════════════════╝")
    salida = input()
    print("╔═══════════════════════════════════════╗")
    print("║Ingresa hora de llegada                ║")
    print("╚═══════════════════════════════════════╝")
    llegada = input()
    print("╔═══════════════════════════════════════╗")
    print("║Ingresa tipo de autobus (PLUS/PLATINO) ║")
    print("╚═══════════════════════════════════════╝")
    tipoAutobus = input()
    print("Nueva corrida creada: ")
    print(f"""Origen: {origen}. 
Destino {destino}. 
Hora de salida: {salida} 
Hora de llegada: {llegada}
Tipo de autobus: {tipoAutobus}""")
    
    
    
def elimCorrida():
    print("╔═══════════════════════════════════════╗")
    print("║Ingresa numero de corrida a eliminar   ║")
    print("╚═══════════════════════════════════════╝")
    numCorrida = int(input())
    print("")
    print(f"Corrida {numCorrida} eliminada")
    
    

    
