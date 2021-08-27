import random

def leer_archivos():
    ARCHIVOS = ('bin\\Cuentos.txt', 'La araña negra - tomo 1.txt', 'Las 1000 Noches y 1 Noche')
    with open(ARCHIVOS[0], 'r') as f:
        lista = []
        data = ''
        for line in f:
            data = line.rstrip('\n').lower().split()
            if data == []:continue
            for i in data:
                lista.append(i)
    return ' '.join(lista)

def quitar_tildes(texto):
    VOCALES = [("a","á"),("e","é"),("i","í"),("o","ó"),("u","ú")]
    for b,a in VOCALES:
            texto = texto.replace(a, b)
    return texto.split()
    
def filtrar_lista(data):
    list = []
    for word in data:
        if len(word) >=5 and word.isalpha():
            list.append(word)
    return list

def crear_diccionario(lista):
    dic_words = {}
    for i in lista:
        dic_words[i] = dic_words.setdefault(i,0) + 1
        
    return list(dic_words.keys())

def palabras():
    texto = leer_archivos()
    lista = quitar_tildes(texto)
    lista = filtrar_lista(lista)   
    dic_words = crear_diccionario(lista)
    return dic_words

class Ahorcado():
    
    def __init__(self, game_over, jugador):
        self.game_over = game_over
        self.jugador = jugador
        self.palabra = ''
        self.palabra_adivinar = ''
        self.longitud = 0
        self.aciertos = 0
        self.desaciertos = 0
        self.p_usadas = []
        self.p_usadas_fallo = ''
        self.LONG_MIN = 5
        self.LONG_MAX = 16
        
    def cambiar_valores(self, game_over, jugador):
        self.game_over = game_over
        self.jugador = jugador
        
    def reiniciar_valores(self):
        self.game_over = True
        self.jugador = 'jugador'
        self.palabra = ''
        self.palabra_adivinar = ''
        self.longitud = 0
        self.aciertos = 0
        self.desaciertos = 0
        self.p_usadas = []
        self.p_usadas_fallo = ''
        self.LONG_MIN = 5
        self.LONG_MAX = 16
        
    def quien_juega(self):
        return '<@' + str(self.jugador) + '> es el jugador de esta partida\n Que longitud de palabra deseas?'
    
    def comprobar_longitud(self, long, user):
        return self.game_over == False and self.jugador == user and self.palabra == '' and long >= self.LONG_MIN and long <= self.LONG_MAX
  
    def palabras_por_longitud(self, long, lista):
        lista_long = []
        for i in lista:
            if len(i) == long:
                lista_long.append(i)
        self.palabra = random.choice(lista_long)
        self.palabra_adivinar = '?' * len(self.palabra)
        resultado = 'Palabra a adivinar: ' + str(self.palabra_adivinar) + ' | desaciertos: ' + str(self.desaciertos) + ' | aciertos: ' + str(self.aciertos)
        return resultado
        
    def respuestas_longitud(self, long, user):
        if self.game_over:
            resultado = 'Debes iniciar unar partida'
        elif self.jugador != user:
            resultado = 'No eres el jugador de esta partida'
        elif long < self.LONG_MIN or long > self.LONG_MAX:
            resultado = 'La longitud no es valida. ingresa una longitud entre 5 y 16'
        elif not self.game_over and self.palabra != '':
            resultado = 'Ya hay una partida en juego'
        return resultado
    
    def comprobar_letra(self, letra, user):
        return letra.isalpha() and self.jugador == user and not self.game_over and letra not in self.p_usadas and self.palabra != '' and len(letra) == 1
    
    def respuesta_letra(self, letra, user):
        if self.game_over:
            resultado = 'Debes iniciar unar partida'
        elif self.jugador != user:
            resultado = 'No eres el jugador de esta partida'
        elif not letra.isalpha():
            resultado = 'Tenes que enviar una letra no un numero'
        elif len(letra) != 1:
            resultado = 'Solo puede enviar una letra'
        elif letra in self.p_usadas:
            resultado = 'La letra ya esta en uso'
        elif self.palabra == '' and not self.game_over:
            resultado = 'Debes enviar una longitud antes de enviar una letra'
        return resultado
    
    def letra_en_palabra(self, letra):
        self.p_usadas.append(letra)
        
        contador = self.palabra.count(letra)
        self.palabra_adivinar = self.palabra_acierto(letra)
        print(self.palabra_adivinar)
        if contador == 0:
            self.p_usadas_fallo = self.p_usadas_fallo + letra + " - "
            self.desaciertos += 1
            resultado = "Lo siento!!! → " + str(self.palabra_adivinar) + " | Aciertos: " + str(self.aciertos) + " | Desaciertos: " + str(self.desaciertos) + " - " + str(self.p_usadas_fallo)
        elif contador > 0:
            self.aciertos += 1
            resultado = "Bien hecho!!! → " + str(self.palabra_adivinar) + " | Aciertos: " + str(self.aciertos) + " | Desaciertos: " + str(self.desaciertos) + " - " + str(self.p_usadas_fallo)
        return resultado
    
    def palabra_acierto(self, letra):
        palabra_aux = self.palabra_adivinar
        palabra_sin_adivinar = ""
        for i in range(len(self.palabra_adivinar)):
            if self.palabra[i] == letra:
                palabra_sin_adivinar += letra
            elif palabra_aux[i] != "?":
                palabra_sin_adivinar += palabra_aux[i]
            else:
                palabra_sin_adivinar += "?"
        return palabra_sin_adivinar
    
    def comprobar_victoria(self):
        return self.palabra == self.palabra_adivinar or self.desaciertos >= 8
    
    def ganar_o_perder(self):
        if self.palabra == self.palabra_adivinar:
            resultado = 'Felicidades <@' + str(self.jugador) +'> ganaste el juego'
            self.reiniciar_valores()
        elif self.desaciertos >= 8:
            resultado = 'Lo lamento <@' + str(self.jugador) + '> pero perdiste'
            self.reiniciar_valores()
        return resultado