import re

class Validaciones:
    def __init__(self):
        pass
    def validar_id(self,valor):
        try:
            valor = str(valor) #se conviete a string
        except Exception:
            return False
        
        if valor == '':
            return 'Todo'

        patron = r'^[A-Za-z0-9_-]{1,}$'
        return bool(re.match(patron, valor))
