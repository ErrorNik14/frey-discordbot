import nextcord
from nextcord.ext import commands
import os

intents = nextcord.Intents()
intents.members = True
bot = commands.Bot(command_prefix="d!", intents=intents, case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_connect():
    print("Bot activated!")


bot.run("TOKEN")
#Use the bot token which is in the group dm ping when testing or running bot,
#but ALWAYS change it back to bot.run(os.)