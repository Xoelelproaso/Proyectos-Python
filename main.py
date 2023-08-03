import discord,os,random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print(f"has iniciado sesión como {bot.user}")

@bot.command()
async def meme(ctx):
    imagenes_cargadas=random.choice(os.listdir("Clase 6\memes"))
    with open(f'Clase 6\memes\{imagenes_cargadas}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def reciclar(ctx):
    await ctx.send("Contenedor amarillo: Dentro del contenedor de color amarillo debemos depositar botellas y envases de plástico, envases metálicos (latas, bandejas de aluminio, aerosoles, botes de desodorante…) y briks. Es decir, es el contenedor perfecto para tirar ENVASES.\n\nContenedor azul: El contenedor azul es el destinado para envases de cartón y papel exclusivamente. Algunos de estos productos pueden ser envases de alimentación, calzado, productos congelados, papel para envolver o papel de uso diario.\n\nContenedor verde: En el contenedor verde debemos depositar botellas de vidrio, frascos de vidrio (como perfumes o colonias) y tarros de alimentos (mermeladas, conservas, etc).\n\nContenedor marrón (orgánico): En este contenedor deben depositarse los restos de alimentos como pieles de frutas, espinas de pescado, plantas, cáscaras de huevo o posos; o servilletas y papel de cocina usados.\n\nContenedor gris (restos): En este contenedor se depositan materiales como juguetes, biberones, chupetes, utensilios de cocina, pañales, objetos cerámicos, arena para mascotas, pelo, polvo, colillas, etc. Es decir, todo aquello que no puede ser reutilizado.")

@bot.command()
async def commands(ctx):
    await ctx.send("$reciclar\n$meme\n")

bot.run("Token")