const TelegramBot = require('node-telegram-bot-api');
const fs = require('fs');
require('dotenv').config();

const bot = new TelegramBot(process.env.TELEGRAM_TOKEN, { polling: true });
const ADMIN_ID = '1975772726';
const DATA_FILE = './data.json';

// Helper to read data
function readData() {
  const data = fs.readFileSync(DATA_FILE);
  return JSON.parse(data);
}

// Helper to write data
function writeData(newData) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(newData, null, 2));
}

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
  const { picks } = readData();
  bot.sendMessage(msg.chat.id, picks);
});

bot.onText(/\/record/, (msg) => {
  const { record } = readData();
  bot.sendMessage(msg.chat.id, record);
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

// Admin-only updates
bot.onText(/\/setrecord (.+)/, (msg, match) => {
  if (msg.from.id.toString() === ADMIN_ID) {
    const data = readData();
    data.record = match[1];
    writeData(data);
    bot.sendMessage(msg.chat.id, "Record updated and saved.");
  } else {
    bot.sendMessage(msg.chat.id, "You are not authorized to use this command.");
  }
});

bot.onText(/\/setpicks (.+)/, (msg, match) => {
  if (msg.from.id.toString() === ADMIN_ID) {
    const data = readData();
    data.picks = match[1];
    writeData(data);
    bot.sendMessage(msg.chat.id, "Picks updated and saved.");
  } else {
    bot.sendMessage(msg.chat.id, "You are not authorized to use this command.");
  }
});
