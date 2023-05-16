from Punto import Punto
from Cuadrilatero import Cuadrilatero
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Trapecio import Trapecio

if __name__ == "__main__":
    cuadradito = Cuadrado(Punto(1,1), Punto(1,2), Punto(2,2), Punto(2,1))
    print(cuadradito)

    rectangulito = Rectangulo(Punto(1,1), Punto(1,2), Punto(3,2), Punto(3,1))
    print(rectangulito)


    trapecito = Trapecio(Punto(0,1), Punto(1,2), Punto(3,2), Punto(3.5,1))
    print(trapecito)