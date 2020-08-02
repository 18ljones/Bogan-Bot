import discord
from database.bogan_db import db
from discord.ext import commands
import asyncio
import random

class Minigames(commands.Cog):

    def __init__(self, client, *args, **kwargs):
        self.client = client

    @commands.command(name="dice")
    async def dice(self, ctx, bet : int):
        curpts = int(db.get_points(ctx.author.id))
        if curpts >= bet :
            roll = random.randint(1,100)
            if roll > 55:
                winpts = int(bet * 1.1)
                db.add_points(ctx.author.id, winpts)
                await ctx.send(f"{ctx.author.mention} rolled a {roll} and won {winpts} Bogan Points!")
            else:
                db.remove_points(ctx.author.id, bet)
                await ctx.send(f"{ctx.author.mention} rolled a {roll} and lost {bet} Bogan Points...")
        else:
            await ctx.send("You do not have enough Bogan Points to make that bet.")

    @commands.command(name="50/50")
    async def fifty_fifty(self, ctx, bet : int):
        curpts = int(db.get_points(ctx.author.id))
        if curpts >= bet :
            roll = random.randint(1,2)
            if roll == 2:
                db.add_points(ctx.author.id, bet)
                await ctx.send(f"{ctx.author.mention} is a WINNER! You've earned {bet} Bogan Points!")
            else:
                db.remove_points(ctx.author.id, bet)
                await ctx.send(f"{ctx.author.mention} loses. You lost {bet} Bogan Points...")
        else:
            await ctx.send("You do not have enough Bogan Points to make that bet.")

    @commands.command(name="number_pick")
    async def pick_a_number(self, ctx, range : int, number_picked : int, bet : int):
        curpts = int(db.get_points(ctx.author.id))
        if curpts >= bet :
            roll = random.randint(1,range)
            if roll == number_picked:
                winpts = int(bet * (range * .75))
                db.add_points(ctx.author.id, winpts)
                await ctx.send(f"The number is {roll}! {ctx.author.mention} won {winpts} Bogan Points!")
            else:
                db.remove_points(ctx.author.id, bet)
                await ctx.send(f"The number is {roll}! {ctx.author.mention} lost {bet} Bogan Points...")
        else:
            await ctx.send("You do not have enough Bogan Points to make that bet.")

def setup(bot):
    bot.add_cog(Minigames(bot))
    print('Minigames loaded')