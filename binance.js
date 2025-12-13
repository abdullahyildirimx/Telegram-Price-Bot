export const handleBinance = async (message, resultMessage, binancelist) => {
  const upperMessage = message.text.toUpperCase()

  if (binancelist.includes(upperMessage)) {
    const url =`https://api.binance.com/api/v3/ticker/24hr?symbol=${upperMessage}USDT`

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Request failed: ${res.status}`)
    const output = await res.json()

    const symbol = '$'
    const price = Number(output.lastPrice).toString()
    const change = `${Number(output.priceChangePercent).toFixed(2)}%`

    if (resultMessage !== '') {
      resultMessage += '\n'
    }

    resultMessage += `Binance -> ${upperMessage}: ${symbol}${price}  ${change}`
  }

  if (upperMessage === 'GAINERS' || upperMessage === 'LOSERS') {
    const url =`https://api.binance.com/api/v3/ticker/24hr`

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Request failed: ${res.status}`)
    const output = await res.json()

    const symbol = '$'
    const changePercentList = binancelist.map(coin => {
      const upperSymbol = coin + 'USDT'
      const entry = output.find(e => e.symbol === upperSymbol)
      return [coin, Number(entry.lastPrice), Number(entry.priceChangePercent)]
    })

    if (upperMessage === 'GAINERS') {
      changePercentList.sort((a, b) => b[2] - a[2])
      resultMessage += 'Binance Top Gainers:'
    } else {
      changePercentList.sort((a, b) => a[2] - b[2])
      resultMessage += 'Binance Top Losers:'
    }

    for (let i = 0; i < 5; i++) {
      const [coin, price, percent] = changePercentList[i]
      resultMessage += '\n'
      resultMessage += `${coin}: ${symbol}${price}  ${percent.toFixed(2)}%`
    }
  }

  return resultMessage
}