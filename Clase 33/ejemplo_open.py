import os

if __name__ == "__main__":

    try:
        # Leer archivo de texto plano (.txt)
        # open("nombre_archivo.ext", modo)
        # "r" -> corresponde a lectura
        # modos extra 
        # "t" -> archivo de texto
        # "b" -> archivos binarios

        # Ruta Absoluta corresponde a toda la ruta desde la raiz del computador
        archivo = open("/Users/joelsebastiantorrescarrasco/Documents/Ulagos/POO/POO2023-1/Clase 33/archivo_1.txt", "rt", encoding="utf-8")
        # Ruta Relativa corresponde a la ruta desde el punto de ejecución
        #archivo = open("archivo_1.txt", "rt")
        print(archivo.read())

        # Al terminar el manejo del archivo
        archivo.close()
    except Exception as e:
        print(f"El archivo no se encuentra... {e}")

    # Escritura de archivo
    try:
        # modos escritura
        # "w" -> corresponde a la escritura de archivo, sino existe archivo, entonces lo crea - Sirve para sobreescribir
        #archivo = open("archivo_2.txt", "w")
        
        # "a" -> corresponde a la escritura al final del archivo, sino existe archivo, entonces lo crea - Sirve para guardar al final
        archivo = open("archivo_2.txt", "a")

        archivo.write("\n Se agrega al final del texto anterior.")
        archivo.close()

    except Exception as e:
        print(f"Problemas al escribir... {e}")

    #Crear archivo vacíos
    # "x" -> crear archivos vacíos

    try:
        #archivo = open("archivo_3.txt", "x")
        #archivo.close()
        print(" ")
        pass
    except Exception as e:
        print(f"El archivo no se encuentra... {e}")

    
    # Eliminar archivo

    try:
        #os.remove("archivo_3.txt")
        print(os.listdir()) # -> si quiero saber la lista de recursos en el directorio
    except Exception as e:
        print(f"El archivo no se encuentra... {e}")

