from dataclasses import dataclass

@dataclass
class Estudiante:
    id:int
    nombre:str
    edad:int
    carrera:str

    def __str__(self):
        return f"Estudiante {self.nombre} ({self.id}) de {self.edad} de la carrera {self.carrera}"