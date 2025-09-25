print("Bienvenidos")
print("------------")
estacion = input("Ingrese la estacion del año que quiere viajar: ")
lugar = input("Bariloche - Mar del plata - Catamarca -Futuro destino:  ")

match estacion:
    case "invierno":
        if lugar == "bariloche":
            print("Se viaja!!!")
        else:
            print("Solo se viaja a Bariloche. No se viaja.")
    case "verano":
        if lugar == "mar del plata" or lugar == "catamarca":
            print("Se viaja!!!")
        else:
            print("No se viaja")
    case "otoño":
        print("Se viaja")
    case "primavera":
        if lugar == "bariloche":
            print("No se viaja.")
        else:
            print("Se viaja a todos los lugares!!!")