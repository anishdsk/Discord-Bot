# Multipurpose-Discord-Bot

 ## Capabilites:
    - Basic chatting
    - Direct welcome messages when a member joins server
    - Displays GIFs/memes
    - Cracks Jokes
    - Simulates dice rolls
    - Logs bot and server activites to an external .log file
    - Restricts channel creation to only those with 'admin' roles

## Prerequisites:
    - Clone repo
    - Create a Discord account
   
    - Create an Application in the Discord Developer Portal
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
    - The 'Discord.log' file should be deleted as your process will generate a new one as the program runs
    

    
