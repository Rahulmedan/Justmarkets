from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import json
import os

TOKEN = "8547005273:AAHb5dSV9MGZWwnBwV61uwmBrtZ5m4dZIUk"
DATA_FILE = "users.json"

# ====== SIMPAN USER ======
def save_user(user_id):
    users = set()

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            users = set(json.load(f))

    users.add(user_id)

    with open(DATA_FILE, "w") as f:
        json.dump(list(users), f)

    return len(users)

# ====== START ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    total_users = save_user(user_id)

    keyboard = [
        ["👑 Admin", "🏦 Link Broker"],
        ["📊 Jumlah Member"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🔥 HAPPY NICE DAY, 🔥",
        reply_markup=reply_markup
    )

# ====== HANDLE MESSAGE ======
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "Admin" in text:
        await update.message.reply_text("👑 Hubungi Admin: @VRA1919")

    elif "Link Broker" in text:
        await update.message.reply_text("🏦 Daftar broker di sini:\nhttps://clickto.trade/bPaMS652XrZ?ib=28166308")

    elif "Jumlah Member" in text:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                users = json.load(f)
            total = len(users)
        else:
            total = 189

        await update.message.reply_text(
            f"📊 Jumlah keseluruhan saat ini sudah ada {187} member aktif.\nKomunitas terus berkembang setiap minggu 🚀"
        )

    else:
        await update.message.reply_text("Silakan pilih menu yang tersedia.")

# ====== MAIN ======
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot aktif...")
app.run_polling()
