# validaciones.py
import re
from PySide6.QtWidgets import QMessageBox

class Validador:
    
    def validar_nombre(self, nombre):
        """Valida que el nombre solo contenga letras y espacios"""
        if not nombre or not nombre.strip():
            return False, "El nombre no puede estar vacío"
        
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            return False, "El nombre solo puede contener letras y espacios"
        
        return True, ""
    
    def validar_apellido(self, apellido, tipo="apellido"):
        """Valida que el apellido solo contenga letras"""
        if not apellido or not apellido.strip():
            return False, f"El {tipo} no puede estar vacío"
        
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellido):
            return False, f"El {tipo} solo puede contener letras"
        
        return True, ""
    
    def validar_telefono(self, telefono):
        """Valida que el teléfono tenga formato correcto"""
        if not telefono or not telefono.strip():
            return False, "El teléfono no puede estar vacío"
        
        telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono.strip())
        
        if not telefono_limpio.isdigit():
            return False, "El teléfono solo puede contener números"
        
        if len(telefono_limpio) != 10:
            return False, "El teléfono debe tener 10 dígitos"
            
        return True, ""
    
    def validar_operador_completo(self, nombre, apellPat, apellMat, telefono, fechaNac, fechaContrato):
        """Valida todos los campos del operador"""
        errores = []
        
        # Validar nombre
        if not nombre or not nombre.strip():
            errores.append("El nombre es obligatorio")
        elif len(nombre.strip()) < 2:
            errores.append("El nombre debe tener al menos 2 caracteres")
        
        # Validar apellido paterno
        if not apellPat or not apellPat.strip():
            errores.append("El apellido paterno es obligatorio")
        elif len(apellPat.strip()) < 2:
            errores.append("El apellido paterno debe tener al menos 2 caracteres")
        
        # Validar apellido materno (opcional)
        if apellMat and len(apellMat.strip()) < 2:
            errores.append("El apellido materno debe tener al menos 2 caracteres")
        
        # Validar teléfono
        telefono_valido, error_telefono = self.validar_telefono(telefono)
        if not telefono_valido:
            errores.append(error_telefono)
        
        # Validar fechas (si el método existe)
        if hasattr(self, 'validar_fecha'):
            if not self.validar_fecha(fechaNac):
                errores.append("La fecha de nacimiento no es válida")
            
            if not self.validar_fecha(fechaContrato):
                errores.append("La fecha de contrato no es válida")
        
        return len(errores) == 0, errores
        
    def mostrar_errores(self, parent, errores):
        """Muestra los errores en un QMessageBox"""
        if errores:
            mensaje = "Se encontraron los siguientes errores:\n\n" + "\n".join(f"• {error}" for error in errores)
            QMessageBox.warning(parent, "Errores de validación", mensaje)
            return False
        return True
    
    def validar_fecha(self, fecha_str):
        """Valida que una fecha tenga formato YYYY-MM-DD y sea válida"""
        try:
            # Verificar formato básico
            if not fecha_str or len(fecha_str) != 10:
                return False
                
            # Verificar que tenga el formato correcto
            partes = fecha_str.split('-')
            if len(partes) != 3:
                return False
                
            año, mes, dia = partes
            
            # Verificar que sean números
            if not (año.isdigit() and mes.isdigit() and dia.isdigit()):
                return False
                
            # Verificar rango de fechas razonable
            año_num = int(año)
            mes_num = int(mes)
            dia_num = int(dia)
            
            if año_num < 1900 or año_num > 2100:
                return False
                
            if mes_num < 1 or mes_num > 12:
                return False
                
            if dia_num < 1 or dia_num > 31:
                return False
                
            # Verificar fecha específica (ej: no 31 de febrero)
            try:
                from datetime import datetime
                datetime.strptime(fecha_str, "%Y-%m-%d")
                return True
            except ValueError:
                return False
                
        except Exception:
            return False