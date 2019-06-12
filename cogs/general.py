from discord.ext import commands
from cogs.util import check
import discord

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Pong"""
        await ctx.send("Pong!")

    @commands.command()
    async def repeat(self, ctx, *, arg):
        await ctx.send(f"{arg}")

    @commands.command()
    async def hitormiss(self, ctx):
        await ctx.send("I guess I never miss, huh?")

    @check.is_contributor()
    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def example(self, ctx, *, string: str = None):
        """Example of a check for user being a contributor"""
        msg = "".join("    " if char == ' ' else f':regional_indicator_{char}:' for char in string if char.isalnum() or
                       char == ' ')
        await ctx.send(f'{msg}')



def setup(bot):
    bot.add_cog(General(bot))
