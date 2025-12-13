export const handleBinanceTr = async (message, resultMessage, binancetrlist) => {
  const upperMessage = message.text.toUpperCase()

  if (binancetrlist.includes(upperMessage)) {
    const url =`https://api.binance.com/api/v3/ticker/24hr?symbol=${upperMessage}TRY`

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Request failed: ${res.status}`)
    const output = await res.json()

    const symbol = '₺'
    const price = Number(output.lastPrice).toString()
    const change = `${Number(output.priceChangePercent).toFixed(2)}%`

    if (resultMessage !== '') {
      resultMessage += '\n'
    }

    resultMessage += `BinanceTR -> ${upperMessage}: ${symbol}${price}  ${change}`
  }

  return resultMessage
}