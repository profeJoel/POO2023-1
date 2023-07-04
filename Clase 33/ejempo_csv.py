# formato CSV -> Valores separados por Coma
# ejemplo de clase -> Estudiante(id, nombre, edad, carrera)

if __name__ == "__main__":
    try:
        almacenamiento = open("registro_personas.csv", "a")
        almacenamiento.write('"0001", "Pepito", "20", "icinf"\n')
        almacenamiento.write('"0002", "Casimiro", "21", "cipol"\n')
        almacenamiento.write('"0003", "Lupita", "19", "enf"\n')

        almacenamiento.close()

    except Exception as e:
        print("Error al almacenar... {e}")