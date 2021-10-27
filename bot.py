import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['.'])

@bot.command() 
async def hello(ctx): 
    author = ctx.message.author 

    await ctx.send(f'Hello, {author.mention}!')

    bot.run('OTAyOTEzNjIwODc3Mzk0MDEw.YXlV1g.TGTPnzAZxw_bdD_2XBV13nbhz1M')