import datetime
from Cliente import Cliente
from Habitacion import Habitacion

class Reserva:

    def __init__(self, id, fecha_inicio, fecha_termino, pasajero:Cliente, habitacion:Habitacion, cantidad_pasajeros):
        self.id = id
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.pasajero = pasajero
        self.habitacion = habitacion
        self.cantidad_pasajeros = cantidad_pasajeros
        self.total_estadia = self.calcular_estadia()

    def calcular_estadia(self):
        cantidad_dias = self.fecha_termino - self.fecha_inicio # mejorarlo
        #print(f"Cantidad de dias: {cantidad_dias.days}")
        return (cantidad_dias * self.habitacion.precio).days

    def __str__(self):
        return f"La reserva de don {self.pasajero.nombres} {self.pasajero.apellido_paterno} en la habitacion {self.habitacion.tipo} es desde el {self.fecha_inicio.strftime('%d/%m/%Y')} hasta {self.fecha_termino.strftime('%d/%m/%Y')} y tendra un valor de {self.total_estadia} pesos."