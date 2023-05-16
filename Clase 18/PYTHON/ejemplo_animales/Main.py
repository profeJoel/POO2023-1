from Animal import Animal
from Gato import Gato
from Perro import Perro
from Vaca import Vaca

if __name__ == "__main__":
    # animal_1 = Animal(1,"Animal 1", "indeterminado")
    animal_1 = Animal(1)
    animal_1.se_mueve()
    animal_1.hace_sonido()

    tom = Gato(2, "Tom", "Felino", "liso y corto")
    spike = Perro(3, "Spike", "Canino", 75)
    lola = Vaca(4, "Lola", "Vacuno", 7)
    
    tom.se_mueve()
    spike.se_mueve()
    lola.se_mueve()

    tom.hace_sonido()
    spike.hace_sonido()
    lola.hace_sonido()

    # tom.hace_miau()
    # spike.hace_guau()
    # lola.hace_muuu()

    #Experimento
    #animal_1.hace_miau()
    #lola.hace_miau()

    tom.se_lava()
    spike.se_lava()