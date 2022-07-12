# bot.py
import os

#import discord package
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client(out bot)
client = discord.Client()

# asnyc event
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# run the client on the server
client.run(TOKEN)