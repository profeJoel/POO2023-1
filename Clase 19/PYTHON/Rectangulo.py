from Punto import Punto
from Cuadrilatero import Cuadrilatero

class Rectangulo(Cuadrilatero):

    def __init__(self, A, B, C, D):
        super().__init__(A, B, C, D)
        self.ladoAB = self.distancia(self.A, self.B)
        self.ladoBC = self.distancia(self.B, self.C)
        self.ladoCD = self.distancia(self.C, self.D)
        self.ladoDA = self.distancia(self.D, self.A)
        self.calcular_area()

    def calcular_area(self):
        ancho = min(self.ladoAB, self.ladoBC, self.ladoCD, self.ladoDA)
        largo = max(self.ladoAB, self.ladoBC, self.ladoCD, self.ladoDA)
        self.area = largo * ancho
        return self.area