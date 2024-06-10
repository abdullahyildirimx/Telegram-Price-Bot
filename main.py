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

    try:
        resultMessage = handleBinance(message, resultMessage)
        resultMessage = handleCurrency(message, resultMessage)
        resultMessage = handleGas(message, resultMessage)
        resultMessage = handleMexc(message, resultMessage)
        resultMessage = handleParibu(message, resultMessage)
    except:
        resultMessage = "Not available."
    
    if message.text.startswith('/'):
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
