from discord.ext import commands
import discord


class Admins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load_cog(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.admin"""
        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e:
            e = discord.Embed(description=f'**`ERROR`** loading {cog} {type(e).__name__} - {e}',
                              colour=discord.Colour(0xFF0000))
            await ctx.send(embed=e)
        else:
            e = discord.Embed(description=f'**`SUCCESSFULLY`** loaded {cog}', colour=discord.Colour(0x278d89))
            await ctx.send(embed=e)

    @commands.has_permissions(administrator=True)
    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload_cog(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.admin"""
        try:
            self.bot.unload_extension(f'cogs.{cog}')
        except Exception as e:
            e = discord.Embed(description=f'**`ERROR`** unloading {cog} {type(e).__name__} - {e}',
                              colour=discord.Colour(0xFF0000))
            await ctx.send(embed=e)
        else:
            e = discord.Embed(description=f'**`SUCCESSFULLY`** unloaded {cog}', colour=discord.Colour(0x278d89))
            await ctx.send(embed=e)

    @commands.has_permissions(administrator=True)
    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.admin"""
        try:
            self.bot.reload_extension(f'cogs.{cog}')
        except Exception as e:
            e = discord.Embed(description=f'**`ERROR`** reloading {cog} {type(e).__name__} - {e}',
                              colour=discord.Colour(0xFF0000))
            await ctx.send(embed=e)
        else:
            e = discord.Embed(description=f'**`SUCCESSFULLY`** reloaded {cog}', colour=discord.Colour(0x278d89))
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Admins(bot))
