from animal import Animal

class Gato(Animal):

    def __init__(self) -> None:
        super().__init__()

    def hacer_sonido(self):
        return "MIUUU.."
    