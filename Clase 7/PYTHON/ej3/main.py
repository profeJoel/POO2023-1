

def imprimir_matriz(m):
    for i in range(3):
        for j in range(3):
            print(m[i][j], end=" ")
        print(" ")

def ingreso_matriz(m):
    for i in range(3):
        for j in range(3):
            m[i][j] = int(input(f"Ingrese el valor de [{i},{j}]"))

def verificar_cubo_magico(m):
    suma_f0 = 0
    suma_f1 = 0
    suma_f2 = 0
    suma_c0 = 0
    suma_c1 = 0
    suma_c2 = 0
    suma_d1 = 0
    suma_d2 = 0

    for i in range(3):
        for j in range(3):
            #filas
            if i == 0: suma_f0 += m[i][j]
            if i == 1: suma_f1 += m[i][j]
            if i == 2: suma_f2 += m[i][j]

            #columnas
            if j == 0: suma_c0 += m[i][j]
            if j == 1: suma_c1 += m[i][j]
            if j == 2: suma_c2 += m[i][j]

            #diagonales
            if i == j: suma_d1 += m[i][j]
            if i + j == 2: suma_d2 += m[i][j]
    
    if suma_f0 == suma_f1 and suma_f1 == suma_f2 and suma_f2 == suma_c0 and suma_c0 == suma_c1 and suma_c1 == suma_c2 and suma_c2 == suma_d1 and suma_d1 == suma_d2:
        print("Si, el cubo es magico!!!")
    else:
        print("No, no es magico")


if __name__ == "__main__":
    # declaracion explicita
    # cubo = [[1,2,3],[4,5,6],[7,8,9]]
    #cubo = [[,,],[,,],[,,]]

    #Declaracion matriz vacia
    #cubo = []
    #for i in range(3):
    #    cubo.append([0]*3)
    
    # Declaracion simple
    columnas = 3
    filas = 3
    cubo = [[0] * columnas for i in range(filas)]

    ingreso_matriz(cubo)
    imprimir_matriz(cubo)
    verificar_cubo_magico(cubo)