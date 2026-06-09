import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")

WELCOME = "ahlan! \n\narsil rabat min:\nTikTok\nInstagram\nYouTube\nX (Twitter)\n\nsa-ursil lak alfideo bidun alamah!"

ERROR_MSG = "rabat ghair madfoom, taked min alsahih"

DOWNLOADING = "jari altahmeel..."

SUCCESS = "tam altahmeel bidun alamah maiah"

FAIL = "hatha khata, taked min alrabat wa hawal mujadadan"

PLATFORMS = ["tiktok.com","instagram.com","youtube.com","youtu.be","twitter.com","x.com","t.co"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME)

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    
