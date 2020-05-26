from discord.ext import commands

class Media(commands.Cog): # Membuat Cogs
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="Tidur") # Membuat Perintah Kbbi untuk Cogs
    async def kbbi(self, ctx, arg):
        if len(arg) > 0:
          try:
            data = KBBI(arg)
            await ctx.send("```Mencari Kata -> {}\n\n{}```".format(arg, data))
          except:await ctx.send("```Kata '{}' Tidak ditemukan dalam KBBI.```".format(arg))
        else:await ctx.send("Kata tidak boleh Kosong.")

def setup(bot): # Setup Cogs nya
    bot.add_cog(Media(bot))
