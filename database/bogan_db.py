import sqlite3
import sys
import traceback
import discord
from discord.ext import commands

class BoganDB():
    def __init__(self, db_file: str):
        try:
            self.db = sqlite3.connect(str(db_file))
        except Exception as e:
            print(f'Failed to load sqlite file {db_file}', file=sys.stderr)
            traceback.print_exc()
        self.cursor = self.db.cursor()

    def load_on_ready(self, client: commands.Bot):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER, username TEXT, bogan_points INTEGER)")
        for user in client.users:
            if(user.id != client.user.id):
                self.cursor.execute(f"SELECT user_id FROM users WHERE user_id = {user.id}")
                result = self.cursor.fetchone()
                if result is None:
                    sql = ("INSERT INTO users(user_id, username, bogan_points) VALUES(?,?,?)")
                    val = (user.id, user.name, 0)
                    self.cursor.execute(sql, val)
                    self.db.commit()
                #_points[name] = 0
                #(user)
                #print(user.id)
        print('on_ready load successful')

    def member_welcome(self, member : discord.Member):
        self.cursor.execute(f"SELECT user_id FROM users WHERE user_id = {member.id}")
        result = self.cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO users(user_id, username, bogan_points) VALUES(?,?,?)")
            val = (member.id, member.name, 0)
            self.cursor.execute(sql, val)
            self.db.commit()
            return True
        else:
            return False

    def get_points(self, user_id: int):
        self.cursor.execute(f"SELECT bogan_points FROM users WHERE user_id = {user_id}")
        points = self.cursor.fetchone()[0]
        return points

    def add_points(self, user_id: int, points: int):
        self.cursor.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
        result = self.cursor.fetchone()
        print(result)
        if result is not None:
            self.cursor.execute(f"SELECT bogan_points FROM users WHERE user_id = {result[0]}")
            old_points = self.cursor.fetchone()
            sql = ("UPDATE users SET bogan_points = ? WHERE user_id = ?")
            val = ((int(old_points[0]) + int(points)), result[0])
            self.cursor.execute(sql, val)
            self.db.commit()
            return True
        else:
            return False

    def on_close(self):
        self.cursor.close()
        self.db.close()