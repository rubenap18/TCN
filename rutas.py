#Sub menu rutas

# modulo_consultar_rutas.py

def CRutas():
    opcion = -1  # cualquier valor diferente de 0 para iniciar el ciclo

    while opcion != 0:
        print("╔══════════════════════════════════════════════════╗")
        print("║           M Ó D U L O :  C O N S U L T A R       ║")
        print("║                    R U T A S                     ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║  1. ▶  Buscar ruta por destino                   ║")
        print("║  2. ▶  Buscar ruta por origen                    ║")
        print("║  3. ▶  Mostrar todas las rutas (simulada)        ║")
        print("║  0. ▶  Salir                                     ║")
        print("╚══════════════════════════════════════════════════╝")
        opcion = int(input("Elige una opción ▶ "))

        match opcion:
            case 0:
                print("╔══════════════════════════════════╗")
                print("║  Saliendo del módulo de rutas... ║")
                print("╚══════════════════════════════════╝")
            case 1:
                print("╔══════════════════════════════════════════════════╗")
                print("║           B U S C A R   P O R   D E S T I N O    ║")
                print("╠══════════════════════════════════════════════════╣")
                print("║  1. ▶  Tijuana                                   ║")
                print("║  2. ▶  Tecate                                    ║")
                print("╚══════════════════════════════════════════════════╝")
                opcdestino = int(input("Elige destino ▶ "))

                match opcdestino:
                    case 1:
                        print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                  R U T A S   H A C I A   T I J U A N A                                     ║")
                        print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ ESCALAS   │  DISTANCIA  │ PRECIO  │ TARIFAS ESPECIALES           ║")
                        print("╟─────────────┼───────────┼───────────┼─────────────┼────────┼───────────────────────────────╢")
                        print("║  MEXICALI   │ TIJUANA   │    1      │  270 km     │  $200  │ Niños $100 / Adulto $100      ║")
                        print("║  ENSENADA   │ TIJUANA   │    0      │  210 km     │  $200  │ Niños $100 / Adulto $100      ║")
                        print("║  TECATE     │ TIJUANA   │    0      │   45 km     │  $00   │ Niños $25 / Adulto $25        ║")
                        print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")

                    case 2:
                        print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                  R U T A S   H A C I A   T E C A T E                                       ║")
                        print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ ESCALAS   │  DISTANCIA  │ PRECIO  │ TARIFAS ESPECIALES           ║")
                        print("╟─────────────┼───────────┼───────────┼─────────────┼────────┼───────────────────────────────╢")
                        print("║  MEXICALI   │ TECATE    │     0     │  140 km     │  $200  │ Niños $100 / Adulto $100      ║")
                        print("║  ENSENADA   │ TECATE    │     1     │  130 km     │  $200  │ ENiños $100 / Adulto $100     ║")
                        print("║  TIJUANA    │ TECATE    │     0     │   45 km     │  $50   │ Niños $25 / Adulto $25        ║")
                        print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")
                    
                    case _:
                        print("╔═══════════════════════╗")
                        print("║  ⚠  Opción inválida   ║")
                        print("╚═══════════════════════╝")

            case 2:
                print("╔══════════════════════════════════════════════════╗")
                print("║           B U S C A R   P O R   O R I G E N      ║")
                print("╠══════════════════════════════════════════════════╣")
                print("║  1. ▶  Tijuana                                   ║")
                print("║  2. ▶  Tecate                                    ║")
                print("╚══════════════════════════════════════════════════╝")
                opcorigen = int(input("Elige origen ▶ "))

                match opcorigen:
                    case 1:
                        print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                R U T A S   D E S D E   T I J U A N A                                       ║")
                        print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ ESCALAS   │  DISTANCIA  │ PRECIO  │ TARIFAS ESPECIALES           ║")
                        print("╟─────────────┼───────────┼───────────┼─────────────┼────────┼───────────────────────────────╢")
                        print("║  TIJUANA    │ MEXICALI  │     1     │  270 km     │  $200  │ Niños $100 / Adulto $100      ║")
                        print("║  TIJUANA    │ ENSENADA  │     0     │  210 km     │  $200  │ Niños $100 / Adulto $100      ║")
                        print("║  TIJUANA    │ TECATE    │     0     │   45 km     │  $50   │ Niños $25 / Adulto $25        ║")
                        print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")

                    case 2:
                        print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                R U T A S   D E S D E   T E C A T E                                         ║")
                        print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ ESCALAS   │  DISTANCIA  │ PRECIO │ TARIFAS ESPECIALES            ║")
                        print("╟─────────────┼───────────┼───────────┼─────────────┼────────┼───────────────────────────────╢")
                        print("║  TECATE     │ MEXICALI  │    1      │  240 km     │  $200  │ Niños $100 / Adulto $100      ║")
                        print("║  TECATE     │ ENSENADA  │    0      │  230 km     │  $200  │ Niños $100 / Adulto $100      ║")
                        print("║  TECATE     │ TIJUANA   │    0      │   45 km     │  $50   │ Niños $25 / Adulto $25        ║")
                        print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")

            case 3:
                        print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                      T O D A S   L A S   R U T A S   (Simulada)                            ║")
                        print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ ESCALAS   │  DISTANCIA  │ PRECIO │ TARIFAS ESPECIALES            ║")
                        print("╟─────────────┼───────────┼───────────┼─────────────┼────────┼───────────────────────────────╢")
                        print("║  TECATE     │ MEXICALI  │     0     │   240 km    │  $200  │ Niños $100 / Adulto $100      ║")
                        print("║  TECATE     │ ENSENADA  │     1     │   230 km    │  $300  │ Niños $100 / Adulto $100      ║")
                        print("║  TECATE     │ TIJUANA   │     0     │    45 km    │  $400  │ Niños $100 / Adulto $100      ║")
                        print("║  TIJUANA    │ TECATE    │     0     │    45 km    │  $50   │ Niños $25 / Adulto $25        ║")
                        print("║  TIJUANA    │ MEXICALI  │     1     │   270 km    │  $300  │ Niños $100 / Adulto $100      ║")
                        print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")
            case _:
                print("╔═══════════════════════╗")
                print("║  ⚠  Opción inválida   ║")
                print("╚═══════════════════════╝")

           

