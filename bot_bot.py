import discord
from discord.ext import commands
from gen_pass import *

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

bot.run("TOKEN")
