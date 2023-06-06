import sys
from PyQt6.QtWidgets import QApplication, QWidget

class Ventana(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100, 500,500)
        self.setWindowTitle("Primera Ventana en PyQt6")
        self.show() # Muestre efectivamente en pantalla (obligatorio)

if __name__ == "__main__":

    app = QApplication(sys.argv) # Lanzar la aplicación con una llamada al sistema.
    #Montar la ventana.
    ventana = Ventana()
    sys.exit(app.exec())