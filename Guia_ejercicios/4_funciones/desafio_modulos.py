from validacion import*
# #1##

# def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)->int|None:
#     """Pide ingreso de numero entero y devuelve el numero si respeta los parametros y None cuando se termine los ca cantidad de intetnos.""

#     Args:
#         mensaje (str): mensaje para pedir el numero entero
#         mensaje_error (str): mensaje de error al no respetar los parametros
#         minimo (int): parametro minimo
#         maximo (int): parametro maximo
#         reintentos (int): Intentos 

#     Returns:
#         int|None  devuelve el numero ingresado o None en caso de que se terminen los intentos
#     """
#     while reintentos != 0:
#         dato_usuraio = int(input(mensaje))
#         if validate_number(dato_usuraio, minimo, maximo):
#             dato_valido = dato_usuraio
#             return dato_valido
#         else:
#             print(mensaje_error)
#             reintentos -= 1
#         # if dato_usuraio > minimo and dato_usuraio < maximo:
#         #     dato_valido = dato_usuraio
#         #     return dato_valido
#         #     break
#         # else:
#         #     print(mensaje_error)
#         #     reintentos -= 1

#     if reintentos == 0:
#         return None
        
    
# numero_entero= get_int("ingrese un numero respetando maximo y minimos : ", "Error al ingresar!!", 3, 200, 4)
# print(f"numero ingresado entero es: {numero_entero}")
    
# def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int)->float|None:
#     """Pide ingreso de numero Flotante y devuelve el numero si respeta los parametros y None cuando se termine los ca cantidad de intetnos.""
#     Args:
#         mensaje (str): ensaje para pedir el numero flotante
#         mensaje_error (str): mensaje de error al no respetar los parametros
#         minimo (float):  parametro minimo
#         maximo (float): parametro maximo_
#         reintentos (int): Intentos

#     Returns:
#         float|None: devuelve el numero ingresado o None en caso de que se terminen los intentos
#     """
#     while reintentos != 0:
#         dato_usuraio = float(input(mensaje))
#         if validate_number(dato_usuraio, minimo, maximo):
#             dato_valido = dato_usuraio
#             return dato_valido
#         else:
#             print(mensaje_error)
#             reintentos -= 1
#         # if dato_usuraio > minimo and dato_usuraio < maximo:
#         #     dato_valido = dato_usuraio
#         #     return dato_valido
#         #     break
#         # else:
#         #     print(mensaje_error)
#         #     reintentos -= 1

#     if reintentos == 0:
#         return None
        
    
# numero_flotante= get_float("ingrese un numero respetando maximo y minimos : ", "Error al ingresar!!", 3, 200, 4)
# print(f"numero ingresado flotante es: {numero_flotante}")


##2#########

def get_string(longitud: int)-> str|None:
    """_summary_

    Args:
        longitud (int): _description_

    Returns:
        str|None: _description_
    """
    string = input("Ingrese un una cadena respetando el limite: ")
    if validate_length(longitud, string):
        return string
    else:
        return None
    
caracteres = get_string(9)
print(caracteres)