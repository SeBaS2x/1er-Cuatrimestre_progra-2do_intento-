from funciones import *
lista = crear_lista(None, 10)

bandera_menu = True
cantidad_ingresos = 0
while bandera_menu ==  True:
    print("1.Ingresar datos \n2.Cantidad de Positivos y Negativos \n3.Suma de Numeros Pares \n4.mayor numero impar \n5.Listar los numerso ingresados \n6.Listar Numeros Pares. \n7.Listar numeros en posiciones impares \n8.Salir")
    opciones =int(input("Ingresar Opciones: "))
    
    match opciones:
        case 1:
                print("**********************************")
                while cargar_lista(lista, "Ingresar un numero: ")!= True:
                    print("Error al cargar lista")
                print("**********************************")    
        case 2:
            print("**********************************")
            cantidad_positivo = contar_positivo_en_lista(lista)
            cantidad_negativo = contador_negativo_en_lista(lista)
            print(f"La cantidad de numeros Positivos son: {cantidad_positivo}")
            print(f"La cantidad de numeros Negativos son: {cantidad_negativo}")
            print("**********************************")
        case 3:
            print("**********************************")
            suma_par = sumar_par(lista)
            print(f"La suma de numeros Pares es: {suma_par}")
            print("**********************************")
        case 4:
            print("**********************************")
            n_impar_mayor = mayor_impar_lista(lista)
            print(f"El mayor numero Impar es {n_impar_mayor}")
            print("**********************************")
        case 5:
            print("**********************************")
            mostrar_lista(lista)
            print("**********************************")
        case 6:
            print("**********************************")
            print("Los numeros Pares Son...")
            listar_pares(lista)
            print("**********************************")
        case 7:
            print("**********************************")
            listar_posicion_impar(lista)
            print("**********************************")
        case 8:
            bandera_menu = False