import os
import discord
import random
import logging
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
from discord.ext import commands

# loads env variables
load_dotenv()

# get Discord and GIPHY tokens to access their APIs
TOKEN = os.getenv('DISCORD_TOKEN')
giphy_token = os.getenv('GIPHY_TOKEN')
# Creates instance of GIPHY API
api_instance = giphy_client.DefaultApi()

''' helper function used by the 'show_gif' command in 'bot.py' '''
# search for a gif using GIPHY API
async def search_gifs(query):
    try:
        # limits how many gif results to choose from and sets content rating to 'pg'
        response = api_instance.gifs_search_get(giphy_token, query, limit=5, rating='pg')
        lst = list(response.data)
        gif = random.choices(lst)
        return gif[0].url
    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

''' logs server and Bot events; called in 'bot.py' '''
def logging_service():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
