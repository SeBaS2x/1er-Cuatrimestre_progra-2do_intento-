# ##1########
# for i in range(1, 11):
#     print(i, end=" ")
# print(end=" ")
# ##2###########
# for i in range(10, 0, -1):
#     print(i, end=" ")

##3########
# numero = int(input("Ingrese un numero:"))
# for i in range(0, numero+1, +1):    
#     print(i)

#4######
# numero = int(input("Ingrese un numero"))

# for i in range(1,11):
#     multiplicacion = numero * i
#     print(f"{numero} x {i} = {multiplicacion}")
#5###
# suma = 0
# contador = 0
# for _ in range (10):
#     numero = int(input("Ingrese un numero o 0 para salir: "))
#     if numero == 0:
#         break
#     suma += numero
#     contador += 1
    
# promedio = suma / contador
# print(f"Cantidad de numeros ingresados, {contador}")
# print(f"Suma total {suma}")
# print(f"promedio: {promedio}")

#6###
# for i in range(1, 10):
#     if i % 3 == 0:
#         print(i)
    
#7####3
# for i in range(1,51):
#     if i % 2== 0:
#         print(i)

##8#############
# numero = int(input("Ingresar un numero: "))
# for i in range(1, numero + 1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()

##9 
numero =  int(input("Ingresar un numero: "))
contador = 0
for i in range(1, numero+1):
    if numero % i == 0:
        contador +=1
        print(f"divisores {i}")
print(f"Cantidad de divisores encontrados: {contador}")
#10##########
# numero = int(input("Ingrese un numero: "))
# encontro = False
# for i in range(1, numero +1):
#     if numero % 1== 0 and numero % i == 0:
#         encontro = True
        
# if encontro == True:
#     print(f"{numero}, es primo")
    

