def crear_lista(valor, cantidad):
    lista = [valor] * cantidad
    return lista

def mostrar_lista(lista)->list:
    for i in range(len(lista)):
        print(f"_ {lista[i]}")
def cargar_lista(lista:list, mensaje: str)->bool:
    bandera = False
    if type(lista)== list:
        for i in range(len(lista)):
            valor =int(input(mensaje))
            while validar_rango(valor, 1000, -1000) != True:
                valor =int(input(mensaje))
            lista[i]= valor
        bandera = True
    return bandera
##Agregar validacion de si es un numero

def validar_rango(valor:int, maximo:int, min:int)->bool:
    validacion = False
    if valor > min and valor < maximo:
        validacion = True
    return validacion


def contar_positivo_en_lista(lista:list)->int:
    contador_p = 0
    for i in range(len(lista)):
        if lista[i] >=0:
            contador_p +=1
    return contador_p
def contador_negativo_en_lista(lista:list)->int:
    contador_n = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            contador_n +=1
    return contador_n

def sumar_par(lista:list)->int:
    suma_par = 0
    for i in range(len(lista)):
        if es_par(lista[i]):
            suma_par += lista[i]
    return suma_par

def es_par(numero: int) -> bool:
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado
def es_impar(numero:int)-> bool:
    if numero % 2 != 0:
        impar = True
    else:
        impar = False
    return impar
# def sumar_impar(lista:list)->int:
#     suma_impar = 0
#     for i in range(len(lista)):
#         if es_impar(lista[i]):
#             suma_impar += lista[i]
#     return suma_impar

def mayor_impar_lista(lista:list)->int:
    mayor = False
    for i in range(len(lista)):
        if es_impar(lista[i]):
            if mayor == False:
                mayor = lista[i]
            elif mayor < lista[i]:
                mayor = lista[i]
    return mayor



def listar_posicion_impar(lista:list):
    for i in range(len(lista)):
        if es_impar(i +1):
            print(f"Los numeros en posiciones Impares son {lista[i]}")

def listar_pares(lista: list):
    for i in range(len(lista)):
        if es_par(lista[i]):
            print(lista[i])
            
