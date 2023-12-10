from pyrogram import filters
from BotConfig import bot
from texts import main_menu_text
from keyboards import main_keyboard , gif_keyboard , image_keyboard
from texts import img_category , gif_category
from Tools import Send_gif_request , Send_img_request , random_anime , main_menu




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
        
    elif text in img_category:
        
        await Send_img_request(chat_id, text)
        
    elif text in gif_category:
        
        await Send_gif_request(chat_id, text)
        
    elif text == "Anime":
        
        await random_anime(chat_id)
        
    elif text == "cancel":
        
        await main_menu(chat_id)
        
        
        
        
bot.run()