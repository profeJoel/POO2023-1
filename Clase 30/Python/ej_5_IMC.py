import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox, QDialog, QDialogButtonBox

class VentanaDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana Customizable")
        btn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.boton = QDialogButtonBox(btn)
        self.boton.accepted.connect(self.accept)
        self.boton.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        mensaje = QLabel("Ventanita desplegada... Limpiar Datos?")
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.boton)
        self.setLayout(self.layout)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        #Sección de diseño
        self.setWindowTitle("IMC")
        self.setFixedSize(QSize(500,500))

        caja_grande = QVBoxLayout()
        caja_pequena = QHBoxLayout()
        bloque_masa = QVBoxLayout()
        bloque_altura = QVBoxLayout()

        # Agregar componentes
        texto_masa = QLabel("Ingrese Masa")
        bloque_masa.addWidget(texto_masa)
        self.ingreso_masa = QLineEdit()
        bloque_masa.addWidget(self.ingreso_masa)


        texto_altura = QLabel("Ingrese Altura")
        bloque_altura.addWidget(texto_altura)
        self.ingreso_altura = QLineEdit()
        bloque_altura.addWidget(self.ingreso_altura)

        caja_pequena.addLayout(bloque_masa)
        caja_pequena.addLayout(bloque_altura)

        texto_bienvenida = QLabel("Hola, calculamos tu IMC")
        caja_grande.addWidget(texto_bienvenida)
        caja_grande.addLayout(caja_pequena)
        boton_imc = QPushButton("Calcular Masa")
        caja_grande.addWidget(boton_imc)
        self.texto_resultado = QLabel("IMC = ")
        caja_grande.addWidget(self.texto_resultado)

        boton_imc.clicked.connect(self.calcular_imc)

        boton_limpiar = QPushButton("Limpiar")
        caja_grande.addWidget(boton_limpiar)
        boton_limpiar.clicked.connect(self.limpieza_datos)

        panel = QWidget()
        panel.setLayout(caja_grande)
        self.setCentralWidget(panel)
    
    def calcular_imc(self):
        if self.ingreso_masa.text() != "" and self.ingreso_altura.text()!= "" and self.ingreso_masa.text().isdecimal() and self.ingreso_altura.text().__contains__(".") and float(self.ingreso_masa.text()) > 0 and float(self.ingreso_altura.text()) > 0:
            m = float(self.ingreso_masa.text())
            h = float(self.ingreso_altura.text())
            imc = m/h**2
            self.texto_resultado.setText(f"IMC = {imc}")
        else:
            #self.texto_resultado.setText("Operación no válida")

            ### Creación de QMessageBox Normal
            # ventana_emergente = QMessageBox(self)
            # ventana_emergente.setWindowTitle("Error en el cálculo")
            # ventana_emergente.setText("Uno de los valores no corresponde")
            # btn = ventana_emergente.exec()

            # if btn == QMessageBox.StandardButton.Ok:
            #     print("Si estoy de acuerdo")

            ### Ejemplode QMessageBox modo critical
            btn = QMessageBox.critical(
                self,
                "Cálculo no se muestra",
                "Los valores no son los adecuados para generar el cálculo de IMC.",
                buttons= QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
                defaultButton= QMessageBox.StandardButton.Discard
            )

            if btn == QMessageBox.StandardButton.Discard:
                self.ingreso_masa.clear()
                self.ingreso_altura.clear()
            elif btn == QMessageBox.StandardButton.NoToAll:
                self.ingreso_masa.setText("0")
                self.ingreso_altura.setText("0")
            else:
                self.ingreso_masa.setText("valor inválido")
                self.ingreso_altura.setText("valor inválido")
        
    def limpieza_datos(self):
        """
        ventanita = QDialog(self)
        ventanita.setWindowTitle("Ventana Flotante")
        ventanita.exec()
        """
        ventanita = VentanaDialog()
        if ventanita.exec():
            self.ingreso_masa.clear()
            self.ingreso_altura.clear()


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
