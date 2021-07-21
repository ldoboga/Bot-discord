import random

condiciones_para_ganar_tateti = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]




def juego_nuevo_tateti(diccionario, sv, autor, bot):
    if autor == diccionario[sv][2]:
        resultado = 'No podes jugar contra vos mismo'
    elif bot:
        resultado = 'No podes jugar contra un bot'
     
    if diccionario[sv][0] and autor != diccionario[sv][2] and not bot:
        resultado = 'Los participantes son <@' + str(diccionario[sv][1]) + '> y <@' + str(diccionario[sv][2])+ '>'
        diccionario[sv][0] = False
    return resultado, diccionario

def deseas_jugar_tateti(diccionario,sv):
    resultado = '<@' + str(diccionario[sv][2]) + '> aceptas el duelo de <@' + str(diccionario[sv][1]) + '> ? (>y/>n aceptar/cancelar)'
    return resultado
    
def aceptar_juego_tateti(diccionario, sv, user):
    tablero = [':white_large_square:', ':white_large_square:', ':white_large_square:',
         ':white_large_square:', ':white_large_square:', ':white_large_square:',
         ':white_large_square:', ':white_large_square:', ':white_large_square:'
        ]
    resultado = ''
    
    if diccionario[sv][0]:
        resultado = 'No hay ninguna partida en curso'
    elif diccionario[sv][2] != user:
        resultado = 'No eres el jugador que fue retado a la partida' 
    elif diccionario[sv][2] == user and not diccionario[sv][0] and diccionario[sv][5] == '':
        diccionario = turno_random_tateti(diccionario,sv)
        diccionario[sv][5] = tablero
        tablero = imprimir_tablero_tateti(diccionario[sv][5])
        resultado = 'El turno es de <@' + str(diccionario[sv][3]) + '>'
    if not diccionario[sv][0] and diccionario[sv][5] != '':
        resultado = 'Ya hay una partida en curso'
    return resultado, diccionario, tablero

def imprimir_tablero_tateti(board):
    line = ''
    lines = []
    for i in range(len(board)):
        if i == 2 or i == 5 or i == 8:
            line += ' ' + board[i]
            lines.append(line)
            line = ''
        else:
            line += ' ' + board[i]
    return lines

def turno_random_tateti(diccionario,sv):
    lista = []
    lista.append(diccionario[sv][1])
    lista.append(diccionario[sv][2])
    diccionario[sv][3] = random.choice(lista)
    return diccionario

def no_acepta_tateti(diccionario, sv, user):
    if diccionario[sv][0]:
        resultado = 'No hay ninguna partida en curso'
    elif diccionario[sv][2] != user:
        resultado = 'No eres el jugador que fue retado a la partida'  
    elif not diccionario[sv][0] and diccionario[sv][2] == user:
        resultado = '<@' + str(diccionario[sv][2]) + '> se cago'
        diccionario[sv][0] = True
        diccionario[sv][6] = False
        
    return resultado, diccionario

def jugar_tateti(diccionario, sv, user, pos):
    MIN_POSITION = 1
    MAX_POSITION = 9
    mark = ''
    tablero = ''
    
    if diccionario[sv][0]:
        resultado = 'Comienza una nueva partida'
    elif diccionario[sv][3] != user:
        resultado = 'No es tu turno'
    elif pos < MIN_POSITION or pos > MAX_POSITION:
        resultado = 'La posicion no es valida. escribe una posicion entre el 1 y 9'
    elif diccionario[sv][5][pos -1] != ':white_large_square:':
        resultado = 'Esa posicion ya fue utilizada'
        
    if not diccionario[sv][0] and diccionario[sv][3] == user and pos >= MIN_POSITION and pos <= MAX_POSITION and diccionario[sv][5][pos -1] == ':white_large_square:':
        if diccionario[sv][3] == diccionario[sv][1]:
            mark = ':o2:'
            diccionario[sv][5][pos - 1] = mark
            diccionario[sv][3] = diccionario[sv][2]
            tablero = imprimir_tablero_tateti(diccionario[sv][5])
            resultado = 'Es el turno de <@' + str(diccionario[sv][2]) + '>'
        elif diccionario[sv][3] == diccionario[sv][2]:
            mark = ':regional_indicator_x:'
            diccionario[sv][5][pos - 1] = mark
            diccionario[sv][3] = diccionario[sv][1]
            tablero = imprimir_tablero_tateti(diccionario[sv][5])
            resultado = 'Es el turno de <@' + str(diccionario[sv][1]) + '>'
        diccionario[sv][4] += 1
        
    if diccionario[sv][4] >= 9:
        resultado = 'Empataron pampus'
        diccionario = limpiar_tateti(diccionario, sv)
    elif ganar_tateti(diccionario, sv, mark)[sv][0]:
        if mark == ':o2:':
            resultado = 'El ganador es <@' + str(diccionario[sv][1]) + '>'
        elif mark == ':regional_indicator_x:':
            resultado = 'El ganador es <@' + str(diccionario[sv][2]) + '>'
        diccionario = limpiar_tateti(diccionario,sv)
        
    return resultado, diccionario, tablero

def ganar_tateti(diccionario, sv, mark):
    condiciones_para_ganar_tateti = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
    
    for condition in condiciones_para_ganar_tateti:
        if diccionario[sv][5] != '':
            if diccionario[sv][5][condition[0]] == mark and diccionario[sv][5][condition[1]] == mark and diccionario[sv][5][condition[2]] == mark:
                diccionario[sv][0] = True
      
    return diccionario

def limpiar_tateti(diccionario, sv):
    diccionario[sv][0] = True
    diccionario[sv][3] = ''
    diccionario[sv][4] = 0
    diccionario[sv][5] = ''
    diccionario[sv][6] = False
    return diccionario