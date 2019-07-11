import asyncio

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)


class testcog(Cog):
    """DO NOT EAT MY MODMAIL PLUGIN UNDER ANY CIRCUMSTANCES
    """


@commands.command
@checks.has_permissions(PermissionLevel.SUPPORTER)
async def sayhi(self, ctx):
     await ctx.send('Hi MiTondoot!')
        

bot.add_cog(testcog(bot))
