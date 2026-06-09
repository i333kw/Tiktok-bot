import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text(
       "مرحباً بك! 👋\n\n"
       "أرسل لي رابط TikTok\n"
       "وسأرسل لك الفيديو فوراً للحفظ بدون علامة مائية 🎵"
   )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
   url = update.message.text
   if "tiktok.com" not in url:
       await update.message.reply_text("❌ أرسل رابط TikTok صحيح")
       return

   await update.message.reply_text("⏳ جاري التحميل...")

   try:
       ydl_opts = {
           'outtmpl': '/tmp/%(id)s.%(ext)s',
           'format': 'mp4',
       }
       with yt_dlp.YoutubeDL(ydl_opts) as ydl:
           info = ydl.extract_info(url, download=True)
           file_path = f"/tmp/{info['id']}.mp4"

       await update.message.reply_video(video=open(file_path, 'rb'))
       os.remove(file_path)

   except Exception as e:
       await update.message.reply_text("❌ حدث خطأ، تأكد من الرابط")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download))
app.run_polling()
