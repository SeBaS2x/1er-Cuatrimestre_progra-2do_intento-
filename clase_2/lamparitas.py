lampara = 7500
cantidad_lamparas = int(input("Ingrese la cantidad de Lamparitas que necesita: "))
marca = input("Ingrese la marca: ")
descuento = 0
ingresos_brutos = 0.10

if cantidad_lamparas >= 6 :
    descuento += 0.50
elif cantidad_lamparas == 5 : 
    if marca == "argentinaluz":
        descuento += 0.40
    else:
        descuento += 0.30
elif cantidad_lamparas == 4:
    if marca== "argentinaluz" or marca == "felipelamparas":
        descuento += 0.25
    else:
        descuento += 0.20
elif cantidad_lamparas == 3:
    if marca == "argentinaluz":
        descuento += 0.15
    elif marca == "felipelamparas":
        descuento += 0.1
    else:
        descuento += 0.05
