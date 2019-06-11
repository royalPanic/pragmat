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

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def repeat(ctx, arg):
    await ctx.send(str(arg))

@bot.command()
async def hitormiss(ctx):
    await ctx.send("I guess I never miss, huh?")

@bot.event # Hopefully handles DMs while bot is online
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        print(f'{message.content} prviate message from {message.author}')
    await bot.process_commands(message)

@bot.event
async def on_connect():
    print("Connecting...")


bot.run(TOKEN) #insert bot token here
