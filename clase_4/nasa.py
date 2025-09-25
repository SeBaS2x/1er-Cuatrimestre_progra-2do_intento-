sumatoria_velocidad_platillo = 0
sumatoria_velocidad_esferica = 0
sumatoria_velocidad_ovalada = 0
contador_platillo = 0
contador_esferica = 0
contador_ovalada = 0

seguir = input ("Quiere ingresar un Avistamiento (si-no)?: ")


while seguir == "si":

        nombre_empleado = input("Ingrese Nombre del empleado: ")
        forma_nave = input("ingrese la forma de la nave(platillo, esferica, u ovalada?:  ) ")
        while forma_nave != "platillo" and forma_nave != "esferica" and forma_nave!= "ovalada": #es distinta en validaciones combiene poner si es diferente a las opciones a elejir 
                forma_nave = input("ingrese la forma de la nave(platillo, esferica, u ovalada?:  ) ")
        velocidad = float(input("reingrese la velociidad de la nave km: "))
        while velocidad <= 100:
                velocidad = float(input("reingrese la velociidad de la nave km: "))
        tipo_mensaje = input("Tipo de mensaje (Ninguno - Claro - incomprensible): ")
        while tipo_mensaje != "ninguno" and tipo_mensaje != "claro" and tipo_mensaje!= "incomprensible": 
                tipo_mensaje = input("Tipo de mensaje (Ninguno - Claro - incomprensible): ")

        
        # Velocidad promedio según la forma de la nave
        match forma_nave:
                case "platillo":
                        sumatoria_velocidad_platillo += velocidad
                        contador_platillo += 1
                case "esferica":
                        sumatoria_velocidad_esferica += velocidad
                        contador_esferica += 1
                case "ovalada":
                        sumatoria_velocidad_ovalada += velocidad
                        contador_ovalada += 1
        
        seguir = input ("Quiere ingresar un Avistamiento (si-no)?: ")
        
        
if contador_platillo != 0:
        promedio_platillo = sumatoria_velocidad_platillo / contador_platillo
        print(f"La velocidad promedio de los Platillos fueron de {promedio_platillo}km/h")
else:
        print("No se ingreso tipo de nave platillo.")
if contador_esferica != 0:
        promedio_esferico = sumatoria_velocidad_esferica / contador_esferica
        print(f"La velocidad promedio de los esferica fueron de {promedio_esferico}km/h")
else:
        print("No se ingreso tipo de nave esferica.")
if contador_ovalada != 0:
        promedio_ovalada = sumatoria_velocidad_ovalada / contador_ovalada
        print(f"La velocidad promedio de los ovalada fueron de {promedio_ovalada}km/h")
else:
        print("No se ingreso tipo de nave ovalada.")