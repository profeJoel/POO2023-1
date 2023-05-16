from Animal import Animal

class Vaca(Animal):

    def __init__(self, id, nombre, especie, n_estomagos) -> None:
        super().__init__(id, nombre, especie)
        self.n_estomagos = n_estomagos
    
    def hace_muuu(self):
        print(f"{self.nombre} hace MUUUUUUU!!!!")

    # Polimorfismo por inclusion
    def hace_sonido(self):
        self.hace_muuu()