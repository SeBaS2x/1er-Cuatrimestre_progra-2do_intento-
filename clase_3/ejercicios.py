##1####

# numero = 1
# multiplo = 5
# while numero < 11 :
#     resultado = numero * multiplo
#     print(f"{numero} x {multiplo} = {resultado}" )
#     numero += 1

#2########

# contador = 0 
# numero = 1 

# while numero <= 50:
#     if numero % 2 == 0:
#         contador +=1
#     numero += 1
# print(contador)

#3####

# contador_pares = 0
# contador_impares = 0
# numeros = 0

# while numeros < 10:
#     numero_usuario = int(input("Ingrese un numero: "))
#     if numero_usuario % 2 == 0:
#         contador_pares += 1
#     else:
#         contador_impares += 1
#     numeros += 1 
# print(f"Cantidad de numeros pares : {contador_pares}")
# print(f"Cantidad de numeros impares : {contador_impares}")

#4#########
# contador = 0
# acumulador = 0
# ingreso = input("Quiere ingresar un numero o fin:")

# while ingreso != "fin":
#     acumulador += int(ingreso)
#     contador += 1
#     ingreso = input("Quiere ingresar un numero o fin:")
# promedio = acumulador / contador
# print(f"El promedio es: {promedio}")

#5###########
# n = 5
# acumulador = 1  
# while n > 1:
#     acumulador = acumulador * n
#     n -= 1
# print(acumulador)

#6#######
usuario = int(input("Ingrese un numero: "))
if usuario % usuario == 0 and usuario % 1 ==0:
    print(f"El numero {usuario}, es un numero primo ")
else:
    print(f"El numero {usuario}, es un numero No es primo ")
    
