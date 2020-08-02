import discord
from discord.ext import commands
import asyncio

class Help(commands.Cog):

    def __init__(self, client, *args, **kwargs):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self, ctx, section : str):
        if section.lower() == "minigame" or section.lower() == "minigames": 
            await ctx.author.send(embed=self.create_minigame_embed())
        else:
            await ctx.send(f"Could not find help for {section}.")

    def create_minigame_embed(self):
        embed = discord.Embed(
            description = "A list of all minigame commands with information about and how to use them",
            color = discord.Color.gold()
        )

        embed.set_author(name = "Minigames")
        embed.add_field(name="!dice <points to bet : integer>", 
                        value="Roll above a 55 and you win! Roll below a 55 and you lose your bet.",
                        inline=False)
        embed.add_field(name="!50/50 <points to bet: integer>",
                        value="You have a 50-50 chance to win! Winners recieve double their bet! Losers get nothing.",
                        inline=False)
        embed.add_field(name="!number_pick <upper range you want the numbers to be between : integer, your number : integer, points to bet: integer>",
                        value="If your number gets chosen between 1 and your specified upper limit, you win! Otherwise you lose you your bet",
                        inline=False)
        return embed

def setup(bot):
    bot.add_cog(Help(bot))
    print('Help loaded')