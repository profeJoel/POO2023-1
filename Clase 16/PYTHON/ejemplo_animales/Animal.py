class Animal:

    def __init__(self, id, nombre, especie):
        self.id = id
        self.nombre = nombre
        self.especie = especie

    def se_mueve(self):
        print(f"{self.nombre} se mueve...")

    def hace_sonido(self):
        print(f"{self.nombre} hace un sonido...")