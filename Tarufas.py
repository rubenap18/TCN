#Sub menu rutas

# modulo_consultar_rutas.py

def CTarifas():
    print("\nTipo de pasajero     Descripción")
    print("-------------------------------------------------")
    print("Niño               |  25% de descuento")
    print("Estudiante         |  50% descuento con credencial")
    print("Adulto mayor       |  50% descuento INAPAM")

def ATarifa():
    print("Añade una ruta")
    input("Ingresa nuevo nombre de la tarifa")
    input("Ingresa nueva descripcion de la tarifa")  
    print("Se agrego exitosamente")     

def ETarifa():
    print("modifica una ruta")
    print("\nTipo de pasajero     Descripción")
    print("-------------------------------------------------")
    print("1)Niño               |  25% de descuento")
    print("2)Estudiante         |  50% descuento con credencial")
    print("3)Adulto mayor       |  50% descuento INAPAM")
    mdtarifa = int(input("modifica una tarifa"))

    input("Ingresa nuevo nombre de la tarifa")
    input("Ingresa nueva descripcion de la tarifa")
    print("Se agrego exitosamente") 
