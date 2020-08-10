import os
import discord
import random
from joke_generator import generate # 'pip install joke-generator'
from dotenv import load_dotenv
from discord.ext import commands


# loads env variables
load_dotenv()
# get discord token to allow access to API
'''
Token subject to change. If you want to use this repo as a template to create
your Discord Bot, after creating a Discord Application/Bot on the Discord
Developer Portal, take the Token given when the Bot was created and replace
the old token with your token in the '.env' file.
'''
TOKEN = os.getenv('DISCORD_TOKEN')
# Creates Discord Bot. To invoke this bot, text commands towards it must be prefixed with '!'
bot = commands.Bot(command_prefix='!')

# event handler for when connection is established
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# event handler for new member join coroutine
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name}, welcome to my Discord server!'
    )

# event handler for when interaction with the bot occurs
@bot.command(name='Hi', help='Responds with a greeting message')
async def message_hi(ctx):
    # lists of responses to choose from
    greetings_responses = [f'Hi :)', 'Hello There ( ͡° ͜ʖ ͡°)', 'Greetings ( ͡ᵔ ͜ʖ ͡ᵔ )']

    response = random.choice(greetings_responses)
    await ctx.send(response)

@bot.command(name='Hello', help='Responds with a greeting message')
async def message_hi(ctx):
    # lists of responses to choose from
    greetings_responses = ['Hi :)', 'Hello There ( ͡° ͜ʖ ͡°)', 'Greetings ( ͡ᵔ ͜ʖ ͡ᵔ )']

    response = random.choice(greetings_responses)
    await ctx.send(response)

# tells a random joke
@bot.command(name='Joke', help='Responds with a random joke')
async def message_joke(ctx):
    joke_response = str(generate())
    await ctx.send(joke_response)

# simulates a dice roll
@bot.command('roll_dice', help='Simulation of dice roll; type in # of dice & # of sides per die after command. Ex: !dice_roll 2 3')
async def roll(ctx, numOfDice: int, numOfSides: int):
    dice = [
        str(random.choice(range(1, numOfSides + 1)))
        for _ in range(numOfDice)
    ]
    await ctx.send(', '.join(dice))

# only gives those with the server Admin ('admin') role to create new channels
@bot.command(name='create-channel', help='Type !create-channel "channel name"')
@commands.has_role('admin')
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    # makes sure the new channel does not have the same name as an existing one
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

# throws error when a user without the 'admin' role tries to make a new channel
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the role to execute this command.')

bot.run(TOKEN)
