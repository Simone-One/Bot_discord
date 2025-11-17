import random
import ollama

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def genera_risposta(domanda):
    client = ollama.Client()
    model = "gemma3:4b"
    risposta = client.generate(model=model, prompt=domanda).response
    return risposta
