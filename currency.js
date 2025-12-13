export const handleCurrency = async (message, resultMessage, currencylist) => {
  const upperMessage = message.text.toUpperCase()

  if (currencylist.includes(upperMessage)) {
    const url = 'https://www.bloomberght.com/chart/ekonomi/doviz/detay/dolar'

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Request failed: ${res.status}`)
    const output = await res.json()

    const symbol = '₺'
    const price = Number(String(output.body.foreignCurrencyDetail.items.lastPrice).replace(',', '.')).toFixed(4)
    const change = `${Number(String(output.body.foreignCurrencyDetail.items.percentChange).replace(',', '.')).toFixed(2)}%`

    if (resultMessage !== '') {
      resultMessage += '\n'
    }

    resultMessage += `Dolar: ${symbol}${price}  ${change}`
  }

  return resultMessage
}