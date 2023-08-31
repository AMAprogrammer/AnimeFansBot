from requests import get
from BotConfig import *
from keyboards import *


# --- [ Main Menu ] --- #
async def main_menu(chat_id):
    await bot.send_message(chat_id,'Welcome',reply_markup=main_keyboard)


# --- [ Gif Request ] --- #
async def Send_request(chat_id,text):
    result = get("https://nekos.best/api/v2/"+ text)
    result=result.json()
    result=result['results'][0]['url']
    await bot.send_animation(chat_id,result)