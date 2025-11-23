import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, 
                            QVBoxLayout, QMainWindow, QStackedWidget,QSizePolicy)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile #Imports de PySyde

from PySide6.QtCore import Signal,Qt
from PySide6.QtGui import QCloseEvent

from ui.ventana_principal import Ui_panelPrincipal as Panel1
from ui.ventana_principal2 import Ui_panelPrincipal as Panel2

from ui.ventana_reservacion1 import Ui_Form as PanelReservacion1


from ui.ventana_horarios import HorariosPage as VentanaHorarios
from ui.prueba import Ui_ventana


class MainUI(QMainWindow):
    def __init__(self,app_manager):
        self.__app_manager = app_manager 

        super().__init__()
        #self.setupUi(self)
        self.setMinimumSize(1280,720)
        self.setWindowTitle('Transportes Cuervo Negro')
        self.showMaximized()
        self.setStyleSheet('background:#fff')

        #Agregando widget central 
        self.centralWidget = QWidget()
        self.layout = QVBoxLayout(self.centralWidget)   
        self.layout.setContentsMargins(0,0,0,0)
        self.setCentralWidget(self.centralWidget)

        #self.__cambiaPantalla = Signal()

        #creando StacketWidget
        self.stackedPrincipal = QStackedWidget()
        #self.stackedPrincipal.setStyleSheet('background:#000')
        self.layout.addWidget(self.stackedPrincipal)

        #instanciando QWidgets que son los paneles
        self.vp1 = VentanaPricipal()
        self.vp2 = VentanaPrincipal2()
        self.vr1 = VentanaReservacion1()
        self.ventana_horarios = VentanaHorarios(self.__app_manager) #le pasamos el manejador de los controladores

        #self.layout_vr1 = QVBoxLayout(self.vr1)
        #self.layout_vr1.addStretch(1)

        self.stackedPrincipal.addWidget(self.vp1)
        self.stackedPrincipal.addWidget(self.vp2)
        self.stackedPrincipal.addWidget(self.vr1)
        self.stackedPrincipal.addWidget(self.ventana_horarios)


        self.stackedPrincipal.setCurrentWidget(self.ventana_horarios)
        
    
        self.vp1.botonCambio.clicked.connect(lambda _:self.__cambiarPantalla('Pantalla 1'))
        self.vp2.botonCambio.clicked.connect(lambda _:self.__cambiarPantalla('Pantalla 2'))


    def __cambiarPantalla(self, nameWindow):
        self.setWindowTitle(nameWindow)

        if nameWindow == 'Pantalla 1':
            self.stackedPrincipal.setCurrentWidget(self.vp2)
            
        elif nameWindow == 'Pantalla 2':
            self.stackedPrincipal.setCurrentWidget(self.vp1)
            for i in self.__app_manager.ruta_controlador.consultarRuta():
                print(i)
    
    def closeEvent(self, event: QCloseEvent):
        """
        Este metodo que se llama cuando se preciona la X en esta ventana.
        """
        print("Terminando programa.")

        event.accept() 
        
        #Nota: Luego de esto event.accept(), el flujo del programa regresa al main.py

class VentanaPricipal(QWidget,Panel1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    
class VentanaPrincipal2(QWidget,Panel2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class VentanaReservacion1(QWidget,PanelReservacion1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class VentanaPrueba(QWidget,Ui_ventana):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
