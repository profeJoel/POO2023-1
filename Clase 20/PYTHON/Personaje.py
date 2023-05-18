class Personaje:
    def __init__(self, id, nombre, vida, exp, poder):
        self.id = id
        self.nombre = nombre
        self.vida = vida
        self.exp = exp
        self.poder = poder

    def __str__(self):
        return f"Personaje {self.nombre}({self.id}) [vida={self.vida}, exp={self.exp}, poder={self.poder}]"

    def atacar(self):
        print(f"{self.nombre} está atacando...")