import discord
from database.bogan_db import BoganDB
from discord.ext import commands
import asyncio

class Welcome(commands.Cog):

    def __init__(self, client, *args, **kwargs):
        self.client = client
        self.db = BoganDB('main.sqlite')

@commands.Cog.listener()
async def on_member_join(self, member : discord.Member):
    new = self.db.member_welcome(member)

    if new:
        await self.client.guilds[0].send('{} has joined and been given no Bogan Points'.format(member.mention))
    else:
        await self.client.guilds[0].send('Welcome back to the channel {}!'.format(member.mention))


def __del__(self):
    self.db.on_close()

def setup(bot):
    bot.add_cog(Welcome(bot))
    print('Welcome loaded')