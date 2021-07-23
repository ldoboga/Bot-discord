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
    dic_tateti.setdefault(ctx.guild.name,[True, ctx.author.id, p2.id, '', 0, '',False])
    if dic_tateti[ctx.guild.name][0]:
        dic_tateti[ctx.guild.name][1] = ctx.author.id
        dic_tateti[ctx.guild.name][2] = p2.id
        resultado, dic_tateti = juego_nuevo_tateti(dic_tateti, ctx.guild.name, ctx.author.id, p2.bot)
        await ctx.send(resultado)
        if not dic_tateti[ctx.guild.name][0] and ctx.author.id != dic_tateti[ctx.guild.name][2] and not p2.bot:
            resultado = deseas_jugar_tateti(dic_tateti, ctx.guild.name)
            await ctx.send(resultado)
    else:
        await ctx.send('Ya hay una partida en juego')
    print(dic_tateti)
    
@bot.command(aliases = ["p"])
async def place(ctx, pos : int):
    global dic_tateti
    dic_tateti.setdefault(ctx.guild.name,[True, '', '', '', 0, '',False])
    resultado, dic_tateti, tablero = jugar_tateti(dic_tateti, ctx.guild.name, ctx.author.id, pos)
    for i in tablero:
        await ctx.send(i)
    await ctx.send(resultado)

@bot.command(aliases = ["yes", "si", "aceptar"])
async def y(ctx):
    global dic_tateti
    dic_tateti.setdefault(ctx.guild.name,[True, '', '', '', 0, '',False])
    resultado, dic_tateti, tablero = aceptar_juego_tateti(dic_tateti,ctx.guild.name,ctx.author.id)
    if dic_tateti[ctx.guild.name][5] != '' and not dic_tateti[ctx.guild.name][6]:
        for line in tablero:
            await ctx.send(line)
        dic_tateti[ctx.guild.name][6] = True
        
    print(dic_tateti)
    await ctx.send(resultado)

@bot.command(aliases = ["no", "cancelar"])
async def n(ctx):
    global dic_tateti
    dic_tateti.setdefault(ctx.guild.name,[True, '', '', '', 0, '',False])
    resultado, dic_tateti = no_acepta_tateti(dic_tateti, ctx.guild.name, ctx.author.id)
    await ctx.send(resultado)
    
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


######### comandos ahorcado


@bot.event
async def on_ready():
    print('Bot encendido')
    
bot.run('ODY0OTg1NDE3MzM3Mjc0Mzk5.YO9acg.kQr01qTlYVYeEbYs9MRhf_AMoU8')