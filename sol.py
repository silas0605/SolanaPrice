import requests
from telegram import Bot
from telegram.ext import Updater, CommandHandler
import time

# Your Telegram bot token
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'  # Could be user ID or group ID

bot = Bot(token=TELEGRAM_TOKEN)

def get_solana_price():
    # Example using Raydium API for SOL price
    url = "https://api.raydium.io/v2/main/price"
    response = requests.get(url).json()
    sol_price = None
    for token in response.get('data', []):
        if token['symbol'] == 'SOL':
            sol_price = token['price']
            break
    return sol_price

def send_price(update, context):
    price = get_solana_price()
    if price:
        message = f"Current Solana (SOL) price: ${price:.2f}"
    else:
        message = "Could not fetch Solana price at the moment."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("price", send_price))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
