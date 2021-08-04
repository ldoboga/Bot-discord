import random

# Declaracion de contantes
MIN_POSITION = 1
MAX_POSITION = 9
GANAR = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
TABLERO_LIMPIO = [
        ':white_large_square:', ':white_large_square:', ':white_large_square:',
        ':white_large_square:', ':white_large_square:', ':white_large_square:',
        ':white_large_square:', ':white_large_square:', ':white_large_square:'
        ]

# Declaracion de clase tateti
class Tateti():
    
    # Funcion constructora del objeto
    def __init__(self):
        self.game_over = True
        self.player_1 = ''
        self.player_2 = ''
        self.turn = ''
        self.count = 0
        self.board = TABLERO_LIMPIO

    # Funcion para resetear el juego    
    def reset(self):
        self.game_over = True
        self.player_1 = ''
        self.player_2 = ''
        self.turn = ''
        self.count = 0
        self.board = TABLERO_LIMPIO
        
    # Funcion para agregar los jugadores de la partida
    def cambiar_valores(self, p1, p2):
        self.player_1 = p1
        self.player_2 = p2
        
    # Funcion que comprueba las cosas necesarias para empezar una nueva partida
    def comprobaciones_tateti(self, bot):
        return self.game_over and self.player_2 != self.player_1 and not bot
    
    # Respuesta en caso de que la comprobacion de la funcion anterior sea correcta
    def respuesta_tateti_bien(self):
        self.game_over = False
        return 'Los participantes son <@' + self.player_1 + '> y <@' + self.player_2 + '>\n<@' + self.player_2 + '> aceptas el duelo de <@' + self.player_1 + '> (>y / >n aceptar/cancelar)'
        
    # Respuesta en caso de que la comprobacion de la funcion anterior sea incorrecta
    def respuesta_tateti_mal(self, bot):
        if bot:
            resultado = 'No podes jugar contra un bot'
        elif self.player_1 == self.player_2:
            resultado = 'No podes jugar contra vos mismo'
        return resultado
    
    # Funcion que comprueba que se cumplan las cosas necesarias para aceptar la partida
    def comprobacion_yes(self, p2):
        return not self.game_over and self.player_2 == p2 and self.turn == ''

    # Respuesta en caso de que la comprobacion de la funcion anterior sea incorrecta
    def resultado_yes(self, p2):
        if self.game_over:
            resultado = 'No hay ninguna partida en curso'
        elif self.turn != '':
            resultado = 'Ya hay una partida en curso'
        elif self.player_2 != p2:
            resultado = 'No eres el jugador que fue retado a la partida'
        return resultado
            
    # Funcion que elije un jugador aleatorio entre los dos jugadores para que tenga el primer turno
    def turno_random(self):
        lista = []
        lista.append(self.player_1)
        lista.append(self.player_2)
        self.turn = random.choice(lista)
        return 'El turno es de <@' + self.turn + '>'
    
    # Funcion que crea una lista para imprimir el tablero
    def imprimir_tablero_tateti(self):
        line = ''
        lines = []
        for i in range(len(self.board)):
            if i == 2 or i == 5 or i == 8:
                line += ' ' + self.board[i]
                lines.append(line)
                line = ''
            else:
                line += ' ' + self.board[i]
        return lines
    
    # Funcion que comprueba que se cumplan los requisitos para el comando place
    def comprobar_place(self, user, pos):
        return not self.game_over and self.turn == user and pos >= MIN_POSITION and pos <= MAX_POSITION and self.board[pos -1] == ':white_large_square:'
    
    # Respuesta en caso de que la comprobacion de la funcion anterior sea incorrecta
    def resultados_place(self, user, pos):
        if self.game_over:
            resultado = 'Comienza una nueva partida'
        elif self.turn != user:
            resultado = 'No es tu turno'
        elif pos < MIN_POSITION or pos > MAX_POSITION:
            resultado = 'La posicion no es valida. escribe una posicion entre el 1 y 16'
        elif self.board[pos -1] != ':white_large_square:':
            resultado = 'Esa posicion ya fue utilizada'
        return resultado
    
    # Funcion del comando place
    def place(self, pos):
        MAXICA_CANTIDAD_DE_POSICIONES = 9
        MARCA_JUGADOR_1 = ':o2:'
        MARCA_JUGADOR_2 = ':regional_indicator_x:'

        # pone la marca del jugador en la posicion que elijio y da el turno al otro jugador
        if self.turn == self.player_1:
            mark = MARCA_JUGADOR_1
            self.board[pos - 1] = mark
            self.turn = self.player_2
            tablero = self.imprimir_tablero_tateti()
            resultado = 'Es el turno de <@' + str(self.player_2) + '>'
        elif self.turn == self.player_2:
            mark = MARCA_JUGADOR_2
            self.board[pos - 1] = mark
            self.turn = self.player_1
            tablero = self.imprimir_tablero_tateti()
            resultado = 'Es el turno de <@' + str(self.player_1) + '>'
        self.count += 1
        
        self.ganar(mark)
        
        # En caso de que se cumpla la condicion se empata
        if self.count >= MAXICA_CANTIDAD_DE_POSICIONES:
            resultado = 'Empataron pampus'
            self.reset()
        # Segun el jugador que gana envia la respuesta y reinicia el jeugo
        elif self.game_over and mark == ':o2:':
            resultado = 'El ganador es <@' + str(self.player_1) + '>'
            self.reset()
        elif self.game_over and mark == ':regional_indicator_x:':
            resultado = 'El ganador es <@' + str(self.player_2) + '>'
            self.reset()
            
        return resultado, tablero
    
    # Funcion que comprueba si algun jugador gano la partida
    def ganar(self, mark):
        for condition in GANAR:
            print(condition)
            if self.board[condition[0]] == mark and self.board[condition[1]] == mark and self.board[condition[2]] == mark:
                self.game_over = True