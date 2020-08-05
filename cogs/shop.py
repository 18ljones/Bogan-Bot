import discord
from database.bogan_db import db
from config.config import config
from discord.ext import commands
import asyncio

class Shop(commands.Cog):

    def __init__(self, client, *args, **kwargs):
        self.client = client

    @commands.command(name="shop")
    async def list_shop(self, ctx):
        if not bool(config.shop_dict):
            await ctx.send("The shop is empty or has not been configured yet.")
        else:
            await ctx.send(embed=self.create_shop_list())

    @commands.command(name="buy")
    async def buy_role(self, ctx, *, role : str):
        roleB = discord.utils.get(ctx.guild.roles, name=role)
        if roleB:
            if roleB in ctx.author.roles:
                await ctx.send("You already own this role!")
            elif db.get_points(ctx.author.id) >= config.shop_dict[role]:
                db.remove_points(ctx.author.id, config.shop_dict[role])
                await ctx.author.add_roles(roleB)
                await ctx.send(f"{ctx.author.mention} has bought the role {str(roleB)}!")
            else:
                await ctx.send("You do not have enough points to buy this role.")
        else:
            await ctx.send("That role is not in the shop.")


    def create_shop_list(self):
        embed = discord.Embed(
            description = "List of ranks in the shop",
            color = discord.Color.gold()
        )

        embed.set_author(name = "Rank Shop")
        for key in config.shop_dict:
            embed.add_field(name=key,
                            value=f"Cost: {config.shop_dict[key]} Bogan Points",
                            inline=False)
        
        return embed

def setup(bot):
    bot.add_cog(Shop(bot))
    print('Shop loaded')