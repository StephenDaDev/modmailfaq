import asyncio
import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

#Cog = getattr(commands, "Cog", object)


class testcog(commands.Cog):
    
    """Testing"""


@commands.command
@checks.has_permissions(PermissionLevel.SUPPORTER)
async def sayhi(self, ctx):
     await ctx.send('Hi MiTondoot!')
        

def setup(bot):
    bot.add_cog(testcog(bot))
