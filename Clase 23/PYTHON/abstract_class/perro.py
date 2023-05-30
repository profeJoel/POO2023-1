from animal import Animal

class Perro(Animal):

    def __init__(self) -> None:
        super().__init__()
    

    def hacer_sonido(self):
        return "GUAUU..."