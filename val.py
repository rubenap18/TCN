
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

                print("╔════════════════════════════════════╗");
                print("║        OPCION FUERA DE RANGO       ║");
                print("╚════════════════════════════════════╝");
                
    return valor #returnando VALOR como tipo int