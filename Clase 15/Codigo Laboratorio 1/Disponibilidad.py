class Disponibilidad:

    def __init__(self, id, fecha):
        self.id = id
        self.fecha = fecha
        self.estado = True

    def reservar(self):
        self.estado = False
    
    def habilitar(self):
        self.estado = True