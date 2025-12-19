export const handleBinanceTr = async (message, resultMessage, binancetrlist) => {
  const upperMessage = message.text.toUpperCase()
  const coin = binancetrlist.find(item => item.name === upperMessage)
  if (coin) {
    const { name, digits } = coin
    const url =`https://api.binance.com/api/v3/ticker/24hr?symbol=${name}TRY`

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Fetch price from BinanceTR error`)
    const output = await res.json()

    const symbol = '₺'
    const price = Number(output.lastPrice).toFixed(digits)
    const change = `${Number(output.priceChangePercent).toFixed(2)}%`

    if (resultMessage !== '') {
      resultMessage += '\n'
    }

    resultMessage += `BinanceTR -> ${name}: ${symbol}${price}  ${change}`
  }

  return resultMessage
}