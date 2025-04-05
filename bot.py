from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

PING_TARGETS = {
    -100000000000: ["@user1", "@user2"]
}

async def ping_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chat_id = update.effective_chat.id

    if "@all" in text:
        if chat_id in PING_TARGETS:
            mentions = " ".join(PING_TARGETS[chat_id])
            await update.message.reply_text(f"Пингую: {mentions}")
        else:
            await update.message.reply_text("Я не знаю, кого пинговать в этой группе.")

app = ApplicationBuilder().token("7940687639:AAEBKOws2l1gC59np2jGNpw_1FqZW8UilAY").build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ping_all))
app.run_polling()
