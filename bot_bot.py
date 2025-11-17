import discord
from discord.ext import commands
from gen_pass import *
import os
from script_importazioni_immagini import *

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f"Ciao!")

@bot.command()
async def arrivederci(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def domanda(ctx):
    await ctx.send(genera_risposta(ctx))

@bot.command()
async def genera_password(ctx, pass_lenght = 21):
    await ctx.send(gen_pass(pass_lenght))

@bot.command()
async def meme(ctx):
    await ctx.send(file=immagini_meme())

@bot.command('duck')
async def duck(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("TOKEN")
