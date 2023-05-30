from abc import ABC, abstractmethod

class Animal(ABC):

    nombre:str
    especie:str

    def setAnimal(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def mostrar(self):
        print(f"El animal {self.nombre} es un {self.especie}...")

    @abstractmethod
    def hacer_sonido(self):
        pass