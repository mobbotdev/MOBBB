import os
from telegram.ext import Updater, CommandHandler

# Your bot token
TOKEN = os.getenv("BOT_TOKEN")

# Your Telegram user ID (admin)
ADMIN_ID = 1975772726

# Initialize the pick and record
current_pick = "No pick has been set yet."
current_record = "No record set yet."

# Command functions
def start(update, context):
    update.message.reply_text("Wassup Family! I'm Mob Bot. Let’s Profit Today 💰")

def help_command(update, context):
    update.message.reply_text("""
Available Commands:
/start – Start the bot
/help – Full list of available commands
/picks – Get today's free sports betting picks
/record – View the recent win/loss record
/vip – Info on how to join the VIP group
/units – Learn about unit sizing and bankroll tips
/rules – Group rules & betting guidelines
/socials – Links to all DPM social media platforms
/about – Info about Digital Profit Mob
/support – Contact for help or issues
""")

def picks(update, context):
    update.message.reply_text(f"Today's Pick:\n{current_pick}")

def setpick(update, context):
    global current_pick
    user_id = update.message.from_user.id
    if user_id == ADMIN_ID:
        current_pick = ' '.join(context.args)
        update.message.reply_text("Today's pick has been updated.")
    else:
        update.message.reply_text("You are not authorized to update the pick.")

def record(update, context):
    update.message.reply_text(f"Recent Win/Loss Record:\n{current_record}")

def setrecord(update, context):
    global current_record
    user_id = update.message.from_user.id
    if user_id == ADMIN_ID:
        current_record = ' '.join(context.args)
        update.message.reply_text("Record updated.")
    else:
        update.message.reply_text("You're not authorized to update the record.")

def vip(update, context):
    update.message.reply_text("To join the VIP group, visit: http://patreon.com/ReeskiDPM")
def units(update, context):
    update.message.reply_text("Unit sizing tips: Here’s some advice on how to size your bets and manage your bankroll effectively.")
- update.message.reply_text("""Unit sizing tips:
- 1 to 5 units based on confidence
- Bet higher when confident
- Track your progress""")
update.message.reply_text("""Unit sizing tips:
- 1 to 5 units based on confidence
- Increase unit size every 35 units gained
- Stick to 2% of bankroll per unit""")

def rules(update, context):
    update.message.reply_text("""
Group Rules:
1. No spam or self-promo
2. Respect all members
3. Bet responsibly
4. Follow DPM leadership
""")

def socials(update, context):
    update.message.reply_text("""
Follow Digital Profit Mob:
Instagram: https://www.instagram.com/digitalprofitmob?igsh=MzB4OWRtYnp6YXo=
Twitter: https://x.com/reebtc_yv?s=21
Telegram: https://t.me/Freegamedpm
YouTube: https://youtube.com/@reemoneyvlogs?si=AvO_I6KcVsFgcslS
""")

def about(update, context):
    update.message.reply_text("""
Digital Profit Mob is a premium betting and finance community focused on disciplined, long-term profits through proven strategies and group support.
""")

def support(update, context):
    update.message.reply_text("Need help? Contact us on IG: https://www.instagram.com/digitalprofitmob/")
# Set up the bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(CommandHandler('picks', picks))
dispatcher.add_handler(CommandHandler('setpick', setpick))  # Admin-only
dispatcher.add_handler(CommandHandler('record', record))
dispatcher.add_handler(CommandHandler('setrecord', setrecord))  # Admin-only
dispatcher.add_handler(CommandHandler('vip', vip))
dispatcher.add_handler(CommandHandler('units', units))
dispatcher.add_handler(CommandHandler('rules', rules))
dispatcher.add_handler(CommandHandler('socials', socials))
dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(CommandHandler('support', support))

# Run the bot
updater.start_polling()
updater.idle()
