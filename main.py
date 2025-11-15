import telebot, requests, os
from flask import Flask
from threading import Thread

app = Flask('')
TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "*Bot Grok AI Aktif!*\n\n/btc - Harga Bitcoin\n/waktu - Jam sekarang", parse_mode='Markdown')

@bot.message_handler(commands=['btc'])
def btc(m):
    try:
        h = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        bot.reply_to(m, f"Bitcoin: ${h['bitcoin']['usd']:,} USD")
    except:
        bot.reply_to(m, "Gagal ambil harga.")

@bot.message_handler(commands=['waktu'])
def waktu(m):
    from datetime import datetime
    bot.reply_to(m, f"Sekarang: {datetime.now().strftime('%d %B %Y, %H:%M WIB')}")

@app.route('/')
def home():
    return "Bot aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
bot.infinity_polling()
