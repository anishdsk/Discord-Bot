import os
import discord
import random
from dotenv import load_dotenv

# load env variables
load_dotenv()
# get discord tokens to allow access to API and guild (server)
TOKEN = os.getenv('DISCORD_TOKEN') # can only be used by who created the discord application

# create discord client
client = discord.Client()

# event handler for when connection is established
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# event handler for new member join coroutine
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # lists of responses to choose from
    greetings_responses = ['Hi', 'Hello', 'Greetings']

    if message.content == 'Hello My_Bot' or message.content == 'Hi My_Bot':
        response = random.choice(greetings_responses)
        await message.channel.send(response)
    # raises an exception when "raise-exception" is typed by the user; for testing purposes
    elif message.content == 'raise-exception':
        raise discord.DiscordException

# event handler for when errors are raised with on_message()
# writes errors to external file for logging purposes
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

'''
    # display list of users currently in the guild/server
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
'''
client.run(TOKEN)
