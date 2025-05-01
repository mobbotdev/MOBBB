from telegram.ext import Updater, CommandHandler

# Replace with your actual bot token
TOKEN = "8028698920:AAFn6NqP2O5mNCypQGp8TqYgaKaNqtEDeXY"

def start(update, context):
    update.message.reply_text("Wassup Family, I’m Mob Bot. Let’s Profit Today! 💰")

def picks(update, context):
    update.message.reply_text("Today's free sports betting picks:\n[Replace with today’s picks]")

def record(update, context):
    update.message.reply_text("Recent win/loss record:\n[Replace with your record here]")

def vip(update, context):
    update.message.reply_text("To join the VIP group, visit: http://patreon.com/ReeskiDPM")

def units(update, context):
    update.message.reply_text("""Unit sizing tips:
- 1 to 5 units based on confidence
- Increase unit size every 35 units gained
- Stick to 2% of bankroll per unit""")

def rules(update, context):
    update.message.reply_text("""Group rules & betting guidelines:
- Respect all members
- No spam or self-promotion
- Bet responsibly and follow the unit system""")

def help_command(update, context):
    update.message.reply_text("""Available commands:
/picks - Get today's free sports betting picks
/record - View recent win/loss record
/vip - Info on how to join VIP group
/units - Learn about unit sizing and bankroll tips
/rules - Group rules & betting guidelines
/socials - Links to all DPM social media
/about - Info about Digital Profit Mob
/support - Contact for help or issues""")

def socials(update, context):
    update.message.reply_text("""DPM Social Media Links:
Instagram: https://www.instagram.com/digitalprofitmob?igsh=MzB4OWRtYnp6YXo=
Twitter: https://x.com/reebtc_yv?s=21
Telegram: https://t.me/Freegamedpm
YouTube: https://youtube.com/@reemoneyvlogs?si=AvO_I6KcVsFgcslS""")

def about(update, context):
    update.message.reply_text("""About Digital Profit Mob:
We are a digital community focused on sports betting education, tips, and daily profit strategies. Join the Mob and let’s elevate together.""")

def support(update, context):
    update.message.reply_text("Need help? Contact us on IG: https://www.instagram.com/digitalprofitmob/")

# Set up the bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('picks', picks))
dispatcher.add_handler(CommandHandler('record', record))
dispatcher.add_handler(CommandHandler('vip', vip))
dispatcher.add_handler(CommandHandler('units', units))
dispatcher.add_handler(CommandHandler('rules', rules))
dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(CommandHandler('socials', socials))
dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(CommandHandler('support', support))

# Start the bot
updater.start_polling()
updater.idle()
