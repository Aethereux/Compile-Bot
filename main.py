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
async def send(ctx, arg):
    await ctx.send(arg)

bot.run(os.getenv("COMPILE_BOT_TOKEN"))