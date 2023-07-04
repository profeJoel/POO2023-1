import sys
from random import randint

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox, QDialog, QDialogButtonBox, QGridLayout

class VentanaTexto(QWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title

        self.setWindowTitle("Ventana Texto")

        capa = QVBoxLayout()
        self.ventana_3 = None
        
        texto = QLabel(f"{self.title}")
        capa.addWidget(texto)
        self.setLayout(capa)

class OtraVentana1(QWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title

        self.setWindowTitle(self.title)

        capa = QGridLayout()
        self.ventana_3 = None
        
        texto = QLabel(f"Hola, estoy en la ventana: {self.title}")
        boton = QPushButton("Ir a ventana 3")
        capa.addWidget(texto, 0,0)
        capa.addWidget(boton, 0,1)
        boton.clicked.connect(self.cambiar_ventana)
        self.setLayout(capa)
    
    def cambiar_ventana(self):
        if self.ventana_3 is None:
            self.ventana_3 = VentanaTexto("Chao")
            self.ventana_3.show()
        else:
            self.ventana_3 = None

class OtraVentana2(QWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title

        self.setWindowTitle(self.title)

        capa = QVBoxLayout()
        self.ventana_4 = None
        
        texto = QLabel(f"Saludos")
        self.entrada = QLineEdit()
        boton = QPushButton("Ir a ventana 4")
        capa.addWidget(texto)
        capa.addWidget(self.entrada)
        capa.addWidget(boton)
        boton.clicked.connect(self.cambiar_ventana)
        self.setLayout(capa)
    
    def cambiar_ventana(self):
        if self.ventana_4 is None:
            self.ventana_4 = VentanaTexto(f"Buenos Días {self.entrada.text()}")
            self.ventana_4.show()
        else:
            self.ventana_4 = None



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.nueva_ventana = None
        self.nueva_ventana_1 = OtraVentana1("Ventana 1")
        self.nueva_ventana_2 = OtraVentana2("Ventana 2")

        #Sección de diseño
        self.setWindowTitle("Multiventanas")
        self.setFixedSize(QSize(500,500))

        caja = QVBoxLayout()

        # Agregar componentes
        texto = QLabel("Ventana Principal")
        caja.addWidget(texto)
        boton_1 = QPushButton("ir a Ventana 1")
        boton_2 = QPushButton("ir a Ventana 2")
        caja.addWidget(boton_1)
        caja.addWidget(boton_2)

        boton_1.clicked.connect(lambda e : self.cambiar_ventana(self.nueva_ventana_1))
        boton_2.clicked.connect(lambda e : self.cambiar_ventana(self.nueva_ventana_2))

        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    
    def cambiar_ventana(self, v):
        if v is not None:
            if v.isVisible():
                v.hide()
            else:
                v.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
