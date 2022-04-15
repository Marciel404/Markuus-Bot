import asyncio
import discord
import config

from discord.ext import commands
from pymongo import MongoClient

cluster = MongoClient("#")

db = cluster["Bank"]

collection = db["Logs"]
collection2 = db["AutoRole"]
collection3 = db["Prefix"]

Game = discord.Game(name = f'Estou em desenvolvimento')
listening  =  discord.Activity(type = discord.ActivityType.listening, name = f"Futuras atualizações por vir")
stream = discord.Streaming(name = 'Meu criador', url = 'https://www.twitch.tv/mncoverz')
watching = discord.Activity(type = discord.ActivityType.watching, name = f'Meu criador fazendo novos codigos')

class events(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        print(f'EU entrei como {self.bot.user}')
        print(discord.__version__)
        while True:
            await self.bot.change_presence(status = discord.Status.online, activity = Game)
            await asyncio.sleep(10)
            await self.bot.change_presence(activity = listening)
            await asyncio.sleep(10)
            await self.bot.change_presence(activity = stream)
            await asyncio.sleep(10)
            await self.bot.change_presence(activity = watching)
            await asyncio.sleep(10)

    @commands.Cog.listener()
    async def on_message(self, message):

        prefix = collection3.find_one({"_id": message.guild.id})

        if message.author == self.bot.user: return

        if message.author.bot: return
        
        if message.author.id == config.banip:
            return
        elif message.mention_everyone:
            return
        elif self.bot.user.mentioned_in(message):
            if ' ' in message.content:
                return
            else:
                await message.reply('Meu prefixo nesse servidor é {0} , use {0}help para saber meus comandos'.format(prefix['prefix']))
        elif message:
            await set_prefix(message.guild, '==')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        user = self.bot.get_user(int(config.IdS))

        embed = discord.Embed(title = f':inbox_tray: | Entrada')
        embed.add_field(name = f':regional_indicator_s: | Nome do servidor:', value = guild.name, inline = False)
        embed.add_field(name = f':regional_indicator_i: | ID do servidor:', value = guild.id, inline = False)
        embed.add_field(name = f':regional_indicator_m: | Membros', value = len(guild.members), inline = False)
        embed.set_thumbnail(url = guild.icon_url)

        await user.send(embed = embed)
        await set_prefix(guild, '==')

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        server = {"_id": guild.id}

        collection.delete_one(server)
        collection2.delete_one(server)

        user = self.bot.get_user(int(config.IdS))

        embed = discord.Embed(title = f':inbox_tray: | Saida')
        embed.add_field(name = f':regional_indicator_s: | Nome do servidor:', value = guild.name, inline = False)
        embed.add_field(name = f':regional_indicator_i: | ID do servidor:', value = guild.id, inline = False)
        embed.add_field(name = f':regional_indicator_m: | Membros', value = len(guild.members), inline = False)
        embed.set_thumbnail(url = guild.icon_url)

        await user.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):

        try:
            r = collection2.find_one({"_id": member.guild.id})
            r1 = r["Role"]
        finally:
            role = discord.utils.get(member.guild.roles, name=f'{r1}')
            await member.add_roles(role)

async def set_prefix(id, prefix):
    user = {'_id': id.id, 'Nome': id.name, 'prefix': prefix}
    myquery = { "_id": id.id}   
    if (collection3.count_documents(myquery) == 0):

        collection3.insert_one(user)

def setup(bot:commands.Bot):
    bot.add_cog(events(bot))