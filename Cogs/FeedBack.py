import discord
import config

from discord.ext import commands

class back(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def sugest(self, ctx, *, sugestão = None):
        if ctx.author.id == config.banip:
            return
        else:
            
            user = self.bot.get_user(int(config.IdS))

            embed = discord.Embed(name = 'Sugest', 
            description = f'**Enviado por:** \n {ctx.author} \n\n **Sugestão:** \n {sugestão} \n\n  **No server:** \n {ctx.guild.name} \n\n **ID:** {ctx.author.id}')

            await ctx.send('Sua sugestão foi enviada ao meu dono')
            await user.send(embed=embed)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def report(self, ctx, *, report = None):
        if ctx.author.id == config.banip:
            return
        else:
            
            user = self.bot.get_user(int(config.IdS))

            embed = discord.Embed(name = 'report', 
            description = f'**Enviado por:** \n {ctx.author} \n\n **Report:** \n {report} \n\n  **No server:** \n {ctx.guild.name} \n\n **ID:** {ctx.author.id}')

            await ctx.send('Seu report foi enviada ao meu dono')
            await user.send(embed=embed)


def setup(bot:commands.Bot):
    bot.add_cog(back(bot))