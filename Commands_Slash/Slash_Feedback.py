import discord, random

from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from Outhers.Random import IdS, banip

class _Feed(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name = 'Sugest', 
        description = 'Envia uma sugestão para meu criador',
        options = [
            create_option(
                name = 'sugestão',
                description = 'Escreva a sugestão',
                option_type = 3,
                required = True
            )
        ]
    )
    @commands.cooldown(1,5, commands.BucketType.user)
    async def _sugest(self, ctx:SlashContext, *, sugestão = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
            
            user = self.bot.get_user(int(IdS))

            embed = discord.Embed(name = 'Sugest', 
            description = f'**Enviado por:** \n {ctx.author} \n\n **Sugestão:** \n {sugestão} \n\n  **No server:** \n {ctx.guild.name} \n\n **ID:** {ctx.author.id}')

            await ctx.send('Sua sugestão foi enviada ao meu dono')
            await user.send(embed=embed)

    @cog_ext.cog_slash(
        name = 'Report',
        description = 'Reportar algum bug do Markuus',
        options = [
            create_option(
                name = 'report',
                description = 'Report',
                option_type = 3,
                required = True
            )
        ]
    )
    @commands.cooldown(1,5, commands.BucketType.user)
    async def _report(self, ctx:SlashContext, *, report = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
            
            user = self.bot.get_user(int(IdS))

            embed = discord.Embed(name = 'report', 
            description = f'**Enviado por:** \n {ctx.author} \n\n **Report:** \n {report} \n\n  **No server:** \n {ctx.guild.name} \n\n **ID:** {ctx.author.id}')

            await ctx.send('Seu report foi enviada ao meu dono')
            await user.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(_Feed(bot))