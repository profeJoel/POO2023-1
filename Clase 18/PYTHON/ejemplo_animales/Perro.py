from Animal import Animal

class Perro(Animal):

    def __init__(self, id, nombre, especie, poder_mandibula) -> None:
        super().__init__(id, nombre, especie)
        self.poder_mandibula = poder_mandibula
    
    def hace_guau(self):
        print(f"{self.nombre} hace GUAUUUU!!!!")

    # Polimorfismo por Sobrecarga
    def se_lava(self):
        print(f"{self.nombre} se lava en una tina...")
    
    # Polimorfismo por inclusion
    def hace_sonido(self):
        self.hace_guau()