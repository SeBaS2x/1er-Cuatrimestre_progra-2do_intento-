##1)
# altura = float(input("Ingrese su altura en cm: "))

# if altura < 160:
#     print("Su posicion es Base")
# elif altura >= 160 and altura <= 179:
#     print("Su posicion es Escolta")
# elif altura >= 180 and altura <= 199:
#     print("Su posicion es Alero")
# else:
#     print("Su posicion es Ala-pivot o Pivot")

##2)

import random 
nota = random.randint(1,10)
if nota >= 6:
    print(f"Promocion directa, la nota es {nota} ")
elif nota >=4 and nota <6:
    print(f"Aprobado, la nota es {nota}")
else:
    print(f"Desaprobado, la nota es {nota}")