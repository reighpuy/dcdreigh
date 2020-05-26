from discord.ext import commands
from datetime import timedelta, date
from datetime import datetime
import time

bot = commands.Bot(command_prefix="!")
programStart = time.time()

@bot.event
async def on_ready():
    print('Program dengan Nama : {0.user} Berhasil dijalankan.'.format(bot))

async def on_message(message):
    print('{0.author}: {0.content}'.format(message))

@commands.command()
async def ping(ctx, elapse):
    start = time.time()
    #await ctx.send('Mengautentikasi...')
    elapse = time.time() - start
    await ctx.send('{}',format(elapse))
bot.add_command(ping)

@commands.command(description="Masukkan Kata", brief="Hello World")
async def says(ctx, *args):
    if len(args) > 0:
        await ctx.send(" ".join(args))
    else:await ctx.send("Kata tidak boleh Kosong.")
bot.add_command(says)

bot.run('Masukkan_Token_Bot_disini')