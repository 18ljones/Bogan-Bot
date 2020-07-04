import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
_points = {'Bogan Bot':100}


# grabs the token for the bot from "token.txt" (this txt file is not included in the GitHub repo)
def get_token():
    with open("token.txt", "r") as file:
        return file.readlines()[0].strip()

_token = get_token()

@client.event
async def on_ready():
    for name in client.users:
        if(name != client.user):
            _points[name] = 0
            print(name)
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    _points[member] = 1
    await member.channel.send('{} has joined and been given 1 Bogan Point'.format(member.mention))

@client.command(name='points') 
async def get_points(ctx):
    await ctx.send('{} has {} points!'.format(ctx.author.mention, _points[ctx.author]))

# TODO: add ignore casing for member parameter
@client.command()
async def add_points(ctx, point, member : discord.Member):
    memFound = False
    memId = ''
    for name in _points:
        if str(member) in str(name):
            _points[name] += int(point)
            memId = name
            memFound = True
            break
    if memFound == True:
        await ctx.send('{} has given {} {} Bogan Points!'.format(ctx.author.mention, member.mention, point))
    else:
        await ctx.send('The user {} does not exist'.format(member))


@client.command()
async def pm(ctx, arg):
    await ctx.send(arg[1:])

#client.add_command(pm)
#client.add_command(message)

client.run(_token)