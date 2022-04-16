from pymongo import MongoClient
from discord.ext import commands
cluster = MongoClient("#")

db = cluster["Bank"]
logs = db["Logs"]
autorule = db["AutoRole"]
prefix = db["Prefix"]

class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))