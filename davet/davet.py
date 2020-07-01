import datetime
from redbot.core import commands
import discord

class Mycog1(commands.Cog):
    """My custom cog"""


    @commands.command()
    async def sure(self, ctx):
        x = datetime.datetime(2020, 5, 17)
        await ctx.send(x)
