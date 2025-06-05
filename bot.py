import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Admin Telegram user id
ADMIN_ID = 1056821860

# JSON file path (same folder mein rakho)
JSON_FILE = "subjects.json"

# Function to load subjects from JSON file
def load_subjects():
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Function to save subjects to JSON file
def save_subjects(data):
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

# 🚀 /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Notes Bot!\n\n"
        "Type a subject name to get the PDF notes.\n"
        "Use /list to see all subjects.\n"
        "Admins can add new notes using:\n"
        "/add subject_name link"
    )

# 📄 /list command to show all subjects
async def list_subjects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subjects = load_subjects()
    if subjects:
        subject_list = "\n".join([f"🔹 {subj.title()}" for subj in subjects.keys()])
        await update.message.reply_text(f"📚 Available subjects:\n\n{subject_list}")
    else:
        await update.message.reply_text("No subjects found yet.")

# 📩 Handle messages - send PDF link if subject found
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subject = update.message.text.lower().strip()
    subjects = load_subjects()

    if subject in subjects:
        await update.message.reply_text(
            f"📘 Here is your *{subject.title()}* Notes PDF:\n{subjects[subject]}",
            parse_mode='Markdown'
        )
    else:
        await update.message.reply_text(
            "❌ Sorry, notes not found for that subject.\nUse /list to see available subjects."
        )

# ➕ /add command - only admin can add subject+link
async def add_subject(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ You are not authorized to add subjects.")
        return

    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Usage: /add subject_name link")
        return

    subject_name = args[0].lower()
    link = " ".join(args[1:])  # rest is link

    subjects = load_subjects()
    subjects[subject_name] = link
    save_subjects(subjects)

    await update.message.reply_text(f"✅ Subject '{subject_name}' added/updated successfully!")

# 🧠 Main bot setup
if __name__ == '__main__':
    app = ApplicationBuilder().token("7973915378:AAEJX1T_bv3Z7B34PTwwYmPpXDI16ic59CI").build()  # ← अपना token डालो

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("list", list_subjects))
    app.add_handler(CommandHandler("add", add_subject))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot running... Press Ctrl+C to stop.")
    app.run_polling()
