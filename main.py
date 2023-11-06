from pyrogram import filters
from files import *




@bot.on_message(filters.private)
async def Main_handler(client , message):
    text = message.text
    chat_id = message.chat.id
    if text == "/start":
        await bot.send_message(
            chat_id,
            main_menu_text,
            reply_markup=main_keyboard
            )
    elif text == "Gif":
        await bot.send_message(chat_id,
            "Choose one",
            reply_markup=gif_keyboard                   
            )
    elif text =="Image":
        await bot.send_message(chat_id,"Choose one",reply_markup=image_keyboard)
    elif text in Categories:
        await Send_request(chat_id, text)
    elif text == "cancel":
        await main_menu(chat_id)
bot.run()