# Multipurpose-Discord-Bot

 ## Features:
    - Basic chatting
    - Direct welcome messages when a member joins server
    - Displays GIFs/memes
    - Cracks Jokes
    - Simulates dice rolls
    - Logs bot and server activites to a seperate '.log' file
    - Restricts channel creation to only those with 'admin' roles

## Prerequisites:
    - Clone repo
    - Create a Discord account
   
    - Create an Application in the Discord Developer Portal
          - [https://discord.com/login?redirect_to=%2Fdevelopers](https://discord.com/login?redirect_to=%2Fdevelopers)
    - Now Create a Bot under that Application in the portal
    - Create a Discord Server/Guild where will your bot will go to work
    
    - Add Bot to that server; can be done on the Discord Developer Portal:
          - Select OAuth2 tab in the portal
          - Then on that same tab, select 'bot' in the 'Scopes' box 
          - Then select 'Administrator' in the 'Bot Permissions' box
          - Generate URL under the 'OAUTH2 URL Generator' section
          - Paste URL into browser and go to that page
          - Then authorize your guild from the drop down menu
          - Your bot will now have been added to your guild/server
          
    - Register on the GIPHY Developer Portal and create a new application. 
          - **https://developers.giphy.com/**
    - Then select an API Key. Not SDK. Then an API key will be given
    
    - Generate a token on the Bot page on the Discord Developer Portal
    - Also make sure you have your GIPHY API Key ready
    - Go to the '.env' file
    - Set the value 'DISCORD_TOKEN' equal to your Bot Token
    - Set the value 'GIPHY_TOKEN' equal to your GIPHY API Key
    
## Dependencies (use Pip to install):
    - "pip install discord.py"
    - "pip install giphy_client"
    - "pip install random"
    - "pip install pprint"
    - "pip install joke-generator"
    - "pip install logging" (might be already installed)

## Running the Bot:
    - Make sure all files are in the same folder
    - The 'discord.log' file should be deleted as your process will generate a new one as the program runs
    - Have the 'bot.py' file running now and go to the server with the bot and start using the bot
    
    - The bot's commands must be prefixed with '!'. Like '!Hello' or '!Joke' and multiple more
    - For the full list of commands go to the server and type in '!help'
    - '!help' will bring up a list of all commands, how to invoke them, and their descriptions
    
    - As actions on the server happen and as your bot connects to the server and runs commands, these will be logged in the automatically created 'discord.log' file
    - They will be saved in that file so you can view that history whenever
    
    - Since the bot is not hosted anywhere at the moment, it only runs as long as the program is running in the background
    
## Important Note:
    - If your bot is already running and you make any changes to the code, before you compile and run make sure you generate a new Bot token and replace the old one
    - This makes sure that you don't have multiple instances of the bot running under the same token. This avoids duplicate responses by the bot on the server for any command
    
## Future Updates:
    - Hosting -> so bot is constantly available
    - Advanced chatting features
    - Music streaming capability
    

    
