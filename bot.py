from discord.ext import commands

bot = commands.Bot(command_prefix="!") # Ini Setkey, Pengawalan sebuah Perintah

@bot.event
async def on_ready():
    print('Bot dengan Nama : {0.user} Berhasil dijalankan.'.format(bot)) # Ini Akan ter print jika Berhasil Login

bot.load_extension(f'cogs.umum') # Membuka Folder Cogs lalu Membuka File umum.py
bot.load_extension(f'cogs.media') # Membuka Folder Cogs lalu Membuka File media.py

bot.run('Masukkan_Token_Bot_disini') # Token Bot Anda
