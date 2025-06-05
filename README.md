# 📚 Telegram Notes Bot

A simple Telegram bot that sends subject-wise PDF notes to users based on their input. Works instantly — just type the subject name!

## 🚀 Features
- 📂 Subject-wise PDF sharing
- 🧠 Topics Supported: `SQL`, `Python`, `Hacker Book`, `OWASP`
- 🔒 Admin panel support (coming soon)

## 💻 How to Use

1. Start the bot on Telegram using `/start`
2. Type any of the supported subjects:
   - `sql`
   - `python`
   - `hacker book`
   - `owasp`
3. The bot will reply with a downloadable PDF link.

## 🛠️ Setup Instructions

To run this bot locally:

```bash
# Step 1: Clone this repo
git clone https://github.com/akashsinghrajput-18/telegram-notes-bot.git
cd telegram-notes-bot

# Step 2: Install dependencies
pip install python-telegram-bot --upgrade

# Step 3: Add your Telegram Bot Token in bot.py
# Step 4: Run the bot
python bot.py
