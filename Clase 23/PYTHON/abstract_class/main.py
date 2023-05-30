from animal import Animal
from gato import Gato
from perro import Perro

if __name__ == "__main__":
    #ameba = Animal()
    #ameba.setAnimal("Ameba", "Ameba")
    #ameba.mostrar()
    garfield = Gato()
    firulais = Perro()

    garfield.setAnimal("Garfield", "Felino")
    firulais.setAnimal("Firulais", "Canino")

    garfield.mostrar()
    firulais.mostrar()

    print(garfield.hacer_sonido())
    print(firulais.hacer_sonido())