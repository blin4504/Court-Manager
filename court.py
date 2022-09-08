# court.py

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

courts = [[], [], [], []]
queue = []
intents=discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def add(ctx, *, arg):
    parsed = arg.split(", ")
    queue.extend(parsed)
    people = ' '.join(queue)
    await ctx.send(f'added {people}')

@bot.command(name='queue')
async def _queue(ctx):
    if (len(queue) > 0):
        peoples = '\n'.join(queue)
        await ctx.send(peoples)
    else:
        await ctx.send('No one is on queue')

@bot.command()
async def play(ctx):
    if (len(queue) < 4):
        await ctx.send('Not enough for a game')
        return

    for court in courts:
        if (len(court) < 4):
            for i in range(4):
                court.append(queue[i])
            del queue[:4]
            return

@bot.command()
async def done(ctx, arg):
    courts[int(arg)-1].clear()
    await ctx.send(f'Court {arg} is open for another game')

@bot.command()
async def info(ctx):
    for court in courts:
        await ctx.send(court)

bot.run(TOKEN)