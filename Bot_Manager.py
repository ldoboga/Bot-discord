from juegos.Tateti4x4 import Tateti4x4
import discord
import datetime
from juegos.tateti import *
from juegos.Ahorcado import *
from discord import client
from discord.ext import commands

dic_tateti = {}
dic_ahorcado = {}
dic_tateti4 = {}

bot = commands.Bot(command_prefix = '>')

lista_ahorcado = palabras()
print(lista_ahorcado)

######### comandos tateti

@bot.command(aliases = ["t", "tictactoe"])
async def tateti(ctx, p2 : discord.Member):
    global dic_tateti
    dic_tateti.setdefault(ctx.guild.name, Tateti())
    if dic_tateti[ctx.guild.name].game_over:
        dic_tateti[ctx.guild.name].cambiar_valores(str(ctx.author.id), str(p2.id))
        if dic_tateti[ctx.guild.name].comprobaciones_tateti(p2.bot):
            await ctx.send(dic_tateti[ctx.guild.name].respuesta_tateti_bien())
        else:
            await ctx.send(dic_tateti[ctx.guild.name].respuesta_tateti_mal(p2.bot))
    else:
        await ctx.send('Ya hay una partida en curso')
    
@bot.command(aliases = ["p"])
async def place(ctx, pos : int):
    global dic_tateti
    dic_tateti.setdefault(ctx.guild.name, Tateti())
    if dic_tateti[ctx.guild.name].comprobar_place(str(ctx.author.id), pos):
        resultado , tablero = dic_tateti[ctx.guild.name].place(pos)
        for lines in tablero:
            await ctx.send(lines)
        await ctx.send(resultado)
    else:
        await ctx.send(dic_tateti[ctx.guild.name].resultados_place(str(ctx.author.id), pos))

@bot.command(aliases = ["yes", "si", "aceptar"])
async def y(ctx):
    global dic_tateti
    dic_tateti.setdefault(ctx.guild.name, Tateti())
    if dic_tateti[ctx.guild.name].comprobacion_yes(str(ctx.author.id)):
        for linea in dic_tateti[ctx.guild.name].imprimir_tablero_tateti():
            await ctx.send(linea)
        await ctx.send(dic_tateti[ctx.guild.name].turno_random())
    else:
        await ctx.send(dic_tateti[ctx.guild.name].resultado_yes(str(ctx.author.id)))

@bot.command(aliases = ["no", "cancelar"])
async def n(ctx):
    global dic_tateti
    dic_tateti.setdefault(ctx.guild.name, Tateti())
    if dic_tateti[ctx.guild.name].comprobacion_yes(str(ctx.author.id)):
        dic_tateti[ctx.guild.name].reset()
        await ctx.send('<@' + str(ctx.author.id) + '> se cago')
    else:
        await ctx.send(dic_tateti[ctx.guild.name].resultado_yes(str(ctx.author.id)))
        
@bot.command(aliases = ['rt'])
async def reset_tateti(ctx):
    global dic_tateti
    dic_tateti.setdefault(ctx.guild.name, Tateti())
    dic_tateti[ctx.guild.name].reset()
    await ctx.send('El juego se reseteo')
    
@tateti.error
async def tateti_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('menciona a una persona para este comando')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Tenes que mencionar al jugador')
        
@place.error
async def tateti_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('por favor ingrese una posición que le gustaría marcar')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('tenes que ingresar un numero entero chaval')    
    
######### comandos ahorcado

@bot.command(aliases = ['a'])
async def ahorcado(ctx):
    global dic_ahorcado
    dic_ahorcado.setdefault(ctx.guild.name, Ahorcado(True, ctx.author.id))
    if dic_ahorcado[ctx.guild.name].game_over:
        dic_ahorcado[ctx.guild.name].cambiar_valores(False, ctx.author.id)
        await ctx.send(dic_ahorcado[ctx.guild.name].quien_juega())
    else:
        await ctx.send('Ya hay una partida en juego')
     
@bot.command(aliases = ['l'])
async def longitud(ctx, longitud : int):   
    global dic_ahorcado
    dic_ahorcado.setdefault(ctx.guild.name, Ahorcado(True, ''))
    if dic_ahorcado[ctx.guild.name].comprobar_longitud(longitud, ctx.author.id):
        await ctx.send(dic_ahorcado[ctx.guild.name].palabras_por_longitud(longitud, lista_ahorcado))      
    else:
        await ctx.send(dic_ahorcado[ctx.guild.name].respuestas_longitud(longitud, ctx.author.id))
    print(dic_ahorcado[ctx.guild.name].palabra)
        
@bot.command(aliases = ['la'])
async def letra(ctx, letra : str):   
    global dic_ahorcado
    dic_ahorcado.setdefault(ctx.guild.name, Ahorcado(True, ''))
    if dic_ahorcado[ctx.guild.name].comprobar_letra(letra.lower(), ctx.author.id):
        await ctx.send(dic_ahorcado[ctx.guild.name].letra_en_palabra(letra.lower()))
        if dic_ahorcado[ctx.guild.name].comprobar_victoria():
            await ctx.send(dic_ahorcado[ctx.guild.name].ganar_o_perder())
    else:
        await ctx.send(dic_ahorcado[ctx.guild.name].respuesta_letra(letra.lower(), ctx.author.id))
        
@bot.command(aliases = ['ra'])
async def reset_ahorcado(ctx):
    global dic_ahorcado
    dic_ahorcado.setdefault(ctx.guild.name, Ahorcado(True, ''))
    dic_ahorcado[ctx.guild.name].reiniciar_valores()
    await ctx.send('El juego se reinicio. Vuelva a comenzar una partida')
        
@longitud.error
async def ahorcado_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Tiene que enviar una longitud')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('La longitud tiene que ser un numero')
        
@letra.error
async def ahorcado_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Por favor ingrese una letra')   
        
######### comandos tateti 4x4

@bot.command(aliases = ['t4', 'tictactoe4'])
async def tateti4(ctx, p2 : discord.Member):
    global dic_tateti4
    dic_tateti4.setdefault(ctx.guild.name, Tateti4x4())
    if dic_tateti4[ctx.guild.name].game_over:
        dic_tateti4[ctx.guild.name].cambiar_valores(str(ctx.author.id), str(p2.id))
        if dic_tateti4[ctx.guild.name].comprobaciones_tateti(p2.bot):
            await ctx.send(dic_tateti4[ctx.guild.name].respuesta_tateti_bien())
        else:
            await ctx.send(dic_tateti4[ctx.guild.name].respuesta_tateti_mal(p2.bot))
    else:
        await ctx.send('Ya hay una partida en curso')
    
@bot.command(aliases = ['y4'])
async def yes4(ctx):
    global dic_tateti4
    dic_tateti4.setdefault(ctx.guild.name, Tateti4x4())
    if dic_tateti4[ctx.guild.name].comprobacion_yes(str(ctx.author.id)):
        for linea in dic_tateti4[ctx.guild.name].imprimir_tablero_tateti():
            await ctx.send(linea)
        await ctx.send(dic_tateti4[ctx.guild.name].turno_random())
    else:
        await ctx.send(dic_tateti4[ctx.guild.name].resultado_yes(str(ctx.author.id)))
    
@bot.command(aliases = ['n4'])
async def no4(ctx):
    global dic_tateti4
    dic_tateti4.setdefault(ctx.guild.name, Tateti4x4())
    if dic_tateti4[ctx.guild.name].comprobacion_yes(str(ctx.author.id)):
        dic_tateti4[ctx.guild.name].reset()
        await ctx.send('<@' + str(ctx.author.id) + '> se cago')
    else:
        await ctx.send(dic_tateti4[ctx.guild.name].resultado_yes(str(ctx.author.id)))
    
@bot.command(aliases = ['p4'])
async def place4(ctx, pos : int):
    global dic_tateti4
    dic_tateti4.setdefault(ctx.guild.name, Tateti4x4())
    if dic_tateti4[ctx.guild.name].comprobar_place(str(ctx.author.id), pos):
        resultado , tablero = dic_tateti4[ctx.guild.name].place(pos)
        for lines in tablero:
            await ctx.send(lines)
        await ctx.send(resultado)
    else:
        await ctx.send(dic_tateti4[ctx.guild.name].resultados_place(str(ctx.author.id), pos))
        
@bot.command(aliases = ['rt4'])
async def reset_tateti_4x4(ctx):
    global dic_tateti4
    dic_tateti4.setdefault(ctx.guild.name, Tateti4x4())
    dic_tateti4[ctx.guild.name].reset()
    await ctx.send('El juego se reseteo')
    
@tateti4.error
async def tateti_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('menciona a una persona para este comando')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Tenes que mencionar al jugador')
        
@place4.error
async def tateti_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('por favor ingrese una posición que le gustaría marcar')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('tenes que ingresar un numero entero chaval') 
    
##############################################################
    
@bot.event
async def on_ready():
    print('Bot encendido')
    
bot.run('token')
