from Animal import Animal

class Perro(Animal):

    def __init__(self, id, nombre, especie, poder_mandibula) -> None:
        super().__init__(id, nombre, especie)
        self.poder_mandibula = poder_mandibula
    
    def hace_guau(self):
        print(f"{self.nombre} hace GUAUUUU!!!!")