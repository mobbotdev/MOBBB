const express = require("express");
const axios = require("axios");
const app = express();
app.use(express.json());

const TELEGRAM_TOKEN = "8028698920:AAFn6NqP2O5mNCypQGp8TqYgaKaNqtEDeXY";
const TELEGRAM_API = `https://api.telegram.org/bot${TELEGRAM_TOKEN}`;
const ADMIN_ID = "1975772726";

let picks = "No picks have been posted yet.";
let record = "Record not updated yet.";

// Helper: send message
async function sendMessage(chatId, text) {
  await axios.post(`${TELEGRAM_API}/sendMessage`, {
    chat_id: chatId,
    text: text,
    parse_mode: "Markdown"
  });
}

// Handle Telegram commands
app.post(`/webhook`, async (req, res) => {
  const msg = req.body.message;
  if (!msg || !msg.text) return res.sendStatus(200);

  const chatId = msg.chat.id.toString();
  const userId = msg.from.id.toString();
  const text = msg.text.trim();

  const command = text.split(" ")[0].toLowerCase();
  const args = text.split(" ").slice(1).join(" ");

  switch (command) {
    case "/start":
      return sendMessage(chatId, `Welcome to *Digital Profit Mob*!
      
Use /help to see everything I can do for you.`);
    case "/help":
      return sendMessage(chatId, `*Available Commands:*
/start - Welcome message
/picks - Get today's free sports betting picks
/record - View the recent win/loss record
/vip - Info on how to join the VIP group
/units - Learn about unit sizing & bankroll tips
/rules - Group rules & betting guidelines
/help - Full command list
/socials - All DPM social media links
/about - Info about Digital Profit Mob
/support - Get help or contact support`);
    case "/picks":
      return sendMessage(chatId, `*Today's Picks:*\n${picks}`);
    case "/record":
      return sendMessage(chatId, `*Recent Record:*\n${record}`);
    case "/vip":
      return sendMessage(chatId, `To join VIP, visit:\nhttp://link.me/reemoney`);
    case "/units":
      return sendMessage(chatId, `*Unit Sizing Info:*
We use a 1-5u scale. 1 unit = 2% of your bankroll.
We raise unit size every 35 units gained.`);
    case "/rules":
      return sendMessage(chatId, `*Group Rules:*
1. No hate, spam, or drama.
2. Bet responsibly.
3. Respect VIP content confidentiality.`);
    case "/about":
      return sendMessage(chatId, `*About DPM:*
Digital Profit Mob helps you profit consistently through disciplined, data-backed sports betting.`);
    case "/socials":
      return sendMessage(chatId, `Follow us here:
http://link.me/reemoney`);
    case "/support":
      return sendMessage(chatId, `For support, message @reemoney or use /vip to join.`);
    
    // Admin-only updates
    case "/updatepicks":
      if (userId !== ADMIN_ID) return sendMessage(chatId, "Unauthorized.");
      picks = args || "No picks posted.";
      return sendMessage(chatId, "Free picks updated.");
    case "/updaterecord":
      if (userId !== ADMIN_ID) return sendMessage(chatId, "Unauthorized.");
      record = args || "No record info provided.";
      return sendMessage(chatId, "Record updated.");
    default:
      return sendMessage(chatId, "Unknown command. Use /help for options.");
  }
});
  
// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Bot running on port ${PORT}`);
});
