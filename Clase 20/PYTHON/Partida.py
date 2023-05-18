from random import randint
from Heroe import Heroe
from Villano import Villano

class Partida:

    def __init__(self, h: Heroe, v: Villano):
        self.h = h
        self.v = v

    def iniciar_partida(self):
        # sistema de turnos aleatorios
        # si el numero aleatorio es par, entonces ataca
        # si el numero aleatorio es impar, entonces espera
        ejecutar = True
        while ejecutar:
            self.tomar_turno(self.h, self.v)
            self.tomar_turno(self.v, self.h)
            if self.decidir_ganador():
                ejecutar = False

        print("Partida Terminada...")


    def tomar_turno(self, p1, p2):
        suerte = randint(0,100)
        if suerte % 2 == 0:
            p1.atacar(p2)
            print(f"Personaje {p1.nombre} Ataca!")
        else:
            print(f"Personaje {p1.nombre} Espera...")
    
    def decidir_ganador(self):
        if self.h.vida == 0:
            print(f"El villano {self.v.nombre} es el ganador...")
            return True

        if self.v.vida == 0:
            print(f"El heroe {self.h.nombre} es el ganador...")
            return True
        
        return False



        