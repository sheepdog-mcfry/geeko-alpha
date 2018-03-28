import asyncio
import json

import aiohttp
from discord.ext import commands

from .utils import chat_formatting as cf


class CatFact:

    """Gets random cat facts."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.url = "https://catfact.ninja/fact"

    @commands.command(pass_context=True, no_pm=True, name="catfact",
                      aliases=["catfacts"])
    async def _catfact(self, ctx: commands.Context, number: int=1):
        """Gets random cat facts."""

        await self.bot.type()

        async with aiohttp.get(self.url) as response:
            await self.bot.say(await response.json())


def setup(bot: commands.Bot):
    bot.add_cog(CatFact(bot))
