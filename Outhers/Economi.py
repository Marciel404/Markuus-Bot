from discord.ext import commands

from pymongo import MongoClient

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

class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))