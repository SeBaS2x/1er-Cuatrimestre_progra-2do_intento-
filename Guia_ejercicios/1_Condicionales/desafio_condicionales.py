cargo_fijo = 7000 
costo_metro_cubico = 200 # 200 por metro cuadrado 
bonificacion = 0 
recargo = 0 
iva = 0.21
print("Bievenido!!")
print("-------------")
cliente = input("Indique el tipo de cliente: ")
metros_del_cliente = float(input("Ingresar cantidad de metros cuadrados: "))

subtotal = cargo_fijo +(costo_metro_cubico * metros_del_cliente)
print(f"Subtotal incluyendo el cargo figo: ${subtotal}")

if cliente == "residencial":
    if metros_del_cliente < 30:
        
        bonificacion += 0.1
        print(f"Se aplicara una bonificacion del: 10%")
    else:
        recargo += 0.15
        print("Se aplicara un recargo del: 15%")
elif cliente == "comercial":
    if metros_del_cliente > 300:
        bonificacion += 0.12
        print(f"Se aplicara una bonificacion del: 12%")    
    elif metros_del_cliente > 150:
        bonificacion += 0.08
        print(f"Se aplicara una bonificacion del: 8%")  
    else:
        recargo += 0.05
        print("Se aplicara un recargo del: 5%")
elif cliente == "industrial":
    if metros_del_cliente >1000:
        bonificacion += 0.3
        print(f"Se aplicara una bonificacion del: 30%")    
    elif metros_del_cliente > 500:
        bonificacion += 0.2
        print(f"Se aplicara una bonificacion del: 20%")  
    else:
        recargo += 0.1
        print("Se aplicara un recargo del: 10%")
        

if cliente == "residencial":
    if subtotal < 35000:
            bonificacion+= 0.05
            print("Se aplicara un Descuento adicionl del: 5%")
    
if bonificacion > 0 :
    porsentaje_bonifiacion = subtotal * bonificacion 
    aplicaicon_bonifiacion = subtotal - porsentaje_bonifiacion
    porsentaje_iva_b = aplicaicon_bonifiacion * iva
    aplicaicon_bonifiacion_iva= aplicaicon_bonifiacion + porsentaje_iva_b
    print(f"Subtotal con Bonificacion: ${aplicaicon_bonifiacion}")
    print(f"Subtotal a pagar con 21% de Iva: ${aplicaicon_bonifiacion_iva}")
    print("------------------------------")
    print(f"Totla final a pagar ${aplicaicon_bonifiacion_iva}")
if recargo > 0:
    porsentaje_recargo = subtotal * recargo 
    aplicaicon_recargo = subtotal + porsentaje_recargo
    porsentaje_iva_r = aplicaicon_recargo * iva
    aplicaicon_recargo_iva = aplicaicon_recargo + porsentaje_iva_r
    print(f"Subtotal con Recargo: ${aplicaicon_recargo}")
    print(f"Subtotal a pagar con 21% de Iva: ${aplicaicon_recargo_iva}")
    print("------------------------------")
    print(f"Total final a pagar: ${aplicaicon_recargo_iva}")