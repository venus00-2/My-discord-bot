import os
import logging
import discord
from discord.ext import commands

# Basic logging
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("DISCORD_TOKEN")
if not TOKEN:
    logging.error("DISCORD_TOKEN environment variable is not set. Exiting.")
    raise SystemExit(1)

intents = discord.Intents.default()
# If your bot needs to read message content, enable this (also enable in Discord dev portal)
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user} (id: {bot.user.id})")
    print(f"Ready — logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    """A simple command to verify the bot is responsive."""
    await ctx.send("Pong!")

if __name__ == "__main__":
    # Run the bot. Token is provided via DISCORD_TOKEN environment variable.
    bot.run(TOKEN)
