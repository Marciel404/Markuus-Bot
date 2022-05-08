import asyncio, random, time, discord, requests, platform

from discord.ext import commands
from Outhers.Random import better_time, banip, punch, sad
from Outhers.Economi import collection, open_account

class Gerais(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            

            help = discord.Embed(title = 'Meus comands',
            description = 
            '''
0️⃣ | Menu.....1️⃣ | Moderação
2️⃣ | Gerais....3️⃣ | Economia
4️⃣ | Suporte.5️⃣ | Imagens
6️⃣ | Musica
            '''
            )
            help.set_thumbnail(url = self.bot.user.avatar_url)
            Moderação = discord.Embed(title = 'Meus comandos',
            description = '**Nome/Permissão/Função**',
            color = ctx.author.color)
            Moderação.add_field(
            name = 'Moderação',
            value = 
            '''
Ban - (Ban members) - Bane membros no seu servidor
BanId - (Ban Members) - Bane uma pessoa que não está no seu server pelo id
Unban - (Ban Members) - Desbane um membro no seu servr
Kick - (Kick Members) - Expulsa uma pessoa do seu server
Clear - (Manage channels) - Limpa o chat do seu server
Say - (Administrator) - Fala algo no server
SetLogs - (Manage_chnnels) - Seta o canal de logs do bot
AutoRole - (Manage_chnnels) - Seta um cargo para Autorole
Setprefix - (Administrator) - Seta o prefixo do bot
TempRole - (manage_roles) -Da um cargo por tempo limitado para um membro
            ''',
            inline = False)
            Moderação.set_thumbnail(url = self.bot.user.avatar_url)

            Gerais = discord.Embed(title = 'Meus comandos',
            color = ctx.author.color)
            Gerais.add_field(
            name='Gerais',
            value = 
            '''
Hello - Comando teste do markuus
Aleatorio - Escolhe um numero aleatorio para você
Ping - Mostra o meu ping e da api do discord
Servers - Diz em quantos servers eu estou
Userinfo - puxa as informações de algum membro ou as suas
ServerInfo - puxa as informações do server
Invite - Manda o link para convidar o bot
Hug - Abraça um membro
Slap - Bate em algum membro
Kiss - Beija um membro
Shoot - Atira em algum membro
Punch - Soca algum membro
Donate - Envia as formas de ajudar o bot
Lembrete -  Define um lembrete
            ''',
            inline = False)
            Gerais.set_thumbnail(url = self.bot.user.avatar_url)

            Economia = discord.Embed(title = 'Meus comandos',
            color = ctx.author.color)
            Economia.add_field(
            name= 'Comandos Economia', 
            value=
            '''
Rolar - Voce pode ganhar de 0 a 2000 edinhos
Edinhos - Mostra quantos edinhos você tem ou do membro mencionado
Edinhostop - Mostra o rank de pessoas mais ricas
Loteria - Você pode apostar na sorte e quadruplicar seus edinhos
Transferir - Você pode transferir edinhos para outras pessoas
ccap - Jogue cara ou coroa valendo seus edinhos
Shop - Compra itens e venda
Inventario - Mostra os itens do seu iventario
Minerar - Minera, tem chance de vir recursos
Craft - Crafta alguns itens
            ''',
            inline = False)
            Economia.set_thumbnail(url = self.bot.user.avatar_url)

            Suporte = discord.Embed(title = 'Meus comandos',
            color = ctx.author.color)
            Suporte.add_field(
            name = 'Suporte',
            value = 
            '''
Sugest - Envia uma sugestão para meu dono
Report - Envia um report para meu dono
            ''',
            inline = False)
            Suporte.set_thumbnail(url = self.bot.user.avatar_url)

            Images = discord.Embed(title = 'Meus comandos',
            color = ctx.author.color)
            Images.add_field(
            name = 'Imagens',
            value = 
            '''
ConquistaMine - Criar uma conquista do minecraft
Perfeição - Cria um meme de "perfeição"
Safadão -  envia uma imagem do Meliodas "safadão"
            ''',
            inline = False)
            Images.set_thumbnail(url = self.bot.user.avatar_url)

            Musica = discord.Embed(title = 'Meus comandos',
            color = ctx.author.color)
            Musica.add_field(
            name = 'Musica',
            value = 
            '''
Play - Toca uma musica
Pause - Pausa a musica tocando
Skip - Pula para a proxima musica da Fila
Stop - Para e tira o Markuus da call
Remove - Remove uma musica da lista de musicas
Leave - Remove o Markuus da call
            ''',
            inline = False)
            Musica.set_thumbnail(url = self.bot.user.avatar_url)

            message = await ctx.reply(embed = help)

            await message.add_reaction('0️⃣')
            await message.add_reaction('1️⃣')
            await message.add_reaction('2️⃣')
            await message.add_reaction('3️⃣')
            await message.add_reaction('4️⃣')
            await message.add_reaction('5️⃣')
            await message.add_reaction('6️⃣')

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']
            while True:
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", check=check, timeout = 60)

                    if str(reaction.emoji) == '0️⃣':
                        await message.edit(embed = help)
                    elif str(reaction.emoji) == '1️⃣':
                        await message.edit(embed = Moderação)
                    elif str(reaction.emoji) == '2️⃣':
                        await message.edit(embed = Gerais)
                    elif str(reaction.emoji) == '3️⃣':
                        await message.edit(embed = Economia)
                    elif str(reaction.emoji) == '4️⃣':
                        await message.edit(embed = Suporte)
                    elif str(reaction.emoji) == '5️⃣':
                        await message.edit(embed = Images)
                    elif str(reaction.emoji) == '6️⃣':
                        await message.edit(embed = Musica)

                except asyncio.TimeoutError:
                    return

    @commands.command()
    async def hello(self, ctx):
        if ctx.channel.id != 8976549468796:
            return
        else:
            rand = random.randint(0,2)
            if ctx.author.id == banip:
                return
            elif rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            else:
                
                await ctx.reply('Hello, World {}'.format(ctx.author.name))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def aleatorio(self, ctx,numero = 0):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            elif numero == 0:
                await ctx.reply('Você precisa escolher um numero')
                return
            
            dado = random.randint(0,int(numero))

            if numero == 0:
                await ctx.reply('Voce precisa escolher um numero para esse comando funcionar')
            else:
                await ctx.reply('Seu numero foi {}'.format(dado))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
            
            p1 = discord.Embed(name = 'ping', 
            description = '**🏓Calculando ping.**',
            color = 0x2ecc71)

            start_time = time.time()
            msg = await ctx.reply(embed = p1)
            end_time = time.time()
            Ping = round(self.bot.latency * 1000)
            
            p2 = discord.Embed(name = 'ping', 
            description = '**🏓Calculando ping..**', color = 0x2ecc71)
            p3 = discord.Embed(name = 'ping', 
            description = '**🏓Calculando ping...**', color = 0x2ecc71)
            p4 = discord.Embed(name = 'ping', 
            description = f'''
Meu ping: {Ping}ms
API: {round((end_time - start_time) * 1000)}ms''', 
            color = 0x2ecc71)

            count = 0

            while  count < 2:
                count += 1
                await msg.edit(embed = p2)
                await asyncio.sleep(0.5)
                await msg.edit(embed = p3)
                await asyncio.sleep(0.5)
                await msg.edit(embed = p1)
                await asyncio.sleep(0.5)

            await msg.edit(embed = p4)

    @commands.command()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def servers(self, ctx):
        if ctx.channel.id == 944367131942854708:
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
            await ctx.reply('Eu estou em ' + str(len(self.bot.guilds)) + ' servers!')
        else:
            await ctx.reply('teste')

    @commands.command(aliases = ['si', 'serveri'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverInfo(self, ctx, server : discord.Guild = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return

            if server == None:
                server = ctx.guild
            
            ct = len(server.text_channels)
            cv = len(server.voice_channels)
            tc = ct + cv

            embed = discord.Embed(title = f'**{server.name}**',
            color = server.owner.top_role.color)

            embed.add_field(name = ':scroll: Nome:', 
            value = server.name,
            inline = True)
            
            embed.add_field(name = ':computer:  Id do server:', 
            value = server.id,
            inline = True)

            embed.add_field(name = ':busts_in_silhouette: Membros:', 
            value = len(server.members),
            inline = True)

            embed.add_field(name = f':speech_balloon: Canais:({tc})', 
            value = f':keyboard: texto: {ct}\n :loud_sound: Voz:{cv}',
            inline = True)

            embed.add_field(name = ':shield: Verificação:',
            value = '{}'.format(str(server.verification_level).upper()),
            inline = True)

            embed.add_field(name = ':crown: Dono:', 
            value = '{}\n ({})'.format(server.owner.mention,server.owner.id),
            inline = True)

            embed.add_field(name = ':calendar_spiral:Criado em:', 
            value = server.created_at.strftime('%d %m %Y'),
            inline = True)

            embed.set_thumbnail(url=server.icon_url)
            await ctx.reply(embed = embed)

    @commands.command(aliases = ['ui', 'useri'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx, membro: discord.Member = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
            e1 = self.bot.get_emoji(971487187361218620)
            
            if membro == None:
                membro = ctx.author

            await open_account(membro)

            user = collection.find_one({"_id": membro.id})

            edinhos = user["Edinhos"]

            embed = discord.Embed(colour=membro.color)

            embed.set_author(name=f"User Info - {membro}"),
            embed.set_thumbnail(url=membro.avatar_url),

            embed.add_field(name = f'{e1} Nome/ID:',
            value = f'{membro.display_name}/{membro.id}',inline=False)

            embed.add_field(name = 'Conta  criada em:',
            value = membro.created_at.strftime(f" %d %m %Y"),inline=True)

            embed.add_field(name = 'Entrou no server em:',
            value = membro.joined_at.strftime(f" %d %m %Y") ,inline=True)

            embed.add_field(name = 'Maior cargo:',
            value = membro.top_role.mention,inline=False)

            embed.add_field(name = 'Edinhos', 
            value = edinhos, inline = True)
    
            await ctx.reply(embed=embed)

    @commands.command()
    async def avatar(self, ctx, membro: discord.Member = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
            if membro == None:
                membro = ctx.author
            else:
                membro = membro

            embed = discord.Embed(title = f'Avatar de {membro}', 
            description = f'clique [aqui]({membro.avatar_url}) para baixar a imagem')
            embed.set_image(url = f'{membro.avatar_url}')
            await ctx.reply(embed = embed)

    @commands.command()
    async def invite(self, ctx):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
            
            e = discord.Embed(title = 'Invite', 
            description = 'Convide-me clicando [aqui](https://discord.com/api/oauth2/authorize?client_id=930619804593819699&permissions=8&scope=bot%20applications.commands)')
            e.set_thumbnail(url = self.bot.user.avatar_url)
            await ctx.reply(embed=e)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def hug(self, ctx, membro: discord.Member = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            elif membro == None:
                await ctx.reply('Você precisa mencionar alguem')
                return

            r = requests.get(
            'http://nekos.life/api/v2/img/hug')
            res = r.json()
            
            hug = discord.Embed(title = 'Abraço',
            description = '<@{}> abraçou <@{}>'.format(ctx.author.id,membro.id))
            hug.set_image(url = res['url'])
            hug.set_footer(text = 'Clique no 🔁 para retribuir')
            hug2 = discord.Embed(title = 'Abraço',
            description = '<@{}> abraçou <@{}>'.format(membro.id,ctx.author.id))
            hug2.set_image(url = res['url'])

            message = await ctx.reply(membro.mention,embed = hug)
            await message.add_reaction("🔁")

            def check(reaction, user):
                if user == self.bot.user:
                    return
                else:
                    return user == membro and str(reaction.emoji) in "🔁"

            reaction, user = await self.bot.wait_for("reaction_add", check=check)

            if str(reaction.emoji) == "🔁":
                await ctx.reply(embed = hug2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def kiss(self, ctx, membro: discord.Member = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            elif membro == None:
                await ctx.reply('Você precisa mencionar alguem')
                return

            r = requests.get(
            'http://nekos.life/api/v2/img/kiss')
            res = r.json()
            
            if membro == self.bot.user:
                await ctx.reply('Acho melhor só sermos amigos')
            else:

                kiss = discord.Embed(title = 'Beijo',
                description = '<@{}> beijou <@{}>'.format(ctx.author.id, membro.id))
                kiss.set_image(url = res['url'])
                kiss.set_footer(text = 'Clique no 🔁 para retribuir')
                
                kiss2 = discord.Embed(title = 'Beijo',
                description = '<@{}> beijou <@{}>'.format(membro.id, ctx.author.id))
                kiss2.set_image(url = res['url'])

                message = await ctx.reply(membro.mention,embed = kiss)
                await message.add_reaction("🔁")

                def check(reaction, user):
                    if user == self.bot.user:
                        return
                    else:
                        return user == membro and str(reaction.emoji) in "🔁"

                reaction, user = await self.bot.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "🔁":
                    await ctx.reply(embed = kiss2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def slap(self, ctx, membro: discord.Member = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            elif membro == None:
                await ctx.reply('Você precisa mencionar alguem')
                return

            r = requests.get(
            'http://nekos.life/api/v2/img/slap')
            res = r.json()
            
            if membro.bot:
                await ctx.reply('Você não faria isso com um pobre bot indefeso?')
            else:

                slap = discord.Embed(title = 'Tapa', description = '<@{}> estapeou <@{}>'.format(ctx.author.id, membro.id))
                slap.set_image(url = res['url'])
                slap.set_footer(text = 'Clique no 🔁 para retribuir')
                slap2 = discord.Embed(title = 'Tapa', description = '<@{1}> estapeou <@{0}>'.format(ctx.author.id, membro.id))
                slap2.set_image(url = res['url'])
        
                message = await ctx.reply(membro.mention,embed = slap)
                await message.add_reaction('🔁')

                def check(reaction, user):
                    if user == self.bot.user:
                        return
                    else:
                        return user == membro and str(reaction.emoji) in "🔁"

                reaction, user = await self.bot.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "🔁":
                    await ctx.reply(embed = slap2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def shoot(self, ctx, membro: discord.Member = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return   
            elif membro == None:
                await ctx.reply('Você precisa mencionar alguem')
                return

            r = requests.get(
            'http://nekos.life/api/v2/img/shoot')
            res = r.json()
            
            if membro.bot:
                await ctx.reply('Você não faria isso com um pobre bot indefeso?')
            else:

                shoot = discord.Embed(title = 'Tiro', description = f'<@{ctx.author.id}> atirou em <@{membro.id}>')
                shoot.set_image(url = res['url'])
                shoot.set_footer(text = 'Clique no 🔁 para retribuir')
                shoot2 = discord.Embed(title = 'Tiro', description = f'<@{membro.id}> atirou em <@{ctx.author.id}>')
                shoot2.set_image(url = res['url'])
        
                message = await ctx.reply(membro.mention,embed = shoot)
                await message.add_reaction("🔁")

                def check(reaction, user):
                    if user == self.bot.user:
                        return
                    else:
                        return user == membro and str(reaction.emoji) in "🔁"

                reaction, user = await self.bot.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "🔁":
                    await ctx.reply(embed = shoot2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def punch(self, ctx, membro: discord.Member = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            elif membro == None:
                await ctx.reply('Você precisa mencionar alguem')
                return
            
            if membro.bot:
                await ctx.reply('Você não faria isso com um pobre bot indefeso?')
            elif membro == None:
                await ctx.reply('Voce precisa mencionar alguem')

                choice = random.choice(punch)
                choice2 = random.choice(punch)
                punch1 = discord.Embed(title = 'Soco', description = f'<@{ctx.author.id}> Socou <@{membro.id}>')
                punch1.set_image(url = choice)
                punch1.set_footer(text = 'Clique no 🔁 para retribuir')
                punch2 = discord.Embed(title = 'Soco', description = f'<@{membro.id}> Socou <@{ctx.author.id}>')
                punch2.set_image(url = choice2)
        
                message = await ctx.reply(membro.mention,embed = punch)
                await message.add_reaction("🔁")

                def check(reaction, user):
                    if user == self.bot.user:
                        return
                    else:
                        return user == membro and str(reaction.emoji) in "🔁"

                reaction, user = await self.bot.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "🔁":
                    await ctx.reply(embed = punch2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def sad(self,ctx):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
            choice = random.choice(sad)
            embed = discord.Embed(title = 'Sad', description = f'{ctx.author.mention} está triste')
            embed.set_image(url = choice)

            await ctx.reply(embed = embed)

    @commands.command()
    async def Vote(self, ctx):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return

            e1 = self.bot.get_emoji(971189865532244028)

            server = '[Server Suport](https://discord.com/invite/xSs6xEjuvf)'
            top = '[Top.gg](https://top.gg/bot/930619804593819699)'
            inv = '[Invite](https://discord.com/api/oauth2/authorize?client_id=930619804593819699&permissions=8&scope=bot%20applications.commands)'

            topgg = discord.Embed(title = 'Vote', 
            description = f'''
Muito obrigado por escolher votar em mim {ctx.author.mention}
isso me ajuda bastante e voce sabia que eu tbm tenho 
um server de suporte, está tudo aqui a baixo
''')
            topgg.add_field(name = f':grey_question: Está com alguma dúvidas? Entre no meu Servidor de Suporte!', value = server, inline = False)
            topgg.add_field(name = f'{e1} Quer me ajudar a crescer? Aqui está o link do Top.gg', 
                value = top, inline = False)
            topgg.add_field(name = f':partying_face: Querendo me convidar? Aqui está o link', 
                value = inv, inline = False)
            topgg.set_thumbnail(url = self.bot.user.avatar_url)
            await ctx.reply(embed = topgg)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def donate(self, ctx):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return
            
            embed = discord.Embed(title = 'Donate')
            embed.add_field(
            name = 'Metodos',
            value = 
            '''
Pix: rafaelucas@protonmail.com(Brasil)
Paypal: rafaelucas@protonmail.com
            ''')
            await ctx.reply(embed = embed)

    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def Lembrete(self, ctx, tempo  = None, *, lembrete = None):
            rand = random.randint(0,2)
            if rand == 1:
                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            elif ctx.author.id == banip:
                return

            if lembrete == None:
                ctx.reply('Você precisa escrever a descrição do lembrete')
            elif tempo == None:
                ctx.reply('Você precisa escolher o tempo do lembrete')

            embed = discord.Embed(color=self.bot.user.color)
            seconds = 0
            if lembrete is None:
                embed.add_field(name='Erro', value='Você precisa definir o lembrete') # Error message
            if tempo.lower().endswith("d"):
                seconds += int(tempo[:-1]) * 60 * 60 * 24
                counter = f"{seconds // 60 // 60 // 24} dias"
            if tempo.lower().endswith("h"):
                seconds += int(tempo[:-1]) * 60 * 60
                counter = f"{seconds // 60 // 60} horas"
            elif tempo.lower().endswith("m"):
                seconds += int(tempo[:-1]) * 60
                counter = f"{seconds // 60} minutos"
            elif tempo.lower().endswith("s"):
                seconds += int(tempo[:-1])
                counter = f"{seconds} segundos"
            if seconds == 0:
                embed.add_field(name='Erro',
                                value='A duração precisa ser maior que 0 Segundos')
            elif seconds > 7776000:
                embed.add_field(
                name='Erro', 
                value=
                '''
A duração desse lembrete é muito longo
Limite de dias é de 90 dias
                '''
                )
            else:
                await ctx.reply('Okay, Eu irei te lembrar de {} daqui a {}'.format(lembrete, counter))
                await asyncio.sleep(seconds)
                await ctx.reply('Ola {1}, estou passando aqui para te lembrar de "{0}" como você me pediu'.format(lembrete, ctx.author.mention))
                return
            await ctx.reply(embed=embed)

    @commands.command()
    async def botinfo(self, ctx):

        e1 = self.bot.get_emoji(971189876986884186)
        e2 = self.bot.get_emoji(971212878763917362)
        e3 = self.bot.get_emoji(971571054046773250)
        e4 = self.bot.get_emoji(971571518532354118)
        e5 = self.bot.get_emoji(971487187361218620)

        e = discord.Embed(title = 'Minhas informações')
        e.set_thumbnail(url = self.bot.user.avatar_url)
        e.add_field(name = f'{e5} Nome', value = self.bot.user.name, inline = True)
        e.add_field(name = f'{e4} Linguagem', value = f'{e1} Python', inline = True)
        e.add_field(name = f'{e2} Discord.py Version', value = discord.__version__, inline = False)
        e.add_field(name = f'{e1} Python Version', value = platform.python_version())
        e.add_field(name = f'{e3} Comandos', value = len(self.bot.commands))


        await ctx.reply(embed = e)
        
    @commands.command()
    async def EmojiInfo(self, ctx, emoji : discord.Emoji = None):

        if emoji == None:
            await ctx.reply('Você precisa colocar o emoji')
            return

        e1 = self.bot.get_emoji(971487187361218620)

        embed = discord.Embed(title = f'{emoji} Emoji Info')
        embed.set_thumbnail(url = emoji.url)
        embed.add_field(name = ':notepad_spiral: Nome do Emoji', value = emoji.name, inline = True)
        embed.add_field(name = f'{e1} Id do Emoji', value = emoji.id, inline = True)
        embed.add_field(name = ':goggles: Menção', value = f'`<:{emoji.name}:{emoji.id}>`', inline = True)
        embed.add_field(name = ':chains: Url', value = emoji.url, inline = True)
        embed.add_field(name = ':date: Adicionado em', value = emoji.created_at.strftime('%d %m %Y'), inline = True)
        embed.add_field(name = ':mag_right: Servidor de origem', value = emoji.guild, inline = True)

        await ctx.reply(embed = embed)

    @commands.command()
    async def emoji(self, ctx, emoji : discord.Emoji = None):
        await ctx.reply(emoji)

    @hello.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @aleatorio.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')
    @ping.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @servers.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')
    
    @userinfo.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @serverInfo.error
    async def o(self, ctx: commands.Context, error):

        if isinstance(error, commands.GuildNotFound):

            await ctx.reply(f':x: Não estou em nenhum server com o id `{error.argument}` então não tenho informações')
            return

        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @invite.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @hug.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @slap.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @kiss.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @shoot.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @punch.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @Vote.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @sad.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @donate.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @Lembrete.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @emoji.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.EmojiNotFound):
            await ctx.reply(':x: Possivelmente esse emoji não é valido')
            return
            
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @EmojiInfo.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.EmojiNotFound):
            await ctx.reply(':x: Possivelmente esse emoji não é valido')
            return
            
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f':x: Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

def setup(bot:commands.Bot):
    bot.add_cog(Gerais(bot))
