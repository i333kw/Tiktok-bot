import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(
        f"👋 أهلاً {name}!\n\n"
        "🎬 أرسل لي رابط فيديو من:\n\n"
        "🎵 TikTok\n"
        "📸 Instagram\n"
        "▶️ YouTube\n"
        "🐦 X (تويتر)\n\n"
        "وسأرسل لك الفيديو للحفظ بدون علامة مائية فوراً! 🚀"
    )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    platforms = [
        "tiktok.com",
        "instagram.com",
        "youtube.com",
        "youtu.be",
        "twitter.com",
        "x.com",
        "t.co"
    ]

    if not any(x in url for x in platforms):
        await update.message.reply_text(
            "❌ رابط غير مدعوم\n\n"
            "المنصات المدعومة:\n"
            "
