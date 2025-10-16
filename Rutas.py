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
        print("║  3. ▶  Mostrar todas las rutas                   ║")
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
                        print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                  R U T A S   H A C I A   T I J U A N A                            ║")
                        print("╠═══════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ AUTOBÚS   │  PRECIO  │ TARIFAS ESPECIALES               ║")
                        print("╟─────────────┼───────────┼───────────┼──────────┼──────────────────────────────────╢")
                        print("║  MEXICALI   │ TIJUANA   │ PLUS      │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("║  ENSENADA   │ TIJUANA   │ PLATINO   │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("║  TECATE     │ TIJUANA   │ PLUS      │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("╚═══════════════════════════════════════════════════════════════════════════════════╝")

                    case 2:
                        print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                  R U T A S   H A C I A   T E C A T E                              ║")
                        print("╠═══════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ AUTOBÚS   │  PRECIO  │ TARIFAS ESPECIALES               ║")
                        print("╟─────────────┼───────────┼───────────┼──────────┼──────────────────────────────────╢")
                        print("║  MEXICALI   │ TECATE    │ PLUS      │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("║  ENSENADA   │ TECATE    │ PLATINO   │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("║  TIJUANA    │ TECATE    │ PLUS      │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("╚═══════════════════════════════════════════════════════════════════════════════════╝")
                    
                    case 3:
                        print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                      T O D A S   L A S   R U T A S   (Simulada)                    ║")
                        print("╠═══════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ HORA     │ AUTOBÚS   │  PRECIO  │ TARIFAS ESPECIALES       ║")
                        print("╟─────────────┼───────────┼──────────┼───────────┼──────────┼─────────────────────────╢")
                        print("║  TECATE     │ MEXICALI  │ 09:00am  │ PLUS      │  $200    │ Estudiante $100 / Adulto $100 ║")
                        print("║  TECATE     │ ENSENADA  │ 12:00pm  │ PLATINO   │  $300    │ Estudiante $150 / Adulto $150 ║")
                        print("║  TECATE     │ TIJUANA   │ 03:00pm  │ PLATINO   │  $400    │ Estudiante $200 / Adulto $200 ║")
                        print("║  TIJUANA    │ TECATE    │ 03:00pm  │ PLUS      │  $200    │ Estudiante $100 / Adulto $100 ║")
                        print("║  TIJUANA    │ MEXICALI  │ 09:00am  │ PLUS      │  $300    │ Estudiante $150 / Adulto $150 ║")
                        print("╚═══════════════════════════════════════════════════════════════════════════════════╝")
                    
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
                        print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                R U T A S   D E S D E   T I J U A N A                              ║")
                        print("╠═══════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ AUTOBÚS   │  PRECIO  │ TARIFAS ESPECIALES               ║")
                        print("╟─────────────┼───────────┼───────────┼──────────┼──────────────────────────────────╢")
                        print("║  TIJUANA    │ MEXICALI  │ PLUS      │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("║  TIJUANA    │ ENSENADA  │ PLATINO   │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("║  TIJUANA    │ TECATE    │ PLUS      │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("╚═══════════════════════════════════════════════════════════════════════════════════╝")

                    case 2:
                        print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                        print("║                R U T A S   D E S D E   T E C A T E                                ║")
                        print("╠═══════════════════════════════════════════════════════════════════════════════════╣")
                        print("║  ORIGEN     │ DESTINO   │ AUTOBÚS   │  PRECIO  │ TARIFAS ESPECIALES               ║")
                        print("╟─────────────┼───────────┼───────────┼──────────┼──────────────────────────────────╢")
                        print("║  TECATE     │ MEXICALI  │ PLUS      │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("║  TECATE     │ ENSENADA  │ PLATINO   │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("║  TECATE     │ TIJUANA   │ PLUS      │  $200    │ Estudiante $100 / Adulto $100    ║")
                        print("╚═══════════════════════════════════════════════════════════════════════════════════╝")

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
    hora = input("Hora de salida (ej. 09:00am): ").strip()
    autobus = input("Tipo de autobús (PLUS / PLATINO / etc.): ").strip().upper()

    print("\n╔══════════════════════════════════════════════════╗")
    print("║              Ruta agregada exitosamente           ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  ORIGEN     │ DESTINO   │ AUTOBÚS     ║")
    print("╟─────────────┼───────────┼──────────────╢")
    print(f"║  {origen:<10} │ {destino:<9} │ {autobus:<10} ║")
    print("╚══════════════════════════════════════════════════╝")




def Eruta():
    print("\n╔═══════════════════════════════════════════════╗")
    print("║      M Ó D U L O   E L I M I N A R   R U T A    ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║  N° │ ORIGEN     │ DESTINO    │   AUTOBÚS       ║")
    print("╠═════╪════════════╪════════════╪══════════╪══════╣")
    print("║  1  │ TECATE     │ MEXICALI   │ PLUS            ║")
    print("║  2  │ TECATE     │ ENSENADA   │ PLATINO         ║")
    print("║  3  │ TECATE     │ TIJUANA    │ PLUS            ║")
    print("║  4  │ TIJUANA    │ TECATE     │ PLUS            ║")
    print("║  5  │ TIJUANA    │ MEXICALI   │ PLUS            ║")
    print("╚═════╧════════════╧════════════╧══════════╧══════╝")

    opcel = int(input("Seleccione una ruta para eliminar (1-5): "))

    print(f"\nLa ruta número {opcel} ha sido eliminada exitosamente ")
