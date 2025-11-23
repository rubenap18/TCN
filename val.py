import datetime


def vOpciones(msg, inf, sup,funcion):
    while True:
        funcion()
        valor = input(msg)
        
        if valor.isdigit() != True: #validacion de solo enteros
            print("| Solo numeros enteros |")
        else:
            valor = int(valor) #validacion de limites inf y sup
            if valor >= inf and valor <= sup:
                break
            
            else:

                print("╔════════════════════════════════════╗")
                print("║        OPCION FUERA DE RANGO       ║")
                print("╚════════════════════════════════════╝")
                
    return valor #returnando VALOR como tipo int


#------------------------------------------------------------------------------
def validarImporteBoleto(msg):
    while True:
        importe = input(msg)
        if importe == '':
            print('No has ingresado nada.')
            continue
        if ' ' in importe:
            print('No se permiten espacios.')
            continue

        if not importe.replace(' ','').isdigit():
            print('Solo se permiten numeros.')
            continue

        if int(importe) <= 0: 
            print('El importe debe ser mayor a 0')
            continue
        
        return importe


def validarMontoReservacion(msg):
    while True:
        monto = input(msg)
        if monto == '':
            print('No has ingresado nada.')
            continue
        if ' ' in monto:
            print('No se permiten espacios.')
            continue

        if not monto.replace(' ','').isdigit():
            print('Solo se permiten numeros.')
            continue

        if int(monto) <= 0: 
            print('El monto debe ser mayor a 0')
            continue
        
        return monto

def validarFechaReservacion(msg):
    while True:
        dia = validarDia('Ingresa el dia: ')
        mes = validarMes('Ingresa el mes: ')
        anio = validarAnio('Ingresa el año: ')

        fecha = datetime.date(anio,mes,dia)

        if datetime.date.today() < fecha: 
            print('La fecha aun no llega')
            continue
        return fecha.strftime('%d/%m/%y')

def validarDia(msg):
    while True:
        dia = int(input(msg).strip())

        if str(dia) == '':
            print('No has ingresado nada.')
            continue

        if ' ' in str(dia):
            print('Sin espacios')
            continue

        if not str(dia).isdigit():
            print('Solo numeros')
            continue 

        if dia > 31 or dia < 1:
            print('Dia fuera de los rangos')
            continue

        return dia



def validarMes(msg):
    while True:
        mes = int(input(msg).strip())

        if str(mes) == '':
            print('No has ingresado nada.')
            continue

        if ' ' in str(mes):
            print('Sin espacios')
            continue

        if not str(mes).isdigit():
            print('Solo numeros')
            continue 

        if mes > 12 or mes < 1:
            print('Mes fuera de los rangos')
            continue
        return mes

def validarAnio(msg):
    while True:
        anio = int(input(msg).strip())

        if str(anio) == '':
            print('No has ingresado nada.')
            continue

        if ' ' in str(anio):
            print('Sin espacios')
            continue

        if not str(anio).isdigit():
            print('Solo numeros')
            continue 

        if anio < 1:
            print('Año debe ser mayor a 0')
            continue

        return anio

validarFechaReservacion('Ingresa algo:')

