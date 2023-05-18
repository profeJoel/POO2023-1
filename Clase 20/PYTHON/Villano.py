from Personaje import Personaje

class Villano(Personaje):

    def __init__(self, id, nombre, vida, exp, poder, robar):
        super().__init__(id, nombre, vida, exp, poder)
        self.robar = robar

    # reemplazamos el metodo __str__ de la clase superior
    def __str__(self):
        return f"Heroe {self.nombre}({self.id}) [vida={self.vida}, exp={self.exp}, poder={self.poder}, robar= {self.robar}]"

    # reemplazamos el metodo atacar de la clase superior
    def atacar(self, v:Personaje): # Obliga a que el parametro v sea de clase Personaje
        if self.poder <= v.vida:
            v.vida -= self.poder
        else:
            v.vida = 0

    def robar_poder(self, h:Personaje):
        h.poder -= self.robar
        self.poder += self.robar