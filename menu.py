# Vista de la empresa

#Menu PRINCIPAL
def mPrincipal():
    print('\n')
    print("|            TCN            |")
    print("|  1) Rutas                 |")
    print("|  2) Corridas              |")
    print("|  3) Autobuses             |")
    print("|  4) Asientos              |")
    print("|  5) Boletos               |")
    print("|  6) Reservaciones         |")
    print("|  7) Pasajeros             |")
    print("|  8) Tarifas               |")
    print("|  0) Salir                 |")
    
def mRutas():
    print("\n")
    print("|           RUTAS           |")
    print("|  1) Consultar rutas       |")
    print("|  2) Modificar ruta        |") #Dentro de esta opcion se va a preguntar la ciudad origen y el destino
    print("|  3) Consultar escalas     |")
    print("|  4) Modificar escalas     |") #Dentro de esta opcion se va a preguntar en donde se va a hacer cada escala y mientras se vayan agregando escalas se va a sacar la cant de escalas
    print("|  5) Eliminar rutas        |")
    print("|  0) Salir                 |")

def mCorridas():
    print("")
    print("|         CORRIDAS         |")
    print("|  1) Consultar corridas   |")
    print("|  2) Agregar corrida      |")
    print("|  3) Eliminar corrida     |")
    print("|  0) Salir                |")
    
#Menu AUTOBUSES
def mAutobuses():
    print("\n")
    print("|                 AUTOBUSES              |")
    print("|  1) Agregar nuevo autobús              |")
    print("|  2) Eliminar autobús existente         |")
    print("|  3) Consultar autobuses disponibles    |")
    print("|  4) Asignar autobús a corrida          |")
    print("|  0) Salir                              |")
    
#Menu ASIENTOS
def mAsientos():
    print("\n")
    print("|                    ASIENTOS                      |")
    print("|  1) Consultar disponibilidad de asiento          |")
    print("|  2) Consultar datos del ocupante                 |")
    print("|  3) Bloquear asiento (situaciones especiales)    |")
    print("|  0) Salir                                        |")
    
#Menu BOLETOS 
def mBoletos():
    print("/n")
    print("|            BOLETOS              |")
    print("|  1) Consultar boleto emitido    |")
    print("|  2) Reimprimir boleto emitido   |")
    print("|  3) Listar boletos emitidos     |")
    print("|  0) Salir                       |")


#Menu RESERVACION
def mReservacion():
    print("/n")
    print("|         RESERVACION                        |")
    print("|  1) Listar reservaciones activas           |")
    print("|  2) Listar reservaciones pasadas           |")
    print("|  3) Crear reservaciones (manualmente)      |")
    print("|  4) Editar reservaciones (manualmente)     |")
    print("|  0) Salir                                  |")

#Menu PASAJEROS
def mPasajeros():
    print("\n")
    print("|            PASAJEROS                 |")
    print("|  1) Consultar datos del pasajero     |")
    print("|  2) Modificar datos del pasajero     |")
    print("|  3) Eliminar pasajero                |")
    print("|  4) Consultar boleto del pasajero    |")
    print("|  0) Salir                            |")
    
#Menu TARIFAS
def mTarifas():
    print("\n")
    print("|          Tarifas          |")
    print("|  1) Consultar tarifas     |")
    print("|  2) Agregar tarifa        |")
    print("|  3) Modificar tarifa      |")
    print("|  4) Eliminar tarifa       |")
    print("|  0) Salir                 |")