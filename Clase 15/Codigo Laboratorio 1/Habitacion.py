import datetime
from Disponibilidad import Disponibilidad

class Habitacion:

    def __init__(self, id, tipo, precio, capacidad_maxima, capacidad_recomendada):
        self.id = id
        self.tipo = tipo
        self.precio = precio
        self.capacidad_maxima = capacidad_maxima
        self.capacidad_recomendada = capacidad_recomendada
        self.disponibilidad = []

    def agregar_disponibilidad(self, d: Disponibilidad):
        self.disponibilidad.append(d)

    def verificar_disponibilidad(self, fecha_inicio, fecha_termino):
        fecha_actual = datetime.datetime.now()
        if fecha_inicio >= fecha_actual and fecha_termino > fecha_inicio:
            for dis in self.disponibilidad:
                if dis.fecha >= fecha_inicio and dis.fecha <= fecha_termino and dis.estado == True:
                    return True
                else:
                    return False
            return False
        else:
            return False
            
    