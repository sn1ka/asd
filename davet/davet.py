
from redbot.core import commands
import discord

class Mycog1(commands.Cog):
    """My custom cog"""


    @commands.command()
    async def davet(self, ctx):
        """Ganesh botu sunucuna davet etmek için aşağıdaki linkleri kullanabilirsin."""
        # Your code will go here
        e = discord.Embed() 
        e.title = "Davet"
        e.description = "Ganesh’i sunucunuzda görmekten mutluluk duyarız! **!yardım** komutu ile komutları görüntüleyebilirsiniz.**Ya da isterseniz aşağıdaki linki kullanabilirsiniz**" 
        e.colour = discord.Color.red()
        await ctx.author.send(embed=e) # send it

        e2 = discord.Embed() 
        e2.title = "<Davet>"
        e2.description = "Ganesh’i sunucunuzda görmekten mutluluk duyarız! **!yardım** komutu ile komutları görüntüleyebilirsiniz." 
        e2.colour = discord.Color.red()
        await ctx.author.send(embed=e2) # send it
