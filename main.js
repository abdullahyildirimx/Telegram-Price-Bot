import { BOT_TOKEN } from './keys.js'
import { handleBinance } from './binance.js'
import { handleBinanceTr } from './binancetr.js'
import { handleCurrency } from './currency.js'
import { binancelist, binancetrlist, currencylist } from './lists.js'

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms))

export const telegram = async (method, payload = {}) => {
  const res = await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/${method}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
  const output = await res.json()
  return output
}

export const sendMessage = async (chatId, text) => {
  return telegram('sendMessage', {
    chat_id: chatId,
    text
  })
}

let offset = 0

export const poll = async () => {
  try {
    const data = await telegram('getUpdates', {
      timeout: 10,
      offset
    })

    for (const update of data.result) {
      offset = update.update_id + 1

      if (!update.message || !update.message.text) continue

      const message = update.message
      const chatId = message.chat.id
      let resultMessage = ''

      const handlers = [
        [handleBinance, binancelist],
        [handleBinanceTr, binancetrlist],
        [handleCurrency, currencylist],
      ]

      for (const [handler, coinlist] of handlers) {
        try {
          resultMessage = await handler(message, resultMessage, coinlist)
        } catch (e) {
          console.error(`Error in ${handler.name}:`, e.message)
        }
      }

      if (message.text.startsWith('/start')) {
        resultMessage = "Write a coin or currency name without typing '/'."
      } else if (message.text.startsWith('/')) {
        resultMessage = "Try without typing '/'."
      }

      if (resultMessage) {
        await sendMessage(chatId, resultMessage)
      }
    }
  } catch (e) {
    console.error('Telegram API error:', e)
    await sleep(2000)
  }
}

export const loop = async () => {
  while (true) {
    await poll()
  }
}

loop()