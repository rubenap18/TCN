#Sub menu rutas

# modulo_consultar_rutas.py

def CRutas():
    opcion = -1  # cualquier valor diferente de 0 para iniciar el ciclo

    while opcion != 0:
        print("\n=== Módulo: Consultar Rutas ===")
        print("1. Buscar ruta por destino")
        print("2. Buscar ruta por origen")
        print("3. Mostrar todas las rutas (simulada)")
        print("0. Salir")

        opcion = int(input("Elige una opción (0-3): "))
       

        match opcion:
            case 1:
                print("\nSeleccione su destino:")
                print("1) Tijuana")
                print("2) Tecate")
                opcdestino = int(input("Elige destino: "))
                

                match opcdestino:
                    case 1:
                        print("\nOrigen      DESTINO       HORA        AUTOBUS     PRECIO")
                        print("MEXICALI    TIJUANA       9:00am      PLUS           $200")
                        print("ENSENADA    TIJUANA       12:00pm     PLATINO        $200")
                        print("TECATE      TIJUANA       3:00pm      PLUS           $200")
                    case 2:
                        print("\nOrigen      DESTINO       HORA      AUTOBUS       PRECIO")
                        print("MEXICALI    TECATE        9:00am      PLUS           $200")
                        print("ENSENADA    TECATE        12:00pm     PLATINO        $200")
                        print("TIJUANA     TECATE        3:00pm      PLUS           $200")
                    case _:
                        print(" Escoge un destino válido.")
            
            case 2:
                print("\nSeleccione su origen:")
                print("1) Tijuana")
                print("2) Tecate")
                opcorigen = int(input("Elige origen: "))
                

                match opcorigen:
                    case 1:
                        print("\nOrigen      DESTINO       HORA      AUTOBUS   PRECIO")
                        print("TIJUANA    MEXICALI       9:00am      PLUS       $200")
                        print("TIJUANA    ENSENADA       12:00pm     PLATINO    $200")
                        print("TIJUANA    TECATE         3:00pm      PLUS       $200")
                    case 2:
                        print("\nOrigen      DESTINO       HORA      AUTOBUS   PRECIO")
                        print("TECATE     MEXICALI       9:00am      PLUS       $200")
                        print("TECATE     ENSENADA       12:00pm     PLATINO    $200")
                        print("TECATE     TIJUANA        3:00pm      PLUS       $200")
                    case _:
                        print(" Escoge un origen válido.")

            case 3:
                print("\nOrigen      DESTINO       HORA      AUTOBUS          PRECIO")
                print("TECATE     MEXICALI       9:00am      PLUS              $200")
                print("TECATE     ENSENADA       12:00pm     PLATINO           $300")
                print("TECATE     TIJUANA        3:00pm      PLATINO           $400")
                print("TIJUANA    TECATE         3:00pm      PLUS              $200")
                print("TIJUANA    MEXICALI       9:00am      PLUS              $300")

            case 0:
                print("\nSaliendo del módulo de consulta...")

            case _:
                print(" Opción no válida. Intenta de nuevo.")

           

def ARuta():
    print("\n=== Módulo: Agregar Rutas ===")
    print("\n--- Agregar nueva ruta ---")
    origen = input("Origen: ").strip().capitalize()
    destino = input("Destino: ").strip().capitalize()
    hora = input("Hora de salida (ej. 09:00am): ").strip()
    autobus = input("Tipo de autobús (PLUS / PLATINO / etc.): ").strip().upper()

    print(" Ruta agregada exitosamente ")
    print("\nOrigen      DESTINO       HORA        AUTOBUS")
    print(origen  + destino + hora  +  autobus)



def Eruta():
    print("\n=== Módulo eliminar ruta ===")
    print("1)TECATE     MEXICALI       9:00am      PLUS")
    print("2)TECATE     ENSENADA       12:00pm     PLATINO")
    print("3)TECATE     TIJUANA        3:00pm      PLUS")
    print("4)TIJUANA    TECATE         3:00pm      PLUS")
    print("5)TIJUANA    MEXICALI       9:00am      PLUS")
    opcel = int(input("Sleccione una ruta"))
    print("Tu ruta ha sido eliminada exitosamente")
