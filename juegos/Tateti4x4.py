class Tateti4x4():
    
    GANAR = [(0,1,2,3), (4,5,6,7), (8,9,10,11), (12,13,14,15), (0,4,8,12), (1,5,9,13), (2,6,10,14), (3,7,11,15), (0,5,10,14), (3,6,9,12), (0,1,4,5), (2,3,6,7), (8,9,12,13), (10,11,14,15), (1,2,5,6), (9,10,13,14), (4,5,8,9), (6,7,10,11), (5,6,9,10)]
    
    def __init__(self, game_over, p1, p2):
        self.game_over = game_over
        self.player_1 = p1
        self.player_2 = p2
        self.turn = ''
        self.count = 0
        self.board = [
        ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:',
        ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:',
        ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:'
        ]
        
    def reset(self):
        self.game_over = True
        self.player_1 = ''
        self.player_2 = ''
        self.turn = ''
        self.count = 0
        self.board = [
        ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:',
        ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:',
        ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:'
        ]
        
    def comprobaciones_tateti(self):
        return 'Los participantes son <@' + self.player_1 + '> y <@' + self.player_2 + '>'