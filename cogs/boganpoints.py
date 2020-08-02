import discord
from database.bogan_db import db
from discord.ext import commands
import asyncio

class BoganPoint(commands.Cog):

    def __init__(self, client, *args, **kwargs):
        self.client = client
        #self.db = BoganDB('main.sqlite')

    @commands.command(name='points') 
    async def get_points(self, ctx):
        points = db.get_points(ctx.author.id)
        await ctx.send(f'{ctx.author.mention} has {points} points!')


    @commands.command(aliases=['give_points'])
    async def add_points(self, ctx, member: discord.Member, points: int):
        added_points = db.add_points(member.id, points)

        if added_points:
            await ctx.send('{} has given {} {} Bogan Points!'.format(ctx.author.mention, member.mention, points))
        else:
            await ctx.send('The user {} does not exist'.format(member))

    @commands.command(aliases=['take_points'])
    async def remove_points(self, ctx, member: discord.Member, points: int):
        removed_points = db.remove_points(member.id, points)

        if removed_points:
            await ctx.send('{} has removed {} Bogan Points from {}!'.format(ctx.author.mention, points, member.mention))
        else:
            await ctx.send('The user {} does not exist'.format(member))


    #def __del__(self):
    #    db.on_close()

def setup(bot):
    bot.add_cog(BoganPoint(bot))
    print('BoganPoint loaded')

            