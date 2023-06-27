import sys
from random import randint

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox, QDialog, QDialogButtonBox, QGridLayout

class OtraVentana(QWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title

        self.setWindowTitle(self.title)

        capa = QGridLayout()
        
        texto = QLabel(f"Hola, estoy en la ventana: {self.title} > {randint(0,100)}")
        capa.addWidget(texto, 0,0)
        self.setLayout(capa)
        self.show()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.nueva_ventana = None
        self.nueva_ventana = OtraVentana("Ventana Predeterminada")

        #Sección de diseño
        self.setWindowTitle("Multiventanas")
        self.setFixedSize(QSize(500,500))

        caja = QVBoxLayout()

        # Agregar componentes
        texto = QLabel("Ventana Principal")
        caja.addWidget(texto)
        boton = QPushButton("ir a Ventana Secundaria")
        caja.addWidget(boton)

        boton.clicked.connect(self.cambiar_ventana)

        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    
    def cambiar_ventana(self):
        #Primera Opcion 
        # VentanaPrincipal > self.nueva_ventana = None
        #self.nueva_ventana = OtraVentana("Nueva Ventana")
        #self.nueva_ventana.show()

        """Segunda forma de presentar ventana
        if self.nueva_ventana is None:
            self.nueva_ventana = OtraVentana("Nueva Ventana")
            self.nueva_ventana.show()
        else:
            self.nueva_ventana = None
        """

        """Ventana persistente"""
        if self.nueva_ventana.isVisible():
            self.nueva_ventana.hide()
        else:
            self.nueva_ventana.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
