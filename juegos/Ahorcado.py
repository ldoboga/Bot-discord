def leer_archivos():
    ARCHIVOS = ('bin\\Cuentos.txt', 'La araña negra - tomo 1.txt', 'Las 1000 Noches y 1 Noche')
    VOCALES = [("a","á"),("e","é"),("i","í"),("o","ó"),("u","ú")]
    with open(ARCHIVOS[0], 'r') as f:
        data = ''
        for line in f:
            data += line.rstrip('\n')
                   
        for b,a in VOCALES:
            data = data.replace(a, b)
        data = data.lower()
        data = data.split()
    
    return data

def filtrar_lista(data):
    list = []
    for word in data:
        if len(word) >=5 and word.isalpha():
            list.append(word)
    return list

def crear_diccionario(list):
    dic_words = {}
    for i in list:
        dic_words[i] = dic_words.setdefault(i,0) + 1
    return dic_words

def palabras():
    list = leer_archivos()
    list = filtrar_lista(list)   
    dic_words = crear_diccionario(list)
    return dic_words



class Ahorcado():
    
    def __init__(self, game_over, jugador, server):
        self.game_over = game_over
        self.jugador = jugador
        self.server = server
        
    def cambiar_valores(self, game_over, jugador, server):
        self.game_over = game_over
        self.jugador = jugador
        self.server = server
        
    def quien_juega(self):
        return '<@' + str(self.jugador) + '> es el jugador de esta partida\n Que longitud de palabra deseas?'
    
  
  
