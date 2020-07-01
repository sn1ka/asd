import datetime
from redbot.core import commands
import discord

class Mycog1(commands.Cog):
    """My custom cog"""


    @commands.command()
    async def sure(self, ctx):
        x = datetime.datetime(2020, 6, 21, 19, 35, 0)
        count_hours, rem = divmod(difference.seconds, 86400)
        count_minutes, count_seconds = divmod(rem, 60)
        await ctx.send(x)
    if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
        await ctx.send("bitti")
