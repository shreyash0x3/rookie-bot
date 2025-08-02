import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Oh Hey, so you here to pirate things.\nChoose a category below:"
    
    keyboard = [
        [InlineKeyboardButton("📺 Movies", callback_data='pirate_movies')],
        [InlineKeyboardButton("🎵 Music", callback_data='pirate_music')],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'pirate_movies':
        # Show more options for Movies
        keyboard = [
            [InlineKeyboardButton("Captain Snowball", url="https://t.me/SnowballOfficialBot")],
            [InlineKeyboardButton("GodFather", url="https://t.me/GDFatheribot")],
            [InlineKeyboardButton("Unknown", url="https://t.me/c/2637750174/812")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Choose your MOVIE source below ⬇️", reply_markup=reply_markup
        )

    elif query.data == 'pirate_music':
        keyboard = [
            [InlineKeyboardButton("Deezload", url="https://t.me/deezload2bot")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Here are some music bots 🎶", reply_markup=reply_markup
        )



if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()