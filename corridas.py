def consultCorridas():
    print("╔═══════════════════════════════════════╗")
    print("║Aqui se van a mostrar las corridas     ║")
    print("╚═══════════════════════════════════════╝")

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
    print("Nueva corrida creada: ")
    print(f"""Origen: {origen}. 
Destino {destino}. 
Hora de salida: {salida} 
Hora de llegada: {llegada}""")
    
    
    
def elimCorrida():
    print("╔═══════════════════════════════════════╗")
    print("║Ingresa numero de corrida a eliminar   ║")
    print("╚═══════════════════════════════════════╝")
    numCorrida = int(input())
    print("")
    print(f"Corrida {numCorrida} eliminada")
    
    
    