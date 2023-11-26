from requests import get
from BotConfig import *
from keyboards import *
from texts import *


# --- [ Main Menu ] --- #

async def main_menu(chat_id):
    
    await bot.send_message(chat_id , 'Welcome' , reply_markup = main_keyboard)


# --- [ Image Request ] --- #

async def Send_img_request(chat_id,text):
    
    result = get("https://nekos.best/api/v2/"+ text)
    result = result.json()
    result = result['results'][0]['url']
    
    await bot.send_photo(chat_id , result , caption = text)
    
# --- [ Gif Request ] --- #

async def Send_gif_request(chat_id , text):
    
    result = get("https://nekos.best/api/v2/"+ text)
    result = result.json()
    result = result['results'][0]['url']
    
    await bot.send_animation(chat_id , result , caption = text)
    
    

# --- [ Random Anime ] --- #

async def random_anime(chat_id):
    
    result = get("https://api.jikan.moe/v4/random/anime")
    result = result.json()
    
    title = result["data"]["title"]

    title_e = result["data"]["title_english"]
    
    image = result["data"]["images"]["jpg"]["large_image_url"]
    
    synopsis = result["data"]["synopsis"]
    
    genres:list = result["data"]["genres"]
        
    Genres = []
    
    genres_count = genres.__len__()
        
    if genres_count == 0:
        
        GenreS = "None"
    
    else:
        
        for i in range(0,genres_count):
        
            Genres.append("\n#")
            Genres.append(genres[i]["name"])
        
        GenreS = "".join(Genres)
        
        
    score = result["data"]["score"]
    
    await bot.send_photo(chat_id,image,caption = anime_text.format(title,title_e,GenreS,synopsis,score))