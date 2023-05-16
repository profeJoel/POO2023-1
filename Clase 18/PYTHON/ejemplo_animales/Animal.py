class Animal:

    # Polimorfismo parametrico
    # parametros opcionales
    def __init__(self, id:int, nombre=None, especie=None):
        self.id = id
        self.nombre = nombre if nombre is not None else ""
        self.especie = especie if especie is not None else ""
    

    def se_mueve(self):
        if self.nombre == "":
            print(f"Animal X se mueve...")
        else:
            print(f"{self.nombre} se mueve...")

    def hace_sonido(self):
        if self.nombre == "":
            print(f"Animal X hace un sonido...")
        else:
            print(f"{self.nombre} hace un sonido...")