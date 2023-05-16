from Punto import Punto
from Cuadrilatero import Cuadrilatero

class Cuadrado(Cuadrilatero):

    def __init__(self, A, B, C, D):
        super().__init__(A, B, C, D)
        self.lado = self.distancia(self.A, self.B)
        self.calcular_area()
    
    def calcular_area(self):
        self.area = self.lado**2
        return self.area