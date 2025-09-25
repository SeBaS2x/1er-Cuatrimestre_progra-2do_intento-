import random
def verificar_ganardor_ronda(jugador, maquina)-> str:
    """Verifica quien es ganador, se pasa las elecciones y se evaluan los casos en los que gana el jugador, pierde o empata 

    Args:
        jugador (_type_): eleccion del jugador en numeros
        maquina (_type_): eleccion de la maquina en numeros

    Returns:
        str: devuelve un Print indicando ganador o empate 
    """
    ganador  = 0
    if (jugador == 1 and maquina == 3) or (jugador == 3 and maquina == 2) or(jugador ==2 and maquina==1) :
        print("Jugador gana")
    elif (jugador == 1 and maquina==2) or(jugador == 3 and maquina == 1) or(jugador == 2 and maquina==3):
        print("Jugador Pierde. Maquina Gana")
    else:
        print("Empate")
        
# player = int(input("ingrese un numero .1 para Piedra .2 para Papel .3 para Tijera:  "))
# bot = random.randint(1,3)
# print(bot)
# verificar_ganardor_ronda(player, bot)
        
def verificar_estado_partida(aciertos_jugadro, aciertos_maquina, ronda_actual)->bool:
    """Verifica si los aciertos del jogaddor o la maquina son 2 o si se acabaron las rondas

    Args:
        aciertos_jugadro (_type_): cantidad aciertos jugador
        aciertos_maquina (_type_): cantidad aciertos maquina
        ronda_actual (_type_): cantidad de rondas restantes 

    Returns:
        bool: retorna un True en caso de que este en curso la ronda o False en caso contrario
    """
    encurso = True
    if ronda_actual <=3 and aciertos_jugadro < 2 and aciertos_maquina < 2:
        encurso = True
    else:
        encurso = False
    return encurso
# if verificar_estado_partida(1, 2, 3): Verificacion de funcion verificar estado partida
#     print("SE sigue")
# else:
#     print("no se sigue")
