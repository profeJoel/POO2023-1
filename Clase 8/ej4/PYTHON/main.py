def contar_letras(p:str):
    #for i in range(p.__len__()):
    #    print(p[i])
    return p.__len__()

if __name__ == "__main__":
    palabra = "programacion"
    print(f"La palabra es: {palabra}")
    print(f"La palabra tiene {contar_letras(palabra)} letras")
