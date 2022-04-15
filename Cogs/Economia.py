import random
import discord
import config

from discord.ext import commands
from pymongo import MongoClient
from Cogs.Slash_Economia import better_time

cluster = MongoClient("#")

db = cluster["Bank"]

collection = db["Bank"]
collection2 = db["Inv"]

shop = [
    {'Nome': 'Picareta ferro','compra': 500, 'Venda': 450},
    {'Nome': 'Picareta ouro','compra': 290900, 'Venda': 261810},
    {'Nome': 'Picareta diamante','compra': 293900, 'Venda': 264510},
    {'Nome': 'Arma', 'compra': 25000, 'Venda': 22500},
    {'Nome': 'Carro', 'compra': 10000, 'Venda':9000},
    {'Nome': 'Ferro', 'compra': 450, 'Venda':405},
    {'Nome': 'Ouro', 'compra': 290880, 'Venda':261792},
    {'Nome': 'Diamante', 'compra': 293504, 'Venda':264153},
    {'Nome': 'Anel casamento', 'compra': 60, 'Venda':54},
    {'Nome': 'Madeira', 'compra': 50, 'Venda': 45},
    {'Nome': 'Computador', 'compra': 3500, "Venda": 2000}
]
    
crafts = [
    {"Nome": 'Picareta ferro', '1': '1 Madeira', '2': '3 Ferros'},
    {"Nome": 'Picareta ouro', '1': '1 Madeira', '2': '3 Ouros'},
    {"Nome": 'Picareta diamante', '1': '1 Madeira', '2': '3 Diamante'},
]
class Economia(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def edinhos(self, ctx, membro: discord.Member = None):
        if ctx.author.id == config.banip:
            return
        else: 

            if membro == None:
                membro = ctx.author
            else:
                membro = membro

            await open_account(membro)

            bal = collection.find_one({"_id": membro.id})
            
            em = discord.Embed(title = f"{membro.name} Edinhos", color = discord.Color.red())
            em.add_field(name ='Edinhos', value = bal["Edinhos"])

            await ctx.reply(embed = em)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Transferir(self, ctx, membro: discord.Member, edinhos = None):
        if ctx.author.id == config.banip:
            return
        elif membro == None:
            await ctx.reply('Você precisa mencionar alguem')
        elif edinhos == None:
            await ctx.reply('Você precisa escolher a quantidade para transferir')
        else:
            await open_account(ctx.author)
            await open_account(membro)
            bal = collection.find_one({"_id": ctx.author.id})

            if edinhos == None:
                await ctx.reply(f'Você precisa selecionar uma quantidade de edinho para transferir')

            dindin = int(edinhos)

            b1 = bal["Edinhos"]

            if dindin > b1:
                await ctx.reply(f'Você não tem dinheiro suficiente')
            elif dindin == 0:
                await ctx.reply('A quantia tem que ser maior que zero')
                return
            elif dindin < 0:
                await ctx.reply(f'A quantia deve ser positiva')
                return

            await update_bank(ctx.author,- dindin)
            await update_bank(membro,+ dindin)
            await ctx.reply(f'Voce transferiu {dindin} edinhos')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def loteria(self, ctx, edinhos = None):
        if ctx.author.id == config.banip:
            return
        else: 
            await open_account(ctx.author)

            if edinhos == None:
                await ctx.reply(f'Você precisa selecionar uma quantidade de edinho para Jogar')

            bal = collection.find_one({"_id": ctx.author.id})

            dindin = int(edinhos)

            if dindin > bal["Edinhos"]:
                await ctx.reply(f'Você não tem dinheiro suficiente')
                return
            elif dindin == 0:
                await ctx.reply('A quantia deve ser maior que 0')
                return
            elif dindin < 0:
                await ctx.reply(f'A quantia deve ser positiva')
                return

            final = []
            for i in range(3):
                a = random.choice([':pineapple:',':grapes:',':kiwi:',])

                final.append(a)

            await ctx.reply(str(final))


            if final[0] == final[1] == final[2]:

                await update_bank(ctx.author,4*dindin)
                await ctx.reply(f'Você ganhou {4*dindin} edinhos!!')
            else:
                await update_bank(ctx.author,-1*dindin)
                await ctx.reply(f'Você perdeu {dindin} edinhos')

    @commands.command(aliases = ['ccap'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Caraoucoroaap(self, ctx, edinhos = int, escolha = None):
        if ctx.author.id == config.banip:
            return
        else: 
            bal = collection.find_one({"_id": ctx.author.id})

            dindin = int(edinhos)

            if dindin > bal["Edinhos"]:
                await ctx.reply(f'Você não tem dinheiro suficiente para apostar')
                return
            elif dindin < 0:
                await ctx.reply(f'A quantia deve ser positiva')
                return

            random1 = random.choice(['cara', 'coroa'])

            if random1 == escolha:
                await ctx.reply(f'Caiu {escolha}\nParabens, você ganhou {dindin*2} edinhos')
                await update_bank(ctx.author, + dindin*2)
            elif random1 != escolha:
                await ctx.reply(f'Caiu {random1}\nSad, você perdeu {dindin} edinhos')
                await update_bank(ctx.author, - dindin)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def edinhostop(self, ctx):

        rankings = collection.find().sort("Edinhos",-1)
        i=1
        embed = discord.Embed(title = f"***Top 5 mais ricos***")
        for x in rankings:
            user_xp = x["Edinhos"]

            embed.add_field(name=f"{i}: {x['Nome']}", value=f"{user_xp}", inline=False)
            if i == 5:
                break
            else:
                i += 1
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        await ctx.reply(embed=embed)

    @commands.command(aliases = ['inv'])
    @commands.cooldown(1,5, commands.BucketType.user)
    async def inventario(self, ctx):
        await open_inv(ctx.author)
        await reload_inv(ctx.author)
        inv = collection2.find_one({"_id": ctx.author.id})

        embed = discord.Embed(
        title = 'Inventario',
        description = 
        f'''
        Picareta ferro {inv['picareta ferro']}
        Picareta de ouro {inv['picareta ouro']}
        Picareta de diamante {inv['picareta diamante']}
        Carro {inv['carro']}
        Arma {inv['arma']}
        Diamante {inv['diamante']}
        Ouro {inv['ouro']}
        Anel de casamento {inv['anel casamento']}
        Ferro {inv['ferro']}
        Madeira {inv['madeira']}
        Computador {inv['computador']}
        ''')
        await ctx.reply(embed = embed)

    @commands.command(aliases = ['mercado'])
    @commands.cooldown(1,5, commands.BucketType.user)
    async def Shop(self, ctx, opção = None, quantidade = int, *,item = None):
        embed = discord.Embed(title = 'Mercado')

        await open_inv(ctx.author)

        if opção == None:
            for i in shop:
                name = i["Nome"]
                compra = i["compra"]
                venda = i["Venda"]
                embed.add_field(name = name, value = f'Compra {compra}\n Venda {venda}')

            await ctx.reply(embed = embed)
        elif opção == 'Buy':
            item_name = item.capitalize()

            await open_inv(ctx.author)

            for it in shop:
                name = it["Nome"]
                if name == item_name:
                    price = it["compra"]
                    break

            cost = price*quantidade

            bal = collection.find_one({"_id": ctx.author.id})

            if bal['Edinhos'] < cost:
                await ctx.reply('Você não tem edinhos suficientes')
            else:
            
                q = None
                if quantidade == 1:
                    q = 'unidade'
                elif quantidade > 1:
                    q = 'unidades'

                await ctx.reply(f'Você comprou {quantidade} {q} de {item} por {cost} edinhos')
                await update_bank(ctx.author, - cost)
                await update_inv(ctx.author, item_name, quantidade)
        elif opção == 'Sell':
            item_name = item.capitalize()
            item_name2 = item.lower()

            await open_inv(ctx.author)

            for it in shop:
                name = it["Nome"]
                if name == item_name:
                    price = it["Venda"]
                    break

            cost = price*quantidade

            bal = collection2.find_one({"_id": ctx.author.id})

            if bal[f'{item_name2}'] < 1:
                await ctx.reply('Você não tem esse item para vender')
            else:
            
                q = None
                if quantidade == 1:
                    q = 'unidade'
                elif quantidade > 1:
                    q = 'unidades'

                await ctx.reply(f'Você vendeu {quantidade} {q} de {item} por {cost} edinhos')
                await update_bank(ctx.author, + cost)
                await update_inv(ctx.author, item_name, - quantidade)
        
    @commands.command(aliases = ['craftar'])
    @commands.cooldown(1,5, commands.BucketType.user)
    async def craft(self, ctx, opção = None, *, craft = None):

        if opção == None:
            e = discord.Embed(title = 'Crafts')

            for i in crafts:
                name = i["Nome"]
                compra = i["1"]
                venda = i["2"]
                e.add_field(name = name, value = f' {compra}\n {venda}')

            await ctx.reply(embed = e)
        elif opção == 'craftar':
            item_ = craft.lower()
            b1 = collection2.find_one({"_id": ctx.author.id})

            if item_ == 'picareta diamante':
                if b1['madeira'] < 1:
                    await ctx.reply('Você não tem madeira suficiente')
                    return
                elif b1['diamante'] < 3:
                    await ctx.reply('Você não tem diamante suficiente')
                    return
                else:
                    await update_inv(ctx.author, 'madeira', - 1)
                    await update_inv(ctx.author, 'diamante', -3)
                    await update_inv(ctx.author, 'picareta diamante', 1)
                    await ctx.reply('Picareta diamante craftada com sucesso')
            
            elif item_ == 'picareta ferro':
                if b1['madeira'] < 1:
                    await ctx.reply('Você não tem madeira suficiente')
                    return
                elif b1['ferro'] < 3:
                    await ctx.reply('Você não tem ferro suficiente')
                    return
                else:
                    await update_inv(ctx.author, 'madeira', - 1)
                    await update_inv(ctx.author, 'ferro', -3)
                    await update_inv(ctx.author, 'picareta ferro', 1)
                    await ctx.reply('Picareta ferro craftada com sucesso')
        
            elif item_ == 'picareta ouro':
                if b1['madeira'] < 1:
                    await ctx.reply('Você não tem madeira suficiente')
                    return
                elif b1['ouro'] < 3:
                    await ctx.reply('Você não tem ouro suficiente')
                    return
                else:
                    await update_inv(ctx.author, 'madeira', - 1)
                    await update_inv(ctx.author, 'ouro', -3)
                    await update_inv(ctx.author, 'picareta ouro', 1)
                    await ctx.reply('Picareta ouro craftada com sucesso')

    @edinhos.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

        if isinstance(error, commands.MemberNotFound):

            await ctx.reply('Não encontrei esse membro no server')

    @edinhostop.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @loteria.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @Transferir.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

        if isinstance(error, commands.MemberNotFound):

            await ctx.reply('Não encontrei esse membro no server')

    @Caraoucoroaap.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @inventario.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @Shop.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @craft.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

async def open_account(id):

    if id is not None:

        user = {"_id": id.id, "Nome": id.name, "Edinhos": 0}
        myquery = { "_id": id.id}   
        if (collection.count_documents(myquery) == 0):

            collection.insert_one(user)

async def update_bank(id, Edinhos : int):
    if id is not None:
        collection.update_one({"_id": id.id}, {"$inc": {"Edinhos": Edinhos}})

async def open_inv(id):
    if id is not None:
        user = {'_id': id.id, 
        'Nome': id.name, 
        'picareta ferro' : 0, 
        'picareta ouro' : 0,
        'picareta diamante' : 0,
        'carro' : 0,
        'arma' : 0,
        'diamante' : 0,
        'ouro' : 0,
        'anel casamento' : 0,
        'ferro' : 0,
        'madeira': 0,
        'computador': 0,
        }
        myquery = { "_id": id.id}   
        if (collection2.count_documents(myquery) == 0):

            collection2.insert_one(user)

async def update_inv(id, item, quantidade : int):

    if id is not None:
        collection2.update_one({"_id": id.id}, {"$inc": {f"{item.lower()}": quantidade}})

async def reload_inv(id):

    if id is not None:
        collection2.update_one({"_id": id.id}, {"$inc": {f"computador": 0}})
        collection2.update_one({"_id": id.id}, {"$inc": {f"madeira": 0}})

def setup(bot:commands.Bot):
    bot.add_cog(Economia(bot))