import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Your bot token
TOKEN = "8028698920:AAFn6NqP2O5mNCypQGp8TqYgaKaNqtEDeXY"

# Define the /start command
def start(update: Update, context: CallbackContext) -> None:
    welcome_message = """
    Wassup family, let's profit today 💰
    
    Here’s how to use the bot:

    - /picks - Get today's free sports betting picks
    - /record - View the recent win/loss record
    - /vip - Info on how to join the VIP group
    - /units - Learn about unit sizing & bankroll tips
    - /rules - Group rules & betting guidelines
    - /help - Full list of available commands
    - /socials - Links to all DPM social media platforms
    - /about - Info about Digital Profit Mob
    - /support - Contact for help or issues

    Type any of these commands to get started!

    Follow us on social media:
    - Telegram: [https://t.me/Freegamedpm](https://t.me/Freegamedpm)
    - Twitter: [https://x.com/reebtc_yv?s=21](https://x.com/reebtc_yv?s=21)
    - Patreon: [http://patreon.com/ReeskiDPM](http://patreon.com/ReeskiDPM)
    - YouTube: [https://youtube.com/@reemoneyvlogs?si=Ptq884AOwIlHDxeS](https://youtube.com/@reemoneyvlogs?si=Ptq884AOwIlHDxeS)
    """
    update.message.reply_text(welcome_message)

# Define the /picks command
def picks(update: Update, context: CallbackContext) -> None:
    free_picks = """
    Today's Free Sports Betting Picks:
    
    1. Pick 1: Team A vs Team B - Bet on Team A to win.
    2. Pick 2: Team C vs Team D - Bet on Team D to win.
    
    Always remember, bet responsibly!
    """
    update.message.reply_text(free_picks)

# Define the /record command
def record(update: Update, context: CallbackContext) -> None:
    win_loss_record = """
    Recent Free Picks Record:
    
    - Pick 1: Win
    - Pick 2: Loss
    - Pick 3: Win
    - Pick 4: Win
    
    Overall Record: 3-1
    """
    update.message.reply_text(win_loss_record)

# Define the /vip command
def vip(update: Update, context: CallbackContext) -> None:
    vip_info = """
    Want to join the VIP group? Here's how:
    
    - Direct message @ReeskiDPM to get VIP access.
    - Exclusive picks, tips, and strategies to maximize your profits!
    """
    update.message.reply_text(vip_info)

# Define the /units command
def units(update: Update, context: CallbackContext) -> None:
    units_info = """
    Unit Sizing & Bankroll Tips:
    
    - Unit size: 2% of your bankroll per bet.
    - Increase your unit size every 35 units won.
    
    Manage your bankroll wisely to ensure long-term profits.
    """
    update.message.reply_text(units_info)

# Define the /rules command
def rules(update: Update, context: CallbackContext) -> None:
    betting_rules = """
    Group Rules & Betting Guidelines:
    
    1. Bet responsibly – don’t risk money you can’t afford to lose.
    2. Follow the picks but use your discretion when betting.
    3. No spamming or promoting other services.
    
    Stick to the rules, and let's make money together!
    """
    update.message.reply_text(betting_rules)

# Define the /help command
def help(update: Update, context: CallbackContext) -> None:
    help_message = """
    Available Commands:

    - /start - Welcome message & how to use the bot
    - /picks - Get today's free sports betting picks
    - /record - View the recent win/loss record
    - /vip - Info on how to join the VIP group
    - /units - Learn about unit sizing & bankroll tips
    - /rules - Group rules & betting guidelines
    - /help - Full list of available commands
    - /socials - Links to all DPM social media platforms
    - /about - Info about Digital Profit Mob
    - /support - Contact for help or issues
    """
    update.message.reply_text(help_message)

# Define the /socials command
def socials(update: Update, context: CallbackContext) -> None:


No, the code I provided is not set up for webhooks. I apologize for the confusion. Here’s the corrected version with webhook integration for your sports betting bot. It will allow you to update via Telegram and properly handle webhooks:

### Updated `main.py` with Webhooks and Command Handlers:

```python
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import Dispatcher, CallbackQueryHandler
import os
from flask import Flask, request
from telegram import Bot

# Set up Flask server for webhook
app = Flask(__name__)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Your bot token and URL
TOKEN = "8028698920:AAFn6NqP2O5mNCypQGp8TqYgaKaNqtEDeXY"
WEBHOOK_URL = "https://mobbb-g2m3.onrender.com"
bot = Bot(token=TOKEN)

# Command Handlers
def start(update: Update, context: CallbackContext) -> None:
    welcome_message = """
    Wassup family, let's profit today 💰

    Here’s how to use the bot:

    - /picks - Get today's free sports betting picks
    - /record - View the recent win/loss record
    - /vip - Info on how to join the VIP group
    - /units - Learn about unit sizing & bankroll tips
    - /rules - Group rules & betting guidelines
    - /help - Full list of available commands
    - /socials - Links to all DPM social media platforms
    - /about - Info about Digital Profit Mob
    - /support - Contact for help or issues

    Type any of these commands to get started!

    Follow us on social media:
    - Telegram: [https://t.me/Freegamedpm](https://t.me/Freegamedpm)
    - Twitter: [https://x.com/reebtc_yv?s=21](https://x.com/reebtc_yv?s=21)
    - Patreon: [http://patreon.com/ReeskiDPM](http://patreon.com/ReeskiDPM)
    - YouTube: [https://youtube.com/@reemoneyvlogs?si=Ptq884AOwIlHDxeS](https://youtube.com/@reemoneyvlogs?si=Ptq884AOwIlHDxeS)
    """
    update.message.reply_text(welcome_message)

def picks(update: Update, context: CallbackContext) -> None:
    free_picks = """
    Today's Free Sports Betting Picks:

    1. Pick 1: Team A vs Team B - Bet on Team A to win.
    2. Pick 2: Team C vs Team D - Bet on Team D to win.

    Always remember, bet responsibly!
    """
    update.message.reply_text(free_picks)

def record(update: Update, context: CallbackContext) -> None:
    win_loss_record = """
    Recent Free Picks Record:

    - Pick 1: Win
    - Pick 2: Loss
    - Pick 3: Win
    - Pick 4: Win

    Overall Record: 3-1
    """
    update.message.reply_text(win_loss_record)

def vip(update: Update, context: CallbackContext) -> None:
    vip_info = """
    Want to join the VIP group? Here's how:

    - Direct message @ReeskiDPM to get VIP access.
    - Exclusive picks, tips, and strategies to maximize your profits!
    """
    update.message.reply_text(vip_info)

def units(update: Update, context: CallbackContext) -> None:
    units_info = """
    Unit Sizing & Bankroll Tips:

    - Unit size: 2% of your bankroll per bet.
    - Increase your unit size every 35 units won.

    Manage your bankroll wisely to ensure long-term profits.
    """
    update.message.reply_text(units_info)

def rules(update: Update, context: CallbackContext) -> None:
    betting_rules = """
    Group Rules & Betting Guidelines:

    1. Bet responsibly – don’t risk money you can’t afford to lose.
    2. Follow the picks but use your discretion when betting.
    3. No spamming or promoting other services.

    Stick to the rules, and let's make money together!
    """
    update.message.reply_text(betting_rules)

def help(update: Update, context: CallbackContext) -> None:
    help_message = """
    Available Commands:

    - /start - Welcome message & how to use the bot
    - /picks - Get today's free sports betting picks
    - /record - View the recent win/loss record
    - /vip - Info on how to join the VIP group
    - /units - Learn about unit sizing & bankroll tips
    - /rules - Group rules & betting guidelines
    - /help - Full list of available commands
    - /socials - Links to all DPM social media platforms
    - /about - Info about Digital Profit Mob
    - /support - Contact for help or issues
    """
    update.message.reply_text(help_message)

def socials(update: Update, context: CallbackContext) -> None:
    socials_message = """
    Follow us on social media:

    - Telegram: [https://t.me/Freegamedpm](https://t.me/Freegamedpm)
    - Twitter: [https://x.com/reebtc_yv?s=21](https://x.com/reebtc_yv?s=21)
    - Patreon: [http://patreon.com/ReeskiDPM](http://patreon.com/ReeskiDPM)
    - YouTube: [https://youtube.com/@reemoneyvlogs?si=Ptq884AOwIlHDxeS](https://youtube.com/@reemoneyvlogs?si=Ptq884AOwIlHDxeS)
    """
    update.message.reply_text(socials_message)

# Setup webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        json_str = request.get_data().decode('UTF-8')
        update = Update.de_json(json_str, bot)
        dispatcher.process_update(update)
        return 'ok'

# Set webhook for the bot
def set_webhook():
    bot.set_webhook(url=WEBHOOK_URL + "/webhook")

# Initialize dispatcher and handlers
def main():
    set_webhook()
    
    # Create the dispatcher for the bot
    dispatcher = Dispatcher(bot, update_queue=None)
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("picks", picks))
    dispatcher.add_handler(CommandHandler("record", record))
    dispatcher.add_handler(CommandHandler("vip", vip))
    dispatcher.add_handler(CommandHandler("units", units))
    dispatcher.add_handler(CommandHandler("rules", rules))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("socials", socials))

# Start Flask server
if __name__ == '__main__':
    main()
    app.run(port=int(os.environ.get('PORT', 5000)))
