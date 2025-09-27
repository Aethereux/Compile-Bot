import discord
import os
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="-", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def send(ctx, *args):
    out = ""
    for arg in args:
        out += " " + arg
    await ctx.send(out)


def run_bot():
    token = os.getenv("COMPILE_BOT_TOKEN")
    if token is None or token == "":
        print("Bot token not found!")
        return

    bot.run(token)


run_bot()
