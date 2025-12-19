export const handleBinance = async (message, resultMessage, binancelist) => {
  const upperMessage = message.text.toUpperCase()
  const coin = binancelist.find(item => item.name === upperMessage)
  if (coin) {
    const { name, digits } = coin
    const url =`https://api.binance.com/api/v3/ticker/24hr?symbol=${name}USDT`

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Fetch price from Binance error`)
    const output = await res.json()

    const symbol = '$'
    const price = Number(output.lastPrice).toFixed(digits)
    const change = `${Number(output.priceChangePercent).toFixed(2)}%`

    if (resultMessage !== '') {
      resultMessage += '\n'
    }

    resultMessage += `Binance -> ${name}: ${symbol}${price}  ${change}`
  }

  if (upperMessage === 'GAINERS' || upperMessage === 'LOSERS') {
    const url =`https://api.binance.com/api/v3/ticker/24hr`

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Fetch price from Binance error`)
    const output = await res.json()

    const symbol = '$'
    const changePercentList = binancelist.map(coin => {
      const upperSymbol = coin.name + 'USDT'
      const entry = output.find(e => e.symbol === upperSymbol)
      return [coin.name, Number(entry.lastPrice).toFixed(coin.digits), Number(entry.priceChangePercent)]
    })

    if (upperMessage === 'GAINERS') {
      changePercentList.sort((a, b) => b[2] - a[2])
      resultMessage += 'Binance Top Gainers:'
    } else {
      changePercentList.sort((a, b) => a[2] - b[2])
      resultMessage += 'Binance Top Losers:'
    }

    for (let i = 0; i < 5; i++) {
      const [name, price, percent] = changePercentList[i]
      resultMessage += '\n'
      resultMessage += `${name}: ${symbol}${price}  ${percent.toFixed(2)}%`
    }
  }

  return resultMessage
}