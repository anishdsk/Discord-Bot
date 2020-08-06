import os
import discord
from dotenv import load_dotenv

# load env variables
load_dotenv()
# get discord token to allow access to API
TOKEN = os.getenv('DISCORD_TOKEN')

# create discord client
client = discord.Client()

# event handler for when connection is established
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

client.run(TOKEN)
