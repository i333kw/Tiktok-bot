import os
import asyncio
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")
PLATFORMS = ["tiktok.com","instagram.com","youtube.com","youtu.be","twitter.com","x.com","t.co"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ahlan! arsil rabat min TikTok / Instagram / YouTube / X")

def do_download(url):
    opts = {'outtmpl': '/tmp/%(id)s.%(ext)s','format': 'mp4','noplaylist': True,'socket_timeout': 30}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return "/tmp/" + info['id'] + ".mp4"

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if not any(x in url for x in PLATFORMS):
        await update.message.reply_text("rabat ghair madfoom")
        return
    await update.message.reply_text("jari altahmeel...")
    try:
        loop = asyncio.get_event_loop()
        file_path = await asyncio.wait_for(loop.run_in_executor(None, do_download, url), timeout=60)
        await update.message.reply_video(video=open(file_path, 'rb'), caption="tam!")
        os.remove(file_path)
    except asyncio.TimeoutError:
        await update.message.reply_text("waqt taweel, hawal mujadadan")
    except Exception:
        await update.message.reply_text("khata fil tahmeel, taked min alrabat")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download))
app.run_polling()
