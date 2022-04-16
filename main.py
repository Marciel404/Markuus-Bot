#--------------------------imports---------------------------
import os, discord, requests
#--------------------------imports---------------------------
#--------------------------Froms--------------------------
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from discord_slash import SlashCommand, SlashContext
from pymongo import MongoClient
from Outhers.Random import IdS
#--------------------------Froms--------------------------
cluster = MongoClient("#")

db = cluster["Bank"]
collection = db["Prefix"]

def get_prefix(client, message):
    prefixes = collection.find_one({"_id": message.guild.id})
    pre = prefixes['prefix']
    return pre

#--------------------------?--------------------------
load_dotenv()
token = getenv("TOKEN")

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(
command_prefix=get_prefix,
help_command=None,
case_insensitive = True,
intents = intents
)

slash = SlashCommand(client, sync_commands=True)

#--------------------------?--------------------------

for filename in os.listdir('./Commands'):
    if filename.endswith('.py'):
        client.load_extension(f'Commands.{filename[:-3]}')

for filename in os.listdir('./Commands_Slash'):
    if filename.endswith('.py'):
        client.load_extension(f'Commands_Slash.{filename[:-3]}')

for filename in os.listdir('./Outhers'):
    if filename.endswith('.py'):
        client.load_extension(f'Outhers.{filename[:-3]}')

@client.command()
async def t1(ctx, thx):
        if ctx.author.id != IdS:
            return
        else:
            e = discord.Embed()
            r = requests.get(
                    f'http://nekos.life/api/v2/img/{thx}')
            res = r.json()

            e.set_image(url=res['url'])
            await ctx.send(embed = e)

client.run(token)