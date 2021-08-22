from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path
import os
import random

import discord

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(name="echo")
async def echo(ctx, *args):
    await ctx.send(" ".join(args))


@client.command(name="bal")
async def bal(ctx):
    await ctx.send("matthew lerman moment")

@client.command(name="rng")
async def rng(ctx, num):
    await ctx.send(random.randint(0, int(num)))

def main():
    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    TOKEN = os.getenv("TOKEN")

    client.run(TOKEN)


main()
