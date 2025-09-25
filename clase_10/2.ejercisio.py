lista_n = [5,3,8,5,9,5,3]
print(lista_n)
def cambiar_numero(lista, numero_a_cambiar, remplazo, todo = True)-> list:
    if todo == True:
        lista[0] = remplazo
    else:
        for i in range(len(lista)):
            if lista[i] == numero_a_cambiar:
                lista[i] = remplazo
    return lista

lista_2 = cambiar_numero(lista_n, 5, 2)

print(f"LIsta cambiada {lista_2}")