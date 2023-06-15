import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0

        #Sección de diseño
        self.setWindowTitle("La 2da aplicación con PyQt6")
        self.setFixedSize(QSize(500,500))

        caja = QGridLayout()
        b1 = QPushButton("1")
        b2 = QPushButton("2")
        b3 = QPushButton("3")
        b4 = QPushButton("4")
        b5 = QPushButton("5")
        b6 = QPushButton("6")
        b7 = QPushButton("7")
        b8 = QPushButton("8")
        b9 = QPushButton("9")
        caja.addWidget(b1, 0,0)
        caja.addWidget(b2, 0,1)
        caja.addWidget(b3, 0,2)
        caja.addWidget(b4, 1,0)
        caja.addWidget(b5, 1,1)
        caja.addWidget(b6, 1,2)
        caja.addWidget(b7, 2,0)
        caja.addWidget(b8, 2, 1)
        caja.addWidget(b9, 2, 2)
        """
        #Ejecucion de la reacción al Click
        b1.clicked.connect(self.reaccionar_1)
        b2.clicked.connect(self.reaccionar_2)
        b3.clicked.connect(self.reaccionar_3)
        b4.clicked.connect(self.reaccionar_4)
        b5.clicked.connect(self.reaccionar_5)
        b6.clicked.connect(self.reaccionar_6)
        b7.clicked.connect(self.reaccionar_7)
        b8.clicked.connect(self.reaccionar_8)
        b9.clicked.connect(self.reaccionar_9)
        """

        #Ejecucion de la reacción al Click
        b1.clicked.connect(lambda evento: self.reaccionar(b1.text()))
        b2.clicked.connect(lambda evento: self.reaccionar(b2.text()))
        b3.clicked.connect(lambda evento: self.reaccionar(b3.text()))
        b4.clicked.connect(lambda evento: self.reaccionar(b4.text()))
        b5.clicked.connect(lambda evento: self.reaccionar(b5.text()))
        b6.clicked.connect(lambda evento: self.reaccionar(b6.text()))
        b7.clicked.connect(lambda evento: self.reaccionar(b7.text()))
        b8.clicked.connect(lambda evento: self.reaccionar(b8.text()))
        b9.clicked.connect(lambda evento: self.reaccionar(b9.text()))
        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    

    def reaccionar(self, numero):
        print(f"Boton {numero} con lambda y metodo reaccionar")

    def reaccionar_1(self):
        print(f"Boton 1")

    def reaccionar_2(self):
        print(f"Boton 2")
    def reaccionar_3(self):
        print(f"Boton 3")

    def reaccionar_4(self):
        print(f"Boton 4")
    def reaccionar_5(self):
        print(f"Boton 5")
    def reaccionar_6(self):
        print(f"Boton 6")

    def reaccionar_7(self):
        print(f"Boton 7")

    def reaccionar_8(self):
        print(f"Boton 8")

    def reaccionar_9(self):
        print(f"Boton 9")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
