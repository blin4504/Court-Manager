# court.py

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

court_1 = court_2 = court_3 = court_4 = []
queue = []
intents=discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def add(ctx, *, arg):
    parsed = arg.split(", ")
    queue.extend(parsed)
    people = ' '.join(queue)
    await ctx.send(f'added {people}')
    

@bot.command(name='queue')
async def _queue(ctx):
    peoples = '\n'.join(queue)
    await ctx.send(peoples)

bot.run(TOKEN)

