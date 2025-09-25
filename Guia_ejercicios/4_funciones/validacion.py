def validate_number(numero, minimo, maximo)->True|False:
    """valida un numero si resperta el minimo y maximo ingresado y devuelve True

    Args:
        numero (_type_): nuemor a validad int o float
        minimo (_type_): parametro minimo
        maximo (_type_): Parametro maximo

    Returns:
        True|False: Devuelve valores booleanos_
    """
    if numero > minimo and numero < maximo:
            return True
    else:
        return False
    
def validate_length(longitud, palabra):
    longitud_palabra = len(palabra)
    if longitud_palabra == longitud:
        return True
    else:
        return None
