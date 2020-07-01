import datetime
from redbot.core import commands
import discord

class Mycog1(commands.Cog):
    """My custom cog"""


    @commands.command()
    async def countdown(stop):
        while True:
            difference = stop - datetime.datetime.now()
            count_hours, rem = divmod(difference.seconds, 86400)
            count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            await ctx.send("Etkinlik Bitti!")
            break:
        await ctx.send('Etkinliğin bitmesine: '
              + str(difference.days) + " Gün "
              + str(count_hours) + " Saat "
              + str(count_minutes) + " Dakika "
              + str(count_seconds) + " Saniye Kaldı. "
              )
        await asyncio.sleep(1)

end_time = datetime.datetime(2020, 6, 21, 19, 35, 0)
countdown(end_time)
