import asyncio

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)


class testcog(Cog):
    """DO NOT EAT MY MODMAIL PLUGIN UNDER ANY CIRCUMSTANCES
    """


@commands.command(pass_context=True)
@checks.has_permissions(PermissionLevel.SUPPORTER)
async def emoji(ctx):
    msg = await bot.say("working")
    reactions = ['dart']
    for emoji in reactions: 
        await bot.add_reaction(msg, emoji)
        
          def setup(bot):
          bot.add_cog(testcog(bot))
