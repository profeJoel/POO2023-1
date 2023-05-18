from Personaje import Personaje
from Heroe import Heroe
from Villano import Villano
from Partida import Partida

if __name__ == "__main__":

    partida = Partida(Heroe(1,"Arturo", 100, 30, 10, 10), Villano(2, "Scar", 100, 50, 10, 5))

    partida.iniciar_partida()