from pyrogram.types import ReplyKeyboardMarkup

# --- [Main Keyboard] --- #

main_keyboard = ReplyKeyboardMarkup(
                [
                    ["Gif" , "Image"],
                    ["Anime"]
                ],
                resize_keyboard=True
            )


# --- [Gif Keyboards] --- #

gif_keyboard= ReplyKeyboardMarkup(
    [
        ["baka", "bite", "blush", "bored"],
        ["cry", "cuddle", "dance", "facepalm"],
        ["feed", "handhold", "happy", "highfive"],
        ["laugh", "nod", "nom", "nope"],
        ["pout", "punch", "shoot", "shrug"],
        ["slap", "sleep", "smile", "smug"],
        ["stare", "think", "thumbsup", "tickle"],
        ["wave", "wink", "yeet", "pat"],
        ["hug", "kick","kiss", "poke"],
        ["cancel"]
    ],
    resize_keyboard=True
)

# --- [Image Keyboards] --- #

image_keyboard= ReplyKeyboardMarkup(
    [
        ["husbando", "kitsune", "neko", "waifu"],
        ["cancel"]
    ],
    resize_keyboard=True
)