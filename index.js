const TelegramBot = require('node-telegram-bot-api');
require('dotenv').config();

const bot = new TelegramBot(process.env.TELEGRAM_TOKEN, { polling: true });

// Admin Telegram user ID
const ADMIN_ID = '1975772726';

// Default values
let recordText = 'No record has been set yet.';
let picksText = 'No picks available yet.';

// Public commands
bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, "Welcome to Digital Profit Mob!\nUse /help to see available commands.");
});

bot.onText(/\/help/, (msg) => {
  bot.sendMessage(msg.chat.id, `
/start - Welcome message & how to use the bot
/picks - Get today's free sports betting picks
/record - View the recent win/loss record
/vip - Info on how to join the VIP group
/units - Learn about unit sizing & bankroll tips
/rules - Group rules & betting guidelines
/help - Full list of available commands
/socials - Links to all DPM social media platforms
/about - Info about Digital Profit Mob
/support - Contact for help or issues
`);
});

bot.onText(/\/picks/, (msg) => {
  bot.sendMessage(msg.chat.id, picksText);
});

bot.onText(/\/record/, (msg) => {
  bot.sendMessage(msg.chat.id, recordText);
});

bot.onText(/\/vip/, (msg) => {
  bot.sendMessage(msg.chat.id, "To join VIP, visit: http://link.me/reemoney");
});

bot.onText(/\/units/, (msg) => {
  bot.sendMessage(msg.chat.id, "We use a 1-5u system. 1 unit = 2% of bankroll. Increase unit size every 35 units won.");
});

bot.onText(/\/rules/, (msg) => {
  bot.sendMessage(msg.chat.id, "Rules: Respect everyone. No spam. No hate speech. Bet responsibly.");
});

bot.onText(/\/about/, (msg) => {
  bot.sendMessage(msg.chat.id, "Digital Profit Mob is your plug for consistent, disciplined sports picks & bankroll growth.");
});

bot.onText(/\/socials/, (msg) => {
  bot.sendMessage(msg.chat.id, "Follow us: http://link.me/reemoney");
});

bot.onText(/\/support/, (msg) => {
  bot.sendMessage(msg.chat.id, "Need help? DM the admin at http://link.me/reemoney");
});

// Admin-only commands
bot.onText(/\/setrecord (.+)/, (msg, match) => {
  if (msg.from.id.toString() === ADMIN_ID) {
    recordText = match[1];
    bot.sendMessage(msg.chat.id, "Record updated.");
  } else {
    bot.sendMessage(msg.chat.id, "You are not authorized to use this command.");
  }
});

bot.onText(/\/setpicks (.+)/, (msg, match) => {
  if (msg.from.id.toString() === ADMIN_ID) {
    picksText = match[1];
    bot.sendMessage(msg.chat.id, "Picks updated.");
  } else {
    bot.sendMessage(msg.chat.id, "You are not authorized to use this command.");
  }
});
