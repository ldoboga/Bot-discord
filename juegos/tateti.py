import random

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

class Tateti():
    
    def __init__(self):
        self.game_over = True
        self.player_1 = ''
        self.player_2 = ''
        self.turn = ''
        self.count = 0
        self.board = TABLERO_LIMPIO
        
    def reset(self):
        self.game_over = True
        self.player_1 = ''
        self.player_2 = ''
        self.turn = ''
        self.count = 0
        self.board = TABLERO_LIMPIO
        
    def cambiar_valores(self, p1, p2):
        self.player_1 = p1
        self.player_2 = p2
        
    def comprobaciones_tateti(self, bot):
        return self.game_over and self.player_2 != self.player_1 and not bot
    
    def respuesta_tateti_bien(self):
        self.game_over = False
        return 'Los participantes son <@' + self.player_1 + '> y <@' + self.player_2 + '>\n<@' + self.player_2 + '> aceptas el duelo de <@' + self.player_1 + '> (>y / >n aceptar/cancelar)'
        
    def respuesta_tateti_mal(self, bot):
        if bot:
            resultado = 'No podes jugar contra un bot'
        elif self.player_1 == self.player_2:
            resultado = 'No podes jugar contra vos mismo'
        return resultado
    
    def comprobacion_yes(self, p2):
        return not self.game_over and self.player_2 == p2 and self.turn == ''
    
    def resultado_yes(self, p2):
        if self.game_over:
            resultado = 'No hay ninguna partida en curso'
        elif self.turn != '':
            resultado = 'Ya hay una partida en curso'
        elif self.player_2 != p2:
            resultado = 'No eres el jugador que fue retado a la partida'
        return resultado
            
    def turno_random(self):
        lista = []
        lista.append(self.player_1)
        lista.append(self.player_2)
        self.turn = random.choice(lista)
        return 'El turno es de <@' + self.turn + '>'
    
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
    
    def comprobar_place(self, user, pos):
        return not self.game_over and self.turn == user and pos >= MIN_POSITION and pos <= MAX_POSITION and self.board[pos -1] == ':white_large_square:'
    
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
    
    def place(self, pos):
        
        if self.turn == self.player_1:
            mark = ':o2:'
            self.board[pos - 1] = mark
            self.turn = self.player_2
            tablero = self.imprimir_tablero_tateti()
            resultado = 'Es el turno de <@' + str(self.player_2) + '>'
        elif self.turn == self.player_2:
            mark = ':regional_indicator_x:'
            self.board[pos - 1] = mark
            self.turn = self.player_1
            tablero = self.imprimir_tablero_tateti()
            resultado = 'Es el turno de <@' + str(self.player_1) + '>'
        self.count += 1
        
        self.ganar(mark)
        
        if self.count >= 9:
            resultado = 'Empataron pampus'
            self.reset()
        elif self.game_over and mark == ':o2:':
            resultado = 'El ganador es <@' + str(self.player_1) + '>'
            self.reset()
        elif self.game_over and mark == ':regional_indicator_x:':
            resultado = 'El ganador es <@' + str(self.player_2) + '>'
            self.reset()
            
        return resultado, tablero
    
    def ganar(self, mark):
        for condition in GANAR:
            print(condition)
            if self.board[condition[0]] == mark and self.board[condition[1]] == mark and self.board[condition[2]] == mark:
                self.game_over = True