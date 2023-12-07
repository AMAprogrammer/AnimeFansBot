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
    result = await anime_req()   
    image , caption = await order_cap(result)
    await bot.send_photo(chat_id,image,caption = caption)
    
    
    
# --- [ Anime Request ] --- #

async def anime_req():
    while True:
        result = get("https://api.jikan.moe/v4/random/anime")
        result = result.json()
        r_type = result["data"]["type"]
        if r_type in ["Monie","TV"]:
            return result

# --- [Ordering Random Anime Caption ] --- #

async def order_cap(result):
            
    title = result["data"]["title"]

    title_e = result["data"]["title_english"]
    
    image = result["data"]["images"]["jpg"]["large_image_url"]
    
    synopsis:str = result["data"]["synopsis"]
    try:
        
        synopsis_len = synopsis.__len__()
        
    except AttributeError:

        synopsis_len = 0
        synopsis = None
        
    if synopsis_len > 400:
        
        synopsis = synopsis[:400]+'...'
    
    
    genres:list = result["data"]["genres"]
        
    Genres = []
    
    genres_count = genres.__len__()
        
    if genres_count == 0:
        
        GenreS = None
    
    else:
        
        for i in range(0,genres_count):
        
            Genres.append("\n#")
            genres_name:str = genres[i]["name"]
            Genres.append(genres_name.replace(" ","_"))
        
        GenreS = "".join(Genres)
        
        
    score = result["data"]["score"]
    
    date = result["data"]["aired"]["prop"]["from"]["year"]
    
    
    caption = '**● Anime :**'
    if title != None:
        caption += f"\n\n**• Name :** {title}"
        
    if title_e != None:
        caption += f"\n\n**• English Name :** {title_e}"
        
    if GenreS != None:
        caption += f"\n\n**• Genre(s) :**{GenreS}"
        
    if synopsis != None:
        caption += f"\n\n**• Synopsis :**\n{synopsis}"
        
    if date != None:
        caption += f"\n\n**• Aired :** {date}"
        
    if score != None:
        caption += f"\n\n**■ Score :** {score}"
        
    return image , caption