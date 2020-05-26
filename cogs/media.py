from discord.ext import commands

class Media(commands.Cog): # Membuat Cogs
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command() # Membuat Perintah untuk Cogs
    async def mantap(self, ctx):
        await ctx.send('hai')

def setup(bot): # Setup Cogs nya
    bot.add_cog(Media(bot))