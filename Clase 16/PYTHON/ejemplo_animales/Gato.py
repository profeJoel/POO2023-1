from Animal import Animal

class Gato(Animal):

    def __init__(self, id, nombre, especie, tipo_pelaje) -> None:
        super().__init__(id, nombre, especie)
        self.tipo_pelaje = tipo_pelaje
    
    def hace_miau(self):
        print(f"{self.nombre} hace MIAUUU!!!!")