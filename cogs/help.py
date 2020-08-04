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
        elif section.lower() == "points" or section.lower() == "bogan_points":
            await ctx.author.send(embed=self.create_boganpoint_embed())
        elif section.lower() == "help":
            await ctx.author.send(embed=self.create_help_embed())
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

    def create_boganpoint_embed(self):
        embed = discord.Embed(
            description = "A list of all Bogan Point related commands with information about how to use them",
            color = discord.Color.gold()
        )

        embed.set_author(name = "Bogan Points")
        embed.add_field(name="!points",
                        value="Displays your Bogan Point balance.",
                        inline=False)
        embed.add_field(name="!add_points <person recieving points : User, amount of points : integer>",
                        value="Gives the specified user the specified amount of points",
                        inline=False)
        embed.add_field(name="!remove_points <person losing points : User, amount of points : integer>",
                        value="Takes the specified amount of points from the specified user.",
                        inline=False)

        return embed

    def create_help_embed(self):
        embed = discord.Embed(
            description = "A list of sections you can get help on.",
            color = discord.Color.gold()
        )

        embed.set_author(name = "Help Sections")
        embed.add_field(name="!help help",
                        value="Displays this help message.",
                        inline=False)
        embed.add_field(name="!help minigame or !help minigames",
                        value="Displays the minigames help message.",
                        inline=False)
        embed.add_field(name="!help points or !help bogan_points",
                        value="Displays the Bogan Points help message.",
                        inline=False)

        return embed

def setup(bot):
    bot.add_cog(Help(bot))
    print('Help loaded')