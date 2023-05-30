
def calcular_cuadrado(num):
    return num**2

if __name__ == "__main__":
    
    a = 2
    cuadrado = a*a
    #Operación Lambda > var_re = lambda params: expresion
    lambda_cuadrado = lambda num: num**2
    
    #print(f"el cuadrado de {a} es {cuadrado}")
    #print(f"el cuadrado de {a} es {calcular_cuadrado(a)}")
    print(f"el cuadrado de {a} es {lambda_cuadrado(a)}")