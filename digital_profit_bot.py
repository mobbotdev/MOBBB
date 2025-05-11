from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Store your bot token here
BOT_TOKEN = "8028698920:AAFn6NqP2O5mNCypQGp8TqYgaKaNqtEDeXY"

# Your Telegram user ID
ADMIN_ID = 1975772726

# File paths
PICKS_FILE = "picks.txt"
RECORD_FILE = "record.txt"

# Helper function to read from file
def read_file(path):
    if not os.path.exists(path):
        return "No data available yet."
    with open(path, "r") as file:
        return file.read()

# Helper function to write to file
def write_file(path, content):
    with open(path, "w") as file:
        file.write(content)

# Command: /picks
async def picks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args

    if args and args[0].lower() == "update" and user_id == ADMIN_ID:
        new_text = " ".join(args[1:])
        write_file(PICKS_FILE, new_text)
        await update.message.reply_text("Free pick updated.")
    else:
        current = read_file(PICKS_FILE)
        await update.message.reply_text(f"FREE PICK:\n{current}")

# Command: /record
async def record(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args

    if args and args[0].lower() == "update" and user_id == ADMIN_ID:
        new_text = " ".join(args[1:])
        write_file(RECORD_FILE, new_text)
        await update.message.reply_text("Record updated.")
    else:
        current = read_file(RECORD_FILE)
        await update.message.reply_text(f"RECORD:\n{current}")

# Start the bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("picks", picks))
app.add_handler(CommandHandler("record", record))

print("Bot is running...")
app.run_polling()
