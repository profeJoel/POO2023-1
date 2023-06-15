import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0

        #Sección de diseño
        self.setWindowTitle("Calculadora de Potencia")
        self.setFixedSize(QSize(500,500))

        caja = QVBoxLayout()

        # Agregar componentes
        i_base = QLabel("Ingrese valor base")
        caja.addWidget(i_base)
        self.base = QLineEdit()
        caja.addWidget(self.base)

        i_exp = QLabel("Ingrese el Exponente")
        caja.addWidget(i_exp)
        self.exp = QLineEdit()
        caja.addWidget(self.exp)

        boton = QPushButton("Calcular")
        caja.addWidget(boton)

        self.resultado = QLabel("Resultado es: ")
        caja.addWidget(self.resultado)

        #Ejecucion de la reacción al Click
        boton.clicked.connect(self.calcular_potencia)

        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    
    def calcular_potencia(self):
        if self.base.text() != "" and self.exp.text()!= "" and self.base.text().isdecimal() and self.exp.text().isdecimal():
            b = int(self.base.text())
            e = int(self.exp.text())
            pot = b**e
            self.resultado.setText(f"La potencia es{pot}")
        else:
            self.resultado.setText("Operación no válida")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
