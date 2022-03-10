import nextcord
from nextcord.ext import commands

intents = nextcord.Intents()
intents.members = True
bot = commands.Bot(command_prefix="d!", intents=intents, case_insensitive=True)
bot.remove_command(help)

@bot.event
async def on_connect():
    print("Bot activated!")


bot.run("TOKEN")