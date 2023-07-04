if __name__ == "__main__":

    try:
        # Leer archivo de texto plano (.txt)
        # open("nombre_archivo.ext", modo)
        # "r" -> corresponde a lectura
        archivo = open("/Users/joelsebastiantorrescarrasco/Documents/Ulagos/POO/POO2023-1/Clase 33/archivo_1.txt", "r")
        print(archivo.read())
    except Exception as e:
        print(f"El archivo no se encuentra... {e}")