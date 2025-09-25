suscripcion = input("\nEstandar\nPremium\ningrese el tipo de susucripcion: ")
antiguedad = int(input("Ingrese su antiguedad en años: "))
horas = float(input("Cantidad de horas cunsumidas diarias: "))
costo_hora = 1200 #mil docientos pesos la hora

print("--------------------")
costo_base = horas * costo_hora

porsentaje_plataforma = costo_base * 3 /100
impuesto_plataforma = costo_base + porsentaje_plataforma

porsentaje_licenciado =  costo_base * 11 / 100
impuesto_licenciado = costo_base + porsentaje_licenciado

bono_fidelidad = costo_base * 10 / 100
costo_final = costo_base + porsentaje_plataforma + porsentaje_licenciado - bono_fidelidad
print(f"Costo base: ${costo_base}")
print(f"Recargo por plataforma del 3%: ${porsentaje_plataforma}")
print(f"Recargo por Contenido Licenciado del 11%: ${porsentaje_licenciado}")
print(f"Bono de fidelidad del 10%: ${bono_fidelidad}")
print("--------------------")
print(f"Costo final a pagar: ${costo_final}")
if suscripcion == "premium" and antiguedad >= 15:
    print("Recibis Susucrpcion Gratuita por 1 año por tu fidelidad en estos años!")
else:
    print("Coodigo de descuento: AAFFXX")    