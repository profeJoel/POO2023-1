import datetime

from Hotel import Hotel
from Cliente import Cliente
from Habitacion import Habitacion
from Disponibilidad import Disponibilidad
from Reserva import Reserva


if __name__ == "__main__":

    hotel = Hotel(1, "Las Cascadas")

    hotel.agregar_habitacion(Habitacion(1, "Ejecutiva Individual", 30000, 2, 1))
    hotel.agregar_habitacion(Habitacion(2, "Ejecutiva Doble", 60000, 4, 2))

    hotel.habitaciones[0].agregar_disponibilidad(Disponibilidad(1,datetime.datetime(2023,5,2)))
    hotel.habitaciones[0].agregar_disponibilidad(Disponibilidad(1,datetime.datetime(2023,5,3)))
    hotel.habitaciones[0].agregar_disponibilidad(Disponibilidad(1,datetime.datetime(2023,5,3)))
    hotel.habitaciones[0].agregar_disponibilidad(Disponibilidad(1,datetime.datetime(2023,5,5)))


    hotel.habitaciones[1].agregar_disponibilidad(Disponibilidad(1,datetime.datetime(2023,5,2)))
    hotel.habitaciones[1].agregar_disponibilidad(Disponibilidad(1,datetime.datetime(2023,5,3)))
    hotel.habitaciones[1].agregar_disponibilidad(Disponibilidad(1,datetime.datetime(2023,5,3)))
    hotel.habitaciones[1].agregar_disponibilidad(Disponibilidad(1,datetime.datetime(2023,5,5)))

    hotel.agregar_cliente(Cliente(1, "1-9", "Casimiro", "Miraflores", "Buenavista", datetime.datetime(1990,5,3),1234567890))

    reserva = Reserva(1, datetime.datetime(2023,5,3), datetime.datetime(2023,5,5), hotel.clientes[0], hotel.habitaciones[1],3)

    #print(f"La reserva de don {reserva.pasajero.nombres} {reserva.pasajero.apellido_paterno} en la habitacion {reserva.habitacion.tipo} es desde el {reserva.fecha_inicio.strftime('%d/%m/%Y')} hasta {reserva.fecha_termino.strftime('%d/%m/%Y')} y tendra un valor de {reserva.total_estadia} pesos.")
    
    print(reserva)