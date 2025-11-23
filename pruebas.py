from reservacion import Reservacion
from boleto import Boleto
from datetime import date

boleto = Boleto(350)

reservacion = Reservacion(date(2025,12,17),date.today(),1000,1160,16,5)
print(str(reservacion))
print()
print(str(boleto))
