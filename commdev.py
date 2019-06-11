# imports
import discord
from discord.ext import commands
import json
# var defs
ConfigLoc = 'config.json'
r=open(ConfigLoc,"r")
data=json.load(r)
ConfigJSON=list(data.values())
TOKEN=ConfigJSON[0]
bot = commands.Bot(command_prefix='>') #allows you to change the bot's prefix

@bot.command()
async def repeat(ctx, arg):
    await ctx.send(str(arg))

bot.run(TOKEN) #insert bot token here
