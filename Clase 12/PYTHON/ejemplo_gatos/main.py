# Es obligatorio importar los codigos que se utilizaran de cada clase

from Gato import Gato # desde el archivo Gato.py carga el codigo de la clase Gato

if __name__ == "__main__":
    oscar = Gato("Oscar", "macho", 5, 7, "marron", "rayado")
    oscar.meow()
    luna = Gato("Luna", "hembra", 2, 5, "gris", "lisa")
    luna.purr()
    print(f"Los gatos se llaman {oscar.name} y {luna.name}")