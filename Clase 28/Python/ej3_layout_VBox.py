import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0

        #Sección de diseño
        self.setWindowTitle("La 2da aplicación con PyQt6")
        self.setFixedSize(QSize(500,500))

        caja = QVBoxLayout()

        # Agregar componentes
        texto = QLabel("Hola Mundo")
        caja.addWidget(texto)
        texto2 = QLabel("Estamos haciendo otro texto")
        caja.addWidget(texto2)
        boton = QPushButton("Presioname")
        caja.addWidget(boton)

        #Ejecucion de la reacción al Click
        boton.clicked.connect(self.reaccionar)

        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    
    def reaccionar(self):
        self.contador += 1
        print(f"El boton se ha presionado {self.contador} veces!!!")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
