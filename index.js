require('dotenv').config();
const TelegramBot = require('node-telegram-bot-api');

const bot = new TelegramBot(process.env.TELEGRAM_TOKEN, { polling: true });

const ADMIN_ID = 1975772726; // Your Telegram ID

let picks = "No picks posted yet.";
let record = "0-0";

// Commands
bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, "Welcome to Digital Profit Mob! Use /help to see all commands.");
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
  bot.sendMessage(msg.chat.id, picks);
});

bot.onText(/\/record/, (msg) => {
  bot.sendMessage(msg.chat.id, record);
});

bot.onText(/\/vip/, (msg) => {
  bot.sendMessage(msg.chat.id, "Join the VIP group at: http://link.me/reemoney");
});

bot.onText(/\/units/, (msg) => {
  bot.sendMessage(msg.chat.id, "We use a 1-5u system. 1u = 2% of bankroll. Adjust every 35u profit.");
});

bot.onText(/\/rules/, (msg) => {
  bot.sendMessage(msg.chat.id, "No spam. Respect all members. Bet responsibly.");
});

bot.onText(/\/socials/, (msg) => {
  bot.sendMessage(msg.chat.id, "Follow us: http://link.me/reemoney");
});

bot.onText(/\/about/, (msg) => {
  bot.sendMessage(msg.chat.id, "Digital Profit Mob brings you consistent, data-backed sports betting picks.");
});

bot.onText(/\/support/, (msg) => {
  bot.sendMessage(msg.chat.id, "Need help? DM @yourusername on Telegram.");
});

// Admin-only updates
bot.onText(/\/updatepicks (.+)/, (msg, match) => {
  if (msg.from.id === ADMIN_ID) {
    picks = match[1];
    bot.sendMessage(msg.chat.id, "Picks updated!");
  } else {
    bot.sendMessage(msg.chat.id, "You are not authorized.");
  }
});

bot.onText(/\/updaterecord (.+)/, (msg, match) => {
  if (msg.from.id === ADMIN_ID) {
    record = match[1];
    bot.sendMessage(msg.chat.id, "Record updated!");
  } else {
    bot.sendMessage(msg.chat.id, "You are not authorized.");
  }
});
