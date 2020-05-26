import discord

COMMAND_PREFIX = "!" # Ini Setkey, Pengawalan sebuah Perintah

class MyClient(discord.Client):
    async def on_ready(self):
        print('Bot dengan Nama : {0} Berhasil dijalankan!'.format(self.user))

    async def on_message(self, message):
        print('[Pesan Baru] - Dari : {0.author} - Pesan : {0.content}'.format(message))
        if message.author.bot:
            return
        
        if message.content[0] != COMMAND_PREFIX:
            return

        cmd_args = message.content.split(" ")
        cmd = cmd_args[0]
        args = list()
        if len(cmd_args) > 1:
            args = cmd_args[1]

        if cmd == "!say":
            await message.channel.send(args)
        elif cmd == "!ping":
            await message.channel.send("Pong")

client = MyClient()
client.run('Masukkan_Token_Bot_disini')