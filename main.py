import fileinput
import os
import pytz
import telegram
from config import API_TOKEN
from youtube_downloader import YouTube_Audio_Downloader
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters,CallbackQueryHandler
from telegram.ext import Updater
from telegram import ForceReply, Update ,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters, 
)

from telegram import __version__ as TG_VER


current_directory = os.getcwd()
# get iran timezone
country_time_zone = pytz.timezone('Asia/Tehran')


# get las version of this telegram compenent
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

import requests
import re

def extract_video_id(url):
    # Regular expression to extract the video ID from YouTube URL
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        return None

def check_youtube_link_validity(url):

        try:
            response = requests.get(url)
            if response.status_code == 200:
                    return True  # Valid YouTube video

        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return False  # Error occurred, not a valid video

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully.")
    else:
        print(f"Directory '{directory}' already exists.")


    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:    
    some_url = {}
    if(check_youtube_link_validity(update.message.text)):
        await update.message.reply_text("Downloading Audio...")
        create_directory_if_not_exists(current_directory + "\\musics")
        video_name =  YouTube_Audio_Downloader(current_directory + "\\musics", update.message.text, someURL= some_url)       
         
        await update.message.reply_audio(title=video_name,
                                         thumbnail=open(current_directory + f"\\musics\\{video_name}.jpg", 'rb'),
                                          audio=open(current_directory + f"\\musics\\{video_name}.mp3", 'rb'))
    else:
        await update.message.reply_text("Invalid Link ...")

    return

def main():
    application = Application.builder().token(API_TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL& ~filters.COMMAND, echo))
    application.run_polling()

if __name__ == "__main__":
    main()