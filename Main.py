import os
import requests
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("8643787951:AAFuouo5dbPQF93lw5uji1x4rPGvCCEY9NA")
GEMINI_KEY = os.getenv("AIzaSyCUmqTvylO99v9d5Qj7QsRuBL4uBX_Ww94")

def handle_message(update: Update, context: CallbackContext):
    question = update.message.text

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"

    data = {
        "contents": [{
            "parts": [{
                "text": f"You are Finfinnee AI Bot. Answer clearly.\nUser: {question}"
            }]
        }]
    }

    try:
        res = requests.post(url, json=data)
        reply = res.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        reply = "Sorry, I couldn't respond right now."

    update.message.reply_text(reply)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if name == "main":
    main()