def ARuta():
    print("╔══════════════════════════════════════════════════╗")
    print("║             M Ó D U L O :  A G R E G A R         ║")
    print("║                    R U T A S                     ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║                Agregar nueva ruta                ║")
    print("╚══════════════════════════════════════════════════╝")

    origen = input("Ingrese origen: ").strip().capitalize()
    destino = input("Ingrese destino: ").strip().capitalize()
    escalas = input("Numero de escalas: ")

    print("\n╔══════════════════════════════════════╗")
    print("║       Ruta agregada exitosamente       ║")
    print("╠════════════════════════════════════════╣")
    print("║  ORIGEN     │ DESTINO   │ ESCALAS      ║")
    print("╟─────────────┼───────────┼──────────────╢")
    print(f"║  {origen:<10} │ {destino:<9} │ {escalas} ║")
    print("╚════════════════════════════════════════╝")




def Eruta():
    print("\n╔═══════════════════════════════════════════════╗")
    print("║      M Ó D U L O   E L I M I N A R   R U T A    ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║  N° │ ORIGEN     │ DESTINO    │     ESCALAS     ║")
    print("╠═════╪════════════╪════════════╪═════════════════╣")
    print("║  1  │ TECATE     │ MEXICALI   │        0        ║")
    print("║  2  │ TECATE     │ ENSENADA   │        1        ║")
    print("║  3  │ TECATE     │ TIJUANA    │        0        ║")
    print("║  4  │ TIJUANA    │ SAN FELIPE │        2        ║")
    print("║  5  │ TIJUANA    │ MEXICALI   │        1        ║")
    print("╚═════╧════════════╧════════════╧═════════════════╝")

    opcel = int(input("Seleccione una ruta para eliminar (1-5): "))

    print(f"\nLa ruta número {opcel} ha sido eliminada exitosamente ")
