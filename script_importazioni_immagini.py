import requests
import os
import random
import discord

def immagini_meme():
    tutto = os.listdir('images')
    img = random.choice(tutto)
    with open(f"images/{img}", "rb") as file:
        meme = discord.File(file)
    return meme

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
