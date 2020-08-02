import os
import discord
import asyncio
import sqlite3
from discord.ext import commands
from database.bogan_db import db
import sys
import traceback

client = commands.Bot(command_prefix = '!')
client.remove_command('help')
#db = BoganDB('main.sqlite')

#load cogs
client.load_extension('cogs.boganpoints')
client.load_extension('cogs.welcome')
client.load_extension('cogs.minigames')
client.load_extension('cogs.help')

# grabs the token for the bot from "token.txt" (this txt file is not included in the GitHub repo)
def get_token():
    with open("token.txt", "r") as file:
        return file.readlines()[0].strip()

_token = get_token()

@client.event
async def on_ready():
    db.load_on_ready(client)
    print('We have logged in as {0.user}'.format(client))

@client.command(name='stop')
async def stop_bot(ctx):
    if str(ctx.author) == 'runedj#5221':
        await ctx.send('Closing bot...')
        db.on_close()
        await client.close()
        exit()
    else:
        await ctx.send('You do not have permission to run this command')
        
if __name__ == '__main__':
    client.run(_token)



