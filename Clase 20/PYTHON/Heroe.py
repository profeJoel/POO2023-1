from Personaje import Personaje
from Villano import Villano

class Heroe(Personaje):

    def __init__(self, id, nombre, vida, exp, poder, sanacion):
        super().__init__(id, nombre, vida, exp, poder)
        self.sanacion = sanacion

    # reemplazamos el metodo __str__ de la clase superior
    def __str__(self):
        return f"Heroe {self.nombre}({self.id}) [vida={self.vida}, exp={self.exp}, poder={self.poder}, sanacion= {self.sanacion}]"

    # reemplazamos el metodo atacar de la clase superior
    def atacar(self, v:Villano): # Obliga a que el parametro v sea de clase Villano
        if self.poder <= v.vida:
            v.vida -= self.poder
        else:
            v.vida = 0

    def sanar(self, h):
        h.vida += self.sanacion