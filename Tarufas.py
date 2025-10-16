#Sub menu rutas

# modulo_consultar_rutas.py
def CTarifas():
    print("╔══════════════════════════════════════════════════════════════════════════╗")
    print("║                M Ó D U L O :  C O N S U L T A R   T A R I F A S          ║")
    print("╠══════════════════════════════════════════════════════════════════════════╣")
    print("║  TIPO DE PASAJERO     │  DESCRIPCIÓN                                     ║")
    print("╟────────────────────────┼─────────────────────────────────────────────────╢")
    print("║  Niño                 │  25% de descuento                                ║")
    print("║  Estudiante           │  50% descuento con credencial                    ║")
    print("║  Adulto mayor         │  50% descuento con credencial INAPAM             ║")
    print("╚══════════════════════════════════════════════════════════════════════════╝")


def ATarifa():
    print("╔══════════════════════════════════════════════════════════════════════════╗")
    print("║                M Ó D U L O :  A G R E G A R   T A R I F A                ║")
    print("╠══════════════════════════════════════════════════════════════════════════╣")
    print("║  Añadir nueva tarifa:                                                    ║")
    print("╚══════════════════════════════════════════════════════════════════════════╝")

    nombre = input("▶ Ingresa nuevo nombre de la tarifa: ").strip().capitalize()
    descripcion = input("▶ Ingresa nueva descripción de la tarifa: ").strip().capitalize()
    
    print("\n╔══════════════════════════════════════════════════════════════════════════╗")
    print("║               Tarifa agregada exitosamente                               ║")
    print("╠══════════════════════════════════════════════════════════════════════════╣")
    print(f"║  Nombre: {nombre:<15} │ Descripción: {descripcion:<30}║")
    print("╚══════════════════════════════════════════════════════════════════════════╝")


def ETarifa():
    print("╔══════════════════════════════════════════════════════════════════════════╗")
    print("║                M Ó D U L O :  M O D I F I C A R   T A R I F A            ║")
    print("╠══════════════════════════════════════════════════════════════════════════╣")
    print("║  TIPO DE PASAJERO     │  DESCRIPCIÓN                                     ║")
    print("╟────────────────────────┼─────────────────────────────────────────────────╢")
    print("║  1) Niño              │  25% de descuento                                ║")
    print("║  2) Estudiante        │  50% descuento con credencial                    ║")
    print("║  3) Adulto mayor      │  50% descuento INAPAM                            ║")
    print("╚══════════════════════════════════════════════════════════════════════════╝")

    mdtarifa = int(input("▶ Selecciona una tarifa a modificar: "))
    nuevo_nombre = input("▶ Ingresa nuevo nombre de la tarifa: ").strip().capitalize()
    nueva_desc = input("▶ Ingresa nueva descripción de la tarifa: ").strip().capitalize()

    print("\n╔══════════════════════════════════════════════════════════════════════════╗")
    print("║           ✅  Tarifa modificada exitosamente                             ║")
    print("╠══════════════════════════════════════════════════════════════════════════╣")
    print(f"║  Nueva tarifa: {nuevo_nombre:<15} │ Descripción: {nueva_desc:<30}║")
    print("╚══════════════════════════════════════════════════════════════════════════╝")
