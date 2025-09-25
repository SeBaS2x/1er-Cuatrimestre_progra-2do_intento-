

limite = 0 #cantidad de ingreso de empleados
masculinos_voto_ia_iot = 0 
empleados_no_votaron_ia = 0
maxima_edad = 0


while limite < 5:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        print("Edad Incorrecta!!")
        edad = int(input("Ingrese su edad: "))
    genero = input("Identifique su genero: masculino/femenino/otro: ")
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input("Identifique su genero: masculino/femenino/otro: ")
    tecnologia = input("Elija una tecnologia : IA-RV/RA-IOT:  ")
    while tecnologia!="ia" and tecnologia!="rv/ra" and tecnologia != "iot":
        tecnologia = input("Elija una tecnologia : IA-RV/RA-IOT:  ")
    limite += 1
    
    if genero == "masculino" and(tecnologia =="iot" or tecnologia == "ia"):
        if edad >=25 and edad <=50:
            masculinos_voto_ia_iot += 1
    
    if genero == "masculino" or genero =="otro":
        if edad > 33 and edad < 40 and tecnologia!="ia":
            empleados_no_votaron_ia += 1
    
    if genero == "masculino":
        if edad > maxima_edad:
            maxima_edad = edad
            nombre_maximo = nombre
            voto_maximo = tecnologia
            
porsentaje_no_votos_ia = (empleados_no_votaron_ia * 100) / limite
print(f"Cantidad de empleados Masculino que votaron por IOT o IA de entre 25 y 50 años es: {masculinos_voto_ia_iot}.")            
print(f"El porsentaje de empleados que NO votaron por IA sin incluir al genero femendino edad entre 33 y 40 años es del: {porsentaje_no_votos_ia}%% ")
print(f"El empleado con mayor edad masculino es: {nombre_maximo} con {maxima_edad} años, vatando {voto_maximo}.")
print("-----------------------------------------------------------------------------------------")
