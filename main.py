import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Oh Hey, so you here to pirate things.\nChoose a category below:"
    keyboard = [
        [InlineKeyboardButton("Movies", callback_data='pirate_movies')],
        [InlineKeyboardButton("Music", callback_data='pirate_music')],
        [InlineKeyboardButton("Books", callback_data='pirate_books')],
    ]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'pirate_movies':
        keyboard = [
            [InlineKeyboardButton("Source 1", url="https://t.me/SnowballOfficialBot")],
            [InlineKeyboardButton("Source 2", url="https://t.me/GDFatheribot")],
            [InlineKeyboardButton("Source 3", url="https://t.me/Angela2_moviebot")],
            [InlineKeyboardButton("Source 4", url="https://t.me/ProSearchM6Bot")],
            [InlineKeyboardButton("Source 5", url="https://t.me/c/2637750174/812")],
        ]
        await query.edit_message_text("Choose your MOVIE source below ⬇️", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == 'pirate_music':
        keyboard = [
            [InlineKeyboardButton("Source 1", url="https://t.me/deezload2bot")],
            [InlineKeyboardButton("Source 2", url="https://t.me/MusicDownloaderRobot")],
        ]
        await query.edit_message_text("Here are some MUSIC bots 🎶", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == 'pirate_books':
        keyboard = [
            [InlineKeyboardButton("Source 1", url="https://t.me/HonoBooksBot")],
        ]
        await query.edit_message_text("Here are some BOOK bots", reply_markup=InlineKeyboardMarkup(keyboard))

async def movies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Source 1", url="https://t.me/SnowballOfficialBot")],
        [InlineKeyboardButton("Source 2", url="https://t.me/GDFatheribot")],
        [InlineKeyboardButton("Source 3", url="https://t.me/Angela2_moviebot")],
        [InlineKeyboardButton("Source 4", url="https://t.me/ProSearchM6Bot")],
        [InlineKeyboardButton("Source 5", url="https://t.me/c/2637750174/812")],
    ]
    await update.message.reply_text("Choose your MOVIE source below ⬇️", reply_markup=InlineKeyboardMarkup(keyboard))

async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Source 1", url="https://t.me/deezload2bot")],
        [InlineKeyboardButton("Source 2", url="https://t.me/MusicDownloaderRobot")],
    ]
    await update.message.reply_text("Here are some MUSIC bots 🎶", reply_markup=InlineKeyboardMarkup(keyboard))

async def books(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Source 1", url="https://t.me/HonoBooksBot")],
    ]
    await update.message.reply_text("Here are some BOOK bots", reply_markup=InlineKeyboardMarkup(keyboard))

async def set_commands(app):
    await app.bot.set_my_commands([
        BotCommand("start", "Start the bot"),
        BotCommand("movies", "Get movie sources"),
        BotCommand("music", "Get music sources"),
        BotCommand("books", "Get book sources"),
    ])

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("movies", movies))
    app.add_handler(CommandHandler("music", music))
    app.add_handler(CommandHandler("books", books))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.post_init = set_commands
    print("Bot is running...")
    app.run_polling()
