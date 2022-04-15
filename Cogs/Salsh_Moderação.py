import asyncio
import discord
import config

from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from pymongo import MongoClient

cluster = MongoClient("#")

db = cluster["Bank"]

collection = db["Logs"]
collection2 = db["AutoRole"]
collection3 = db["Prefix"]

class _Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name='SetLogs', 
        description='Seta o chat de logs do bot no server',
        options=[
            create_option(
                name = 'id',
                description = 'Mencione o canal',
                option_type = 7,
                required = False
            )
        ]
    )
    @commands.has_permissions(manage_channels = True)
    async def _setlogs(self, ctx, id = None):
        if ctx.author.id == config.banip:
            return
        else:

            server1 = {"_id": ctx.guild.id}

            if id == None:
                await ctx.send('Chat de logs removido')
                collection.remove(server1)
                
            
            id2 = int(id.id)

            server = {"_id": ctx.guild.id, "Nome": ctx.guild.name, "canal": id2}
            myquery = { "_id": ctx.guild.id}   
            if (collection.count_documents(myquery) == 0):
                collection.insert_one(server)
                await ctx.send('Canal de logs setado para {}, se desejar remover as logs use o comando sem mencionar um chat'.format(id.mention))
            else:
                collection.update({"_id" : ctx.guild.id}, {"$set":{"canal": id2}})
                await ctx.send('Canal de logs setado para {}, se desejar remover as logs use o comando sem mencionar um chat'.format(id.mention))

    @cog_ext.cog_slash(
        name = 'setprefix',
        description = 'seta o prefix do bot',
        options = [
            create_option(
                name = 'prefix',
                description = 'Escolha o prefix',
                option_type = 3,
                required = True
            )
        ]
    )
    @commands.has_permissions(manage_channels = True)
    async def _setprefix(self, ctx, prefix = None):
        if ctx.author.id == config.banip:
            return
        else:
            collection3.update_one({"_id": ctx.guild.id}, {"$set": {"prefix": prefix}})
            await ctx.reply('Prefixo mudado para {}'.format(prefix))

    @cog_ext.cog_slash(
        name='AutoRole', 
        description='Seta o cargo de auto role',
        options=[
            create_option(
                name = 'cargo',
                description = 'Mencione o cargo',
                option_type = 8,
                required = False
            )
        ]
    )
    @commands.has_permissions(manage_channels = True)
    async def _autorole(self, ctx, cargo: discord.Role = None):
        if ctx.author.id == config.banip:
            return
        else:
            
            cargo2 = cargo.name

            if cargo == None:
                collection.delete_one({"_id" : ctx.guild.id})
                await ctx.send('Auto Role desativado')
                

            server = {"_id": ctx.guild.id, "Nome": ctx.guild.name, "Role": cargo2}
            myquery = { "_id": ctx.guild.id}   
            if (collection2.count_documents(myquery) == 0):
                collection2.insert_one(server)
                await ctx.send('Auto Role setado para o cargo {}'.format(cargo.mention))
            else:
                collection2.update({"_id" : ctx.guild.id}, {"$set":{"Role": cargo2}})
                await ctx.send('Auto Role setado para o cargo {}'.format(cargo.mention))

    @cog_ext.cog_slash(
        name = 'kick',
        description = 'Espulsa alguem do seu server',
        options = [
            create_option(
                name = 'membro',
                description = 'Escolha a pessoa a ser banida',
                option_type = 6,
                required = True
            ),
            create_option(
                name = 'motivo',
                description = 'Escreva o motivo de expulsar',
                option_type = 6,
                required = False
            )
        ]
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def _kick(self, ctx:SlashContext, membro: discord.Member = None, *,motivo=None):
        if ctx.author.id == config.banip:
            return
        else:

            try:
                log = collection.find_one({"_id": ctx.guild.id})
                log2 = log["canal"]
                l1 = self.bot.get_channel(log2)
            finally:

                if motivo == None:
                    motivo = 'Motivo não informado'
                else:
                    motivo = motivo

                e1 = discord.Embed(name = 'kick', description = f'Voce esta prestes a expulsar {membro.mention}')
                R = f'Pessoa expulsa: {membro} \n Quem expulsou: {ctx.author.name} \n Motivo: {motivo}'
                E = discord.Embed(title = 'kick', description = f'Pessoa expulsa: {membro} \n Quem expulsou: {ctx.author.mention} \n motivo: {motivo}')

                if membro == self.bot.user:
                    await ctx.send('Não posso expulsar a mim mesmo')
                elif  membro == ctx.author:
                        await ctx.send('Você não pode expulsar a si mesmo')
                else:
                    message = await ctx.send(embed = e1)
                    await message.add_reaction("✅")
                    await message.add_reaction("❎")

                    def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) in ["✅", "❎"]

                    try:
                        reaction, user = await self.bot.wait_for("reaction_add", check=check)

                        if str(reaction.emoji) == "✅":
                            await message.delete()
                            try:
                                await l1.send(embed = E)
                                await ctx.send(f'{membro.name} expulso com sucesso')
                                await membro.kick(reason = R)
                            except:
                                await ctx.send(embed = E)
                                await ctx.send('Canal de logs não setado use o setlogs')
                                await membro.kick(reason = R)
                        elif str(reaction.emoji) == "❎":
                            await message.delete()
                            await ctx.send(f'ufa, ainda bem que expulsar o {membro.mention}')

                    except asyncio.TimeoutError:
                        return

    @cog_ext.cog_slash(
        name = 'Ban',
        description = 'Espulsa alguem do seu server',
        options = [
            create_option(
                name = 'membro',
                description = 'Escolha a pessoa a ser banida',
                option_type = 6,
                required = True
            ),
            create_option(
                name = 'motivo',
                description = 'Escreva o motivo de expulsar',
                option_type = 6,
                required = False
            )
        ]
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def _Ban(self, ctx:SlashContext, membro: discord.Member = None, *,motivo=None):
        if ctx.author.id == config.banip:
            return
        else:
            
            try:
                log = collection.find_one({"_id": ctx.guild.id})
                log2 = log["canal"]
                l1 = self.bot.get_channel(log2)
            except:
                if motivo == None:
                    motivo = 'Motivo não informado'
                else:
                    motivo = motivo

                e1 = discord.Embed(name = 'kick', description = f'Voce esta prestes a expulsar {membro}')
                R = f'Pessoa expulsa: {membro} \n Quem expulsou: {ctx.author.name} \n Motivo: {motivo}'
                E = discord.Embed(title = 'kick', description = f'Pessoa expulsa: {membro} \n Quem expulsou: {ctx.author.mention} \n motivo: {motivo}')

                if membro == self.bot.user:
                    await ctx.send('Não posso expulsar a mim mesmo')
                elif  membro == ctx.author:
                        await ctx.send('Você não pode expulsar a si mesmo')
                else:
                    message = await ctx.send(embed = e1)
                    await message.add_reaction("✅")
                    await message.add_reaction("❎")

                    def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) in ["✅", "❎"]
                    try:
                        reaction, user = await self.bot.wait_for("reaction_add", check=check)

                        if str(reaction.emoji) == "✅":
                            await message.delete()
                            try:
                                await l1.send(embed = E)
                                await ctx.send(f'{membro.name} banido com sucesso')
                                await membro.ban(reason = R)
                            except:
                                await ctx.send(embed = E)
                                await ctx.send('Canal de logs não setado use o setlogs')
                                await membro.ban(reason = R)
                        elif str(reaction.emoji) == "❎":
                            await message.delete()
                            await ctx.send(f'ufa, ainda bem que banir o {membro}')
                                        

                    except asyncio.TimeoutError:
                        return

    @cog_ext.cog_slash(
        name='Say', 
        description='Fala algo no server',
        options = [
            create_option(
                name = 'msg',
                description = 'Esceva oq deseja falar',
                option_type = 3,
                required = True
            )
        ]
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_channels = True)
    async def _say(self, ctx:SlashContext, *, msg = None):
        if ctx.author.id == config.banip:
            return
        else:
            
            if msg == None:
                await ctx.send('Você precisa falar algo')
            else:
                await ctx.send(f'{msg} \n\nFalado por {ctx.author.mention}')

    @cog_ext.cog_slash(    
        name = 'Clear', 
        description = 'Limpa o chat',
        options = [
            create_option(
                name = 'quantidade',
                description = 'escolha uma quantidade para limpar',
                option_type = 4,
                required = True
            )
        ]
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(manage_channels = True)
    @commands.has_permissions(manage_channels = True)
    async def _clear(self, ctx:SlashContext, quantidade = 0):
        if ctx.author.id == config.banip:
            return
        else:
            
            if quantidade > 1000:
                await ctx.send('O limite maximo é de 1000 palavras')
                return
            elif quantidade == 0:
                await ctx.send('Você precisa escolher uma quantidade de mensagens, a quantidade maxima é 1000 mensagens')
            else:
                purge = await ctx.channel.purge(limit=quantidade)
                await asyncio.sleep(10)
                await ctx.send(f"O chat teve {len(purge)} mensagens apagadas por {ctx.author.mention}")

    @cog_ext.cog_slash(
        name = 'Banid',
        description = 'Bane alguem do seu server sem estar nele pelo id',
        options = [
            create_option(
                name = 'membro',
                description = 'Coloque o id',
                option_type = 6,
                required = True
            ),
            create_option(
                name = 'motivo',
                description = 'Escreva o motivo de Banir',
                option_type = 3,
                required = False
            )
        ]
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def _banid(self, ctx, membro: int, *,motivo=None):
        if ctx.author.id == config.banip:
            return
        else:
            
            try:
                log = collection.find_one({"_id": ctx.guild.id})
                log2 = log["canal"]
                l1 = self.bot.get_channel(log2)
            finally:

                member1 = await self.bot.fetch_user(membro)

                if motivo == None:
                    motivo = 'Motivo não informado'
                else:
                    motivo = motivo

                e1 = discord.Embed(name = 'BanId', description = f'Voce esta prestes a banir {membro}')
                R = f'Pessoa banida: {membro} \n Quem baniu: {ctx.author.name} \n Motivo: {motivo}'
                E = discord.Embed(title = 'ban', description = f'Pessoa banida: <@{membro}> \n Quem baniu: {ctx.author.mention} \n Motivo: {motivo} \n id: {membro}')

                if membro == self.bot.user:
                    await ctx.send('Não posso banir a mim mesmo')
                elif  membro == ctx.author:
                        await ctx.send('Você não pode banir a si mesmo')
                else:
                    message = await ctx.send(embed = e1)
                    await message.add_reaction("✅")
                    await message.add_reaction("❎")
                                
                    def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) in ["✅", "❎"]
                    try:
                        reaction, user = await self.bot.wait_for("reaction_add", check=check)

                        if str(reaction.emoji) == "✅":
                            await message.delete()

                            try:
                                await ctx.guild.ban(member1, reason = R)
                                await l1.send(embed = E)
                                await ctx.send(f'{membro} banido com sucesso')
                            except Exception:

                                await ctx.guild.ban(member1, reason = R)
                                await ctx.send(embed = E)
                                await ctx.send('Canal de logs não setado use o setlogs')

                        elif str(reaction.emoji) == "❎":
                            await message.delete()
                            await ctx.send(f'ufa, ainda bem que banir o {membro}')

                    except asyncio.TimeoutError:
                        return

    @cog_ext.cog_slash(
        name='Unban', 
        description='Desbane um membro pelo id',
        options = [
            create_option(
                name = 'id',
                description = 'Coloque o id para desbanir',
                option_type = 6,
                required = True
            ),
            create_option(
                name = 'razão',
                description = 'Escreva a razão',
                option_type = 3,
                required = False
            )
        ]
    )
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def _unban(self, ctx:SlashContext, id: int, *, razão = None):
        if ctx.author.id == config.banip:
            return
        else:
            
            try:
                log = collection.find_one({"_id": ctx.guild.id})
                log2 = log["canal"]
                l1 = self.bot.get_channel(log2)
            finally:

                if razão == None:
                    razão = 'Não informado'
                else:
                    razão = razão

                e = discord.Embed(name = 'UnBan',
                description = f'Quem desbaniu: {ctx.author}\n quem foi desbanido: <@{id}> \nrazão: {razão}')
                try:
                    user = await self.bot.fetch_user(id)
                    await l1.send(embed = e)
                    await ctx.send(f'{id} desbanido com sucesso')
                    await ctx.guild.unban(user)
                except:
                    user = await self.bot.fetch_user(id)
                    await ctx.send(embed = e)
                    await ctx.guild.unban(user)

    @_setlogs.error
    async def setlogs_error(self,ctx: commands.context, error):
        if isinstance(error, commands.MissingPermissions):
            
            await ctx.send("Você não tem permissão para usar esse comando")

    @_autorole.error
    async def setlogs_error(self,ctx: commands.context, error):
        if isinstance(error, commands.MissingPermissions):
            
            await ctx.send("Você não tem permissão para usar esse comando")

    @_kick.error
    async def kick_error(self,ctx: SlashContext, error):
        if isinstance(error, commands.CommandOnCooldown):

            await ctx.send('Você precisa esperar 5 segundos parta usar esse comando de novo')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.send("Você não tem permissão para usar esse comando")

        if isinstance(error, commands.BadArgument):

            await ctx.reply('Eu não encontrei esse membro no server para expulsar')

        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.send('Desculpa, mas eu não tenho permissão "Kick_Members" para usar esse commando')

    @_Ban.error
    async def ban_error(self,ctx: commands.context, error):
        if isinstance(error, commands.CommandOnCooldown):

            await ctx.send('Você precisa esperar 5 segundos parta usar esse comando de novo')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.send("Você não tem permissão para usar esse comando")

        if isinstance(error, commands.MemberNotFound):

            await ctx.send('Eu não encontrei esse membro no server para banir, se deseja banir ele, use o "BanId"')

        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.send('Desculpa, mas eu não tenho permissão "Ban_Members" para usar esse commando')

    @_unban.error
    async def unban_error(self,ctx: commands.context, error):
        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.send('Desculpa, mas eu não tenho permissão "Ban_Members" para usar esse commando')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.send("Você não tem permissão para usar esse comando")

    @_say.error
    async def say_error(self,ctx: commands.context, error):
        if isinstance(error, commands.CommandOnCooldown):

            await ctx.send(f'Você precisa esperar 5 segundos para  usar esse comando de novo')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.send("Você não tem permissão para usar esse comando")

    @_clear.error
    async def clear_error(self,ctx: commands.context, error):
        if isinstance(error, commands.CommandOnCooldown):

            await ctx.send(f'Você precisa esperar 5 segundos para  usar esse comando de novo')
        
        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.send('Desculpa, mas eu não tenho permissão "Manage_chennels" para usar esse commando')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.send("Você não tem permissão para usar esse comando")

    @_banid.error
    async def clear_error(self,ctx: commands.context, error):
        if isinstance(error, commands.CommandOnCooldown):

            await ctx.send(f'Você precisa esperar 5 segundos para  usar esse comando de novo')
        
        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.send('Desculpa, mas eu não tenho permissão "Manage_chennels" para usar esse commando')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.send("Você não tem permissão para usar esse comando")

async def update_prefix(id, prefix):

    if id is not None:
        collection2.update_one({"_id": id.id}, {"$set": {f"prefix": prefix}})

def setup(bot):
    bot.add_cog(_Mod(bot))