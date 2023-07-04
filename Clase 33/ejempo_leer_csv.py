from Estudiante import Estudiante

if __name__ == "__main__":

    lista_estudiantes = []

    try: 
        registro = open("registro_personas.csv", "r")
        lineas = registro.readlines()
        for linea in lineas:
            dato = linea.split(",")
            id = int(dato[0].replace('"',''))
            nombre = dato[1].replace('"','')
            edad = int(dato[2].replace('"',''))
            carrera = dato[3].replace('"','')
            #print(f"id {id} nombre {nombre} edad {edad} carrera {carrera}")
            lista_estudiantes.append(Estudiante(id, nombre, edad, carrera))
        registro.close()
    except Exception as e:
        print(f"Error {e}")

    for estudiante in lista_estudiantes:
        print(estudiante)