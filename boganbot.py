import discord
from discord.ext import commands
import sqlite3

client = commands.Bot(command_prefix = '!')
_points = {'Bogan Bot':100}
db = sqlite3.connect('main.sqlite')
cursor = db.cursor()

# grabs the token for the bot from "token.txt" (this txt file is not included in the GitHub repo)
def get_token():
    with open("token.txt", "r") as file:
        return file.readlines()[0].strip()

_token = get_token()

@client.event
async def on_ready():
    cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER, username TEXT, bogan_points INTEGER)")
    for user in client.users:
        if(user.id != client.user.id):
            cursor.execute(f"SELECT user_id FROM users WHERE user_id = {user.id}")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO users(user_id, username, bogan_points) VALUES(?,?,?)")
                val = (user.id, user.name, 0)
                cursor.execute(sql, val)
                db.commit()
            #_points[name] = 0
            print(user)
            print(user.id)
    print('We have logged in as {0.user}'.format(client))

# TODO: fix welcome messages
@client.event
async def on_member_join(member : discord.Member):
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = {member.id}")
    result = cursor.fetchone()
    if result is None:
        sql = ("INSERT INTO users(user_id, username, bogan_points) VALUES(?,?,?)")
        val = (member.id, member.name, 0)
        cursor.execute(sql, val)
        db.commit()
        await client.guilds[0].send('{} has joined and been given no Bogan Points'.format(member.mention))
    else:
        await client.guilds[0].send('Welcome back to the channel {}!'.format(member.mention))

@client.command(name='points') 
async def get_points(ctx):
    cursor.execute(f"SELECT bogan_points FROM users WHERE user_id = {ctx.author.id}")
    points = cursor.fetchone()[0]
    await ctx.send('{} has {} points!'.format(ctx.author.mention, points))


@client.command()
async def add_points(ctx, member : discord.Member, points):
    #memFound = False
    #for name in _points:
     #   if str(member) in str(name):
      #      _points[name] += int(point)
       #     memId = name
        #    memFound = True
         #   break
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = {member.id}")
    result = cursor.fetchone()
    print(result)
    if result is not None:
        cursor.execute(f"SELECT bogan_points FROM users WHERE user_id = {result[0]}")
        old_points = cursor.fetchone()
        sql = ("UPDATE users SET bogan_points = ? WHERE user_id = ?")
        val = ((int(old_points[0]) + int(points)), result[0])
        cursor.execute(sql, val)
        db.commit()
        await ctx.send('{} has given {} {} Bogan Points!'.format(ctx.author.mention, member.mention, points))
    else:
        await ctx.send('The user {} does not exist'.format(member))

@client.command(name='stop')
async def stop_bot(ctx):
    if str(ctx.author) == 'runedj#5221':
        await ctx.send('Closing bot...')
        cursor.close()
        db.close()
        client.close()
        exit()
    else:
        await ctx.send('You do not have permission to run this command')

#client.add_command(pm)
#client.add_command(message)

client.run(_token)