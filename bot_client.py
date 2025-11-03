import discord
from gen_pass import *

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")
    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$domanda:'):
        await message.channel.send(genera_risposta(message.content))
    elif message.content.startswith('$genera_password'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)
        print(f"L'utente ha inviato: {message.content}")

client.run("TOKEN")
