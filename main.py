import discord

from bot_logic import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("See you soon!")
    elif message.content.startswith('$password'):
        await message.channel.send("Your password " + gen_pass(10))

client.run("MTEyOTA5MjU1MTc2MTIxOTcyNg.GKijTX.cMX294Qvjj3ItVUrhoqAkJCk_jShImniuT7xBg")