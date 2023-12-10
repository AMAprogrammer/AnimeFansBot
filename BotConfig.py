from pyrogram import Client

#Import local settings for bot
"""     Creat a file that named local_BotConfig.py and write in it your bot settings 
        (api_id , api_hash and bot_token)
"""
from local_BotConfig import api_ID , api_HASH , token

api_id = api_ID
api_hash = api_HASH
bot_token = token

# Define the bot
bot = Client(
    "AnimeBot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
    )