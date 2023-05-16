from Punto import Punto
from Cuadrilatero import Cuadrilatero

class Trapecio(Cuadrilatero):

    def __init__(self, A, B, C, D):
        super().__init__(A, B, C, D)
        self.ladoAB = self.distancia(self.A, self.B)
        self.ladoBC = self.distancia(self.B, self.C)
        self.ladoCD = self.distancia(self.C, self.D)
        self.ladoDA = self.distancia(self.D, self.A)
        self.calcular_area()

    def calcular_area(self):
        lado_menor = min(self.ladoAB, self.ladoBC, self.ladoCD, self.ladoDA)
        lado_mayor = max(self.ladoAB, self.ladoBC, self.ladoCD, self.ladoDA)
        aux = Punto(self.B.x, self.A.y)
        altura = self.distancia(aux,self.B)
        self.area = ((lado_menor+lado_mayor)*altura)/2
        return self.area