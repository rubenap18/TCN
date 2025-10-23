#Sub menu rutas

# modulo_consultar_rutas.py
def CTarifas():
    print("╔═══════════════════════════════════════════════════════════════════════════════╗")
    print("║                        C O N S U L T A R   T A R I F A                        ║")
    print("╠═══════════════════════════════════════════════════════════════════════════════╣")
    print("║  No │     CORRIDA        | HORA SALIDA │ HORA LLEGADA |  SERVICIO |  TARIFA   ║")
    print("╟──────────────────────────┼─────────────|──────────────|───────────|───────────╢")
    print("║  1  │Tijuana-Mexicali    │    7:00     |     10:30    |   PLUS    |   $250    ║")
    print("║  2  │Tijuana-Mexicali    │    9:00     |     11:00    |  PLATINO  |   $350    ║")
    print("║  3  │Tijuana-San Quintín │    13:00    |     18:30    |   PLUS    |   $450    ║")
    print("║  4  │Tijuana-San Quintín │    15:00    |     20:00    |   PLUS    |   $450    ║")
    print("╚═══════════════════════════════════════════════════════════════════════════════╝")


def mTarifa():
    print("╔═══════════════════════════════════════════════════════════════════════════════╗")
    print("║                       M O D I F I C A R   T A R I F A                         ║")
    print("╠═══════════════════════════════════════════════════════════════════════════════╣")
    print("║  No │     CORRIDA        | HORA SALIDA │ HORA LLEGADA |  SERVICIO |  TARIFA   ║")
    print("╟──────────────────────────┼─────────────|──────────────|───────────|───────────╢")
    print("║  1  │Tijuana-Mexicali    │    7:00     |     10:30    |   PLUS    |   $250    ║")
    print("║  2  │Tijuana-Mexicali    │    9:00     |     11:00    |  PLATINO  |   $350    ║")
    print("║  3  │Tijuana-San Quintín │    13:00    |     18:30    |   PLUS    |   $450    ║")
    print("║  4  │Tijuana-San Quintín │    15:00    |     20:00    |   PLUS    |   $450    ║")
    print("╚═══════════════════════════════════════════════════════════════════════════════╝")
    opcTR = int(input("Elige una Tarifa ▶ "))
    
    match opcTR:
        case 1:
            nuevo_tarifa = input("▶ Ingresa nuevo precio de la tarifa: ")
            print("╠═══════════════════════════════════════════════════════════════════════════════════════╣")
            print("║  No │     CORRIDA        | HORA SALIDA │ HORA LLEGADA |  SERVICIO |       TARIFA      ║")
            print("╟──────────────────────────┼─────────────|──────────────|───────────|───────────────────╢")
            print(f"║  1  │Tijuana-Mexicali    │    7:00     |     10:30    |   PLUS    |   ${nuevo_tarifa:<12}   ║")
            print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")
        case 2:
            nuevo_tarifa = input("▶ Ingresa nuevo precio de la tarifa: ")
            print("╠═══════════════════════════════════════════════════════════════════════════════════════╣")
            print("║  No │     CORRIDA        | HORA SALIDA │ HORA LLEGADA |  SERVICIO |       TARIFA      ║")
            print("╟──────────────────────────┼─────────────|──────────────|───────────|───────────────────╢")
            print(f"║  2  │Tijuana-Mexicali    │    9:00     |     11:00    |  PLATINO  |   ${nuevo_tarifa:<12}   ║")
            print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")
        case 3:
            nuevo_tarifa = input("▶ Ingresa nuevo precio de la tarifa: ")
            print("╠═══════════════════════════════════════════════════════════════════════════════════════╣")
            print("║  No │     CORRIDA        | HORA SALIDA │ HORA LLEGADA |  SERVICIO |       TARIFA      ║")
            print("╟──────────────────────────┼─────────────|──────────────|───────────|───────────────────╢")
            print(f"║  3  │Tijuana-San Quintín │    13:00    |     18:30    |   PLUS    |   ${nuevo_tarifa:<12}   ║")
            print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")
        case 4:
            nuevo_tarifa = input("▶ Ingresa nuevo precio de la tarifa: ")
            print("╠═══════════════════════════════════════════════════════════════════════════════════════╣")
            print("║  No │     CORRIDA        | HORA SALIDA │ HORA LLEGADA |  SERVICIO |      TARIFA       ║")
            print("╟──────────────────────────┼─────────────|──────────────|───────────|───────────────────╢")
            print(f"║  4  │Tijuana-San Quintín │    15:00    |     20:00    |   PLUS    |    ${nuevo_tarifa:<12}   ║")
            print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")
        case _:
            print("▶ Selecciona una tarifa a valida ")
    
    


  
