# Areas de cada Cuadrilatero
# Cuadrado = A^2
# Rectangulo = A * B
# Trapecio = ((a+b)/2) * h, a = lado mas pequeno, b = lado mas grande, h = altura (calcular)
import math
from Punto import Punto

class Cuadrilatero:
    
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.area = None

    def calcular_area(self):
        print("Se calcula area...")
    
    def __str__(self):
        return f"El area del cuadrilatero es: {self.area}"

    def distancia(self, p1, p2):
        return math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
