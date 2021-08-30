import discord
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path
import os
import random

client = commands.Bot(command_prefix='.')


def main():
    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    TOKEN = os.getenv("TOKEN")
    client.run(TOKEN)


@client.event
async def on_ready():  # detects when bot is ready
    print("Bot is up")  # prints to terminal


@client.command()
async def hello(ctx):
    await ctx.reply("Hey <@" + str(ctx.message.author.id) + "> !")


@client.command(name="rng")
async def rng(ctx, num):
    await ctx.send(random.randint(0, int(num)))


@client.command(name="echo")
async def echo(ctx, *args):
    await ctx.send(" ".join(args))


@client.command()
async def ping(ctx, user: discord.Member, num):
    if (int(num) > 5):
        return await ctx.send("Too many pings!")
    for i in range(int(num)):
        await ctx.send("<@" + str(user.id) + ">")


@client.command(aliases=["forcequit", "fq", "dc", "kill"])  # sets command aliases
@commands.is_owner()  # checks if the person running the command is an owner
async def shutdown(ctx):
    await ctx.send("Bot successfully shut down!")  # returns success message
    await ctx.bot.logout()  # kills bot


@client.command()
async def count(ctx, *, words):
    words_array = words.split()
    await ctx.send(len(words_array))

main()
