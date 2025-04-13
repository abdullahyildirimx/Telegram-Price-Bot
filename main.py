import telebot
import os, sys
from requests.exceptions import ConnectionError, ReadTimeout

from keys import telegramkey
from binance import handleBinance
from currency import handleCurrency
from gas import handleGas
from mexc import handleMexc
from paribu import handleParibu

bot = telebot.TeleBot(telegramkey)

@bot.message_handler(content_types=['text'])
def handleMessage(message):

    resultMessage = ""
    chat_id = message.chat.id
    handlers = [handleBinance, handleCurrency, handleGas, handleMexc, handleParibu]
    for handler in handlers:
        try:
            resultMessage = handler(message, resultMessage)
        except Exception as e:
            print(f"Error in {handler.__name__}: {e}")
            continue

    if message.text.startswith('/start'):
        resultMessage = "Write a coin or currency name without typing '/'."
    elif message.text.startswith('/'):
        resultMessage = "Try without typing '/'."
        
    if resultMessage != "":
        bot.send_message(chat_id, resultMessage)


try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError, ReadTimeout) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
