from discord.ext import commands
import os, sys, time

programStart = time.time()

def restartProgram():
    print ('Pesan Sistem: *Memulai Ulang Program.')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

class Umum(commands.Cog): # Membuat Cogs
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(description="Tidak dapat ditambahkan Apapun") # Membuat Perintah untuk Cogs
    async def halo(self, ctx):
        await ctx.send('hai')

    @commands.command(description="Masukkan Kata", brief="Hello World")
    async def say(self, ctx, *args):
        if len(args) > 0:
            await ctx.send(" ".join(args))
        else:await ctx.send("Kata tidak boleh Kosong.")

    @commands.command(description="Tidak dapat ditambahkan Apapun")
    async def relogin(self, ctx):
        await ctx.send('Memulai Ulang Program...')
        restartProgram()
    
    @commands.command(description="Tidak dapat ditambahkan Apapun")
    async def runtime(self, ctx):
        timeNow = time.time()
        runtime = timeNow - programStart
        runtime = timeChange(runtime)
        await ctx.send('{}'.format(runtime))

def setup(bot): # Setup Cogs nya
    bot.add_cog(Umum(bot))