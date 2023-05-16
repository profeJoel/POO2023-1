from Animal import Animal

class Gato(Animal):

    def __init__(self, id, nombre, especie, tipo_pelaje) -> None:
        super().__init__(id, nombre, especie)
        self.tipo_pelaje = tipo_pelaje
    
    def hace_miau(self):
        print(f"{self.nombre} hace MIAUUU!!!!")
    
    # Polimorfismo de Sobrecarga
    def se_lava(self):
        print(f"{self.nombre} se lava con su lengua...")
    
    # Polimorfismo por inclusion
    def hace_sonido(self):
        self.hace_miau()