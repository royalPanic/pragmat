import discord
from discord.ext import commands
import jthon
config = jthon.load('config')
TOKEN = config.get('token').data


def get_prefix(bot, message):
    prefix = config.get('prefix')
    if not prefix:
        prefix = '>'
    return commands.when_mentioned_or(*prefix)(bot, message)


bot = commands.Bot(command_prefix=get_prefix) #allows you to change the bot's prefix


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")


@bot.check #no replying to bots
async def __before_invoke(ctx):
    if not ctx.message.author.bot:
        return True


@commands.is_owner()
@bot.command(aliases=['sp'])
async def setprefix(ctx, prefix: str=None):
    if not prefix or len(prefix) >= 3:
        await ctx.send("Please provide the prefix you would like to use between 1-2 chars.")
    else:
        config['prefix'] = prefix
        config.save()
        await ctx.send(f'Prefix updated to: {prefix}')


@bot.command()
async def repeat(ctx, *, arg):
    await ctx.send(f"{arg}")


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
