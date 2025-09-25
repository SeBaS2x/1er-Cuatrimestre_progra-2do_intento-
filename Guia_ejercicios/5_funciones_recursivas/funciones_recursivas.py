
# def sumar_naturales(numero: int)-> int:
#     suma = 0
#     if numero == 0:
#         return 0
#     else:
#         suma += numero 
#         suma += sumar_naturales(numero-1)
#     return suma
    
    
# sumas_de_naturales = sumar_naturales(4)
# print(sumas_de_naturales)

##2###########

# def calcular_potencia(base: int, exponente: int)-> int:
#     potencia = 1
    
#     if exponente == 0:
#         return 1
#     else:
        
#         potencia *= base
#         potencia *= calcular_potencia(base , exponente-1) 
#     return potencia

# potencia = calcular_potencia(3,3)
# print(potencia)

##4###########

def calcular_fibonacci(numero: int)-> int:
    suma = 0
    
    if numero == 0 or numero== 1:
        return numero
    else:
       
        suma += calcular_fibonacci(numero-1)
        suma += calcular_fibonacci(numero-2)
    return suma

fibo = calcular_fibonacci(13)
print(fibo)