import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ================= CONFIG =================
BOT_TOKEN = "7719596959:AAErR8ZQuT2Q_AKa_jaFLHyKMDJCudI0ukY"
ADMIN_USERNAME = "VRA1919"   # tanpa @
BROKER_LINK = "https://one.justmarkets.link/a/b7lp60euua"
BROKER_NAME = "Justmarkets"
MEMBER_TOTAL = 378

# ================= LOG =================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ================= MENU =================
main_menu = ReplyKeyboardMarkup(
    [
        ["👑 Admin"],
        ["🏦 Link Broker"],
        ["📊 Jumlah Member"]
    ],
    resize_keyboard=True
)

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Hari Yang menyenangkan, silahkan pilih 🔥",
        reply_markup=main_menu
    )

# ================= HANDLE BUTTON =================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # ADMIN BUTTON
    if text == "👑 Admin":
        await update.message.reply_text(
            f"Silakan hubungi admin resmi:\nhttps://t.me/{ADMIN_USERNAME}"
        )

    # LINK BROKER BUTTON
    elif text == "🏦 Link Broker":
        await update.message.reply_text(
            f"Berikut link pendaftaran resmi:\n{BROKER_LINK}\n\n"
            "Setelah daftar, kirim No akun anda pada admin agar rebate 80% bisa diaktifkan."
        )

    # MEMBER BUTTON
    elif text == "📊 Jumlah Member":
        await update.message.reply_text(
            f"Jumlah keseluruhan saat ini sudah ada {MEMBER_TOTAL} member aktif.\n"
            "Komunitas terus berkembang setiap minggu."
        )

    else:
        await update.message.reply_text(
            "Senang membantu anda, silahkan pilih menu yang tersedia."
        )

# ================= MAIN =================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
