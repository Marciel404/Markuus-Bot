import asyncio
import discord

from discord.ext import commands
from Outhers.Random import IdS, banip, Game,listening,stream,watching
from Outhers.Moderate import logs, autorule, prefix

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

        prefixo = prefix.find_one({"_id": message.guild.id})

        if message.author == self.bot.user: return

        if message.author.bot: return
        
        if message.author.id == banip:
            return
        elif message.mention_everyone:
            return
        elif self.bot.user.mentioned_in(message):
            if ' ' in message.content:
                return
            else:
                await message.reply('Meu prefixo nesse servidor é {0} , use {0}help para saber meus comandos'.format(prefixo))
        elif message.content:

            await set_prefix(message.guild, '==')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        user = self.bot.get_user(int(IdS))

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

        logs.delete_one(server)
        prefix.delete_one(server)
        autorule.delete_one(server)

        user = self.bot.get_user(int(IdS))

        embed = discord.Embed(title = f':inbox_tray: | Saida')
        embed.add_field(name = f':regional_indicator_s: | Nome do servidor:', value = guild.name, inline = False)
        embed.add_field(name = f':regional_indicator_i: | ID do servidor:', value = guild.id, inline = False)
        embed.add_field(name = f':regional_indicator_m: | Membros', value = len(guild.members), inline = False)
        embed.set_thumbnail(url = guild.icon_url)

        await user.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):

        try:
            r = autorule.find_one({"_id": member.guild.id})
            r1 = r["Role"]
        finally:
            role = discord.utils.get(member.guild.roles, name=f'{r1}')
            await member.add_roles(role)

async def set_prefix(id, prefixo):
    user = {'_id': id.id, 'Nome': id.name, 'prefix': prefixo}
    myquery = { "_id": id.id}   
    if (prefix.count_documents(myquery) == 0):

        prefix.insert_one(user)

def setup(bot:commands.Bot):
    bot.add_cog(events(bot))