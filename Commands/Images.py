import random,discord

from PIL import ImageDraw, ImageFont, Image
from discord.ext import commands
from Outhers.Random import better_time, banip
from io import BytesIO

class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def procurado(self, ctx, membro: discord.Member = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
        
            if membro == None:
                membro = ctx.author

            procurado = Image.open('./images_fonts/procurado.png')

            asset = membro.avatar_url_as(size = 128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)

            pfp = pfp.resize((193,149))
            procurado.paste(pfp, (18,71))

            procurado.save('./images_fonts/Procurado.jpg')

            await ctx.reply(file = discord.File('./images_fonts/Procurado.jpg'))

    @commands.command()
    async def conquistamine(self ,ctx, conquista):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            elif conquista == None:
                await ctx.reply('Você precisa escrever a conquista')
                return

        
            conquista1 = Image.open('./images_fonts/conquista.jpeg')
            
            draw = ImageDraw.Draw(conquista1)
            font = ImageFont.truetype("./images_fonts/Minecrafter.Alt.ttf",size=15)

            draw.text((59,35), conquista ,font = font)

            conquista1.save('./images_fonts/conquista.png')

            await ctx.reply(file = discord.File('./images_fonts/conquista.png'))

    @commands.command()
    async def perfeição(self, ctx, membro: discord.Member = None):
        rand = random.randint(0,2)
        if ctx.author.id == banip:
            return
        elif rand == 1:
            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
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

            await ctx.reply(file = discord.File('./images_fonts/perfeicao.png'))

    @commands.command()
    async def safadão(self, ctx, membro: discord.Member = None, escolha = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            elif membro == None:
                await ctx.reply('Você precisa mencionar alguem')
                return

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

            await ctx.reply(file = discord.File('./images_fonts/safadao.png'))

    @perfeição.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @safadão.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @conquistamine.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @procurado.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')


def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))