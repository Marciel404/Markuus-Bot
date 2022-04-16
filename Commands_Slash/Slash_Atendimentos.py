import discord

from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from Outhers.Random import better_time, banip

class _Aten(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name='Ticket', 
        description='Abre um tichket no server'
    )
    async def _ticket(self, ctx:SlashContext):
        if ctx.author.id == banip:
            return

        guild = ctx.guild

        Chat = discord.utils.get(guild.channels, name=f'ticket-{ctx.author.id}')

        if Chat is None:

            guild = ctx.guild
            embed = discord.Embed(
                    title = 'Ticket criado com sucesso',
                    description = 'Agora só esperar a resposta',
                    color = 0
                )

            embed.set_footer(text=f'Ticket de {ctx.author.name}')

            msg = await ctx.send(embed=embed)
            await msg.add_reaction("📩")

            ticket = f'ticket-{ctx.author.id}'
            member = ctx.author
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True),
                }

            channel = await guild.create_text_channel(name=ticket, overwrites = overwrites)
            await channel.send(ctx.author.mention)

        else:
            await ctx.reply('Ticket já existente, encerre o ultimo para criar outro')

    @cog_ext.cog_slash(
        name='Ft', 
        description='Fecha o ticket aberto'
    )
    async def _ft(self, ctx:SlashContext):
        if ctx.author.id == banip:
            return

        if f'ticket-{ctx.author.id}' in ctx.channel.name:
            await ctx.channel.delete()
        elif f'ticket-' in ctx.channel.name and ctx.author.guild_permissions.manage_channels:
            await ctx.channel.delete()
        else:
            await ctx.reply('Esse não é um chat  de ticket')
        

    @cog_ext.cog_slash(
        name='ADC', 
        description = 'Adiciona um membro ao ticket',
        options = [
            create_option(
                name = 'id',
                description = 'adiciona um membro ao chat ticket',
                option_type = 6,
                required = True
            )
        ]
    )
    async def _adc(self, ctx:SlashContext, id: discord.Member):
        if ctx.author.id == banip:
            return

        if f'ticket-{ctx.author.id}' in ctx.channel.name or ctx.author.guild_permissions.manage_channels:
            await ctx.channel.set_permissions(id, read_messages=True)
            await ctx.reply(f'{id.mention} adicionado')
        elif ctx.channel.name != f'ticket-{ctx.author.id}':
            await ctx.send('Este ticket não te pertence ou você não pode gerenciar canais')

    @cog_ext.cog_slash(
        name='RMV', 
        description = 'Remove um membro do chat ticket',
        options = [
            create_option(
                name = 'membro',
                description = 'Selecione um membro para ver a quantia',
                option_type = 6,
                required = True
            )
        ]
    )
    async def _rmv(self, ctx:SlashContext, membro: discord.Member):
        if ctx.author.id == banip:
            return

        if f'ticket-{ctx.author.id}' in ctx.channel.name or ctx.author.guild_permissions.manage_channels:
            await ctx.channel.set_permissions(membro, read_messages=False)
            await ctx.reply(f'{membro.mention}')
        elif ctx.channel.name != f'ticket-{ctx.author.id}':
            await ctx.send('Este ticket não te pertence ou você não pode gerenciar canais')

    @_ticket.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')
    
    @_ft.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @_adc.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @_rmv.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

def setup(bot:commands.Bot):
    bot.add_cog(_Aten(bot))