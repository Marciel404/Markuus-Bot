import random
import discord

from PIL import ImageDraw, ImageFont, Image
from io import BytesIO
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from Outhers.Random import better_time, banip

class _Img(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name = 'Procurado',
        description = 'Faz um cartaz de procurado',
        options = [
            create_option(
                name = 'membro',
                description = 'Escolha um membro',
                option_type = 6,
                required = False
            )
        ]
    )
    async def _procurado(self, ctx:SlashContext, membro: discord.Member = None):
        if ctx.author.id == banip:
            return
        else:
        
            if membro == None:
                membro = ctx.author

            procurado = Image.open('./images_fonts/procurado.png')

            asset = membro.avatar_url_as(size = 128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)

            pfp = pfp.resize((193,149))
            procurado.paste(pfp, (18,71))

            procurado.save('./images_fonts/Procurado.jpg')

            await ctx.send(file = discord.File('./images_fonts/Procurado.jpg'))

    @cog_ext.cog_slash(
        name = 'ConquistaMine',
        description = 'cria uma conquista do minecraft',
        options = [
            create_option(
                name = 'conquista',
                description = 'Escreva a conquista',
                option_type = 3,
                required = True,
            )
        ]
    )
    async def _conquistamine(self ,ctx:SlashContext, conquista):
        if ctx.author.id == banip:
            return
        else:
        
            conquista1 = Image.open('./images_fonts/conquista.jpeg')
            
            draw = ImageDraw.Draw(conquista1)
            font = ImageFont.truetype("./images_fonts/Minecrafter.Alt.ttf",size=15)

            draw.text((59,35), conquista ,font = font)

            conquista1.save('./images_fonts/conquista.png')

            await ctx.send(file = discord.File('./images_fonts/conquista.png'))

    @cog_ext.cog_slash(
        name = 'Perfeição',
        description = 'Cria um meme de perfeição não existe',
        options = [
            create_option(
                name = 'membro',
                description = 'Escolha um membro',
                option_type = 6,
                required = False
            )
        ]
    )
    async def _perfeição(self, ctx:SlashContext, membro: discord.Member = None):
        if ctx.author.id == banip:
            return
        else:
        
            if membro == None:
                membro = ctx.author

            perfeição = Image.open('./images_fonts/perfeicao.jpeg')

            draw = ImageDraw.Draw(perfeição)
            font = ImageFont.truetype("./images_fonts/LeagueGothic-Regular-VariableFont_wdth.ttf",size=20)

            draw.text((9,6), 'Pessoa: "Perfeição não existe"\nEu:', fill= (0,0,0) ,font = font)
            
            asset = membro.avatar_url_as(size = 128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)

            pfp = pfp.resize((150,150))
            perfeição.paste(pfp, (144,52))
            
            perfeição.save('./images_fonts/perfeicao.png')

            await ctx.send(file = discord.File('./images_fonts/perfeicao.png'))

    @cog_ext.cog_slash(
        name = 'Safadão',
        description = 'Cria um meme do meliodas safadão',
        options = [
            create_option(
                name = 'membro',
                description = 'Escolha um membro',
                option_type = 6,
                required = True
            ),
            create_option(
                name = 'escolha',
                description = 'Escolha a imagem',
                required = False,
                option_type = 3,
                choices = ['1','2','3','4']
            ),
        ]
    )
    async def _safadão(self, ctx:SlashContext, membro: discord.Member = None, escolha = None):

        names = ['1','2','3','4']

        if escolha == None:
            escolha = random.choice(names)

        safadão = Image.open(f'./images_fonts/{escolha}.jpeg')

        asset = ctx.author.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        asset2 = membro.avatar_url_as(size = 128)
        data2 = BytesIO(await asset2.read())
        pfp2 = Image.open(data2)
        
        if escolha == '1':
            
            pfp = pfp.resize((50,50))
            safadão.paste(pfp, (142,53))

            pfp2 = pfp2.resize((50,50))
            safadão.paste(pfp2, (102,35))

            safadão.save('./images_fonts/safadao.png')

        elif escolha == '2':

            pfp = pfp.resize((100,100))
            safadão.paste(pfp, (139,20))

            pfp2 = pfp2.resize((20,20))
            safadão.paste(pfp2, (95,50))

            safadão.save('./images_fonts/safadao.png')

        elif escolha == '3':

            pfp = pfp.resize((81,81))
            safadão.paste(pfp, (339,51))
            
            pfp2 = pfp2.resize((79,79))
            safadão.paste(pfp2, (238,47))

            safadão.save('./images_fonts/safadao.png')

        elif escolha == '4':

            pfp = pfp.resize((100,100))
            safadão.paste(pfp, (135,70))
            
            pfp2 = pfp2.resize((100,100))
            safadão.paste(pfp2, (308,10))

            safadão.save('./images_fonts/safadao.png')

        await ctx.send(file = discord.File('./images_fonts/safadao.png'))

    @_perfeição.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @_safadão.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @_conquistamine.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @_procurado.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')


def setup(bot):
    bot.add_cog(_Img(bot))