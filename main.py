#--------------------------imports---------------------------
import os
import discord
import config
import requests
#--------------------------imports---------------------------
#--------------------------Froms--------------------------
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from discord_slash import SlashCommand, SlashContext
from pymongo import MongoClient
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

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

client.run(token)