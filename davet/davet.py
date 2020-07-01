import datetime
from redbot.core import commands
import discord

class Mycog1(commands.Cog):
    """My custom cog"""


    @commands.command()
    async def sure(self, ctx):
        x = datetime.datetime(2023, 6, 21, 19, 35, 0)
        await ctx.send(x)
