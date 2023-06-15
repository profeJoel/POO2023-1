import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QStackedLayout, QWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0

        #Sección de diseño
        self.setWindowTitle("La 2da aplicación con PyQt6")
        self.setFixedSize(QSize(500,500))

        caja = QStackedLayout()
        texto0 = QLabel("Panel 0")
        texto1 = QLabel("Panel 1")
        texto2 = QLabel("Panel 2")
        texto3 = QLabel("Panel 3")

        caja.addWidget(texto0)
        caja.addWidget(texto1)
        caja.addWidget(texto2)
        caja.addWidget(texto3)

        caja.setCurrentIndex(4)

        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
