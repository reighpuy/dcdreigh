import discord

COMMAND_PREFIX = "!" # Setkey/Prefix of Commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Bot : {0} has been Actived!'.format(self.user))

    async def on_message(self, message):
        print('[New Message] - From : {0.author} - Message : {0.content}'.format(message))
        if message.author.bot:
            return
        
        if message.content[0] != COMMAND_PREFIX:
            return

        cmd_args = message.content.split(" ")
        cmd = cmd_args[0]
        args = list()
        if len(cmd_args) > 1:
            args = cmd_args[1]

        if cmd == "!botsay":
            await message.channel.send(args)
        elif cmd == "!checkalive":
            await message.channel.send(f"Hi Sir {ctx.author.name}")

client = MyClient()
client.run('PUT_YOUR_BOT_TOKEN_HERE')
