import os
import discord
from dotenv import load_dotenv

# load env variables
load_dotenv()
# get discord tokens to allow access to API and guild (server)
TOKEN = os.getenv('DISCORD_TOKEN') # can only be used by who created the discord application
GUILD = os.getenv('DISCORD_GUILD')

# create discord client
client = discord.Client()

# event handler for when connection is established
@client.event
async def on_ready():
    # in case the bot is connected to multiple guilds, this will search for the guild we want
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} is connected to guild: {guild.name} (id: {guild.id})')

# event handler for new member join coroutine
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name}, welcome to the Discord server!'
    )



'''
    # display list of users currently in the guild/server
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
'''
client.run(TOKEN)
