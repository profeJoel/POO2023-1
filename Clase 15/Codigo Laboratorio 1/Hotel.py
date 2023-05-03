from Habitacion import Habitacion
from Cliente import Cliente

class Hotel:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.personal = [] # list()
        self.habitaciones = []
        self.clientes = []

    def agregar_habitacion(self, h:Habitacion):
        self.habitaciones.append(h)

    def agregar_cliente(self, c:Cliente):
        self.clientes.append(c)

    