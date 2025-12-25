export const handleCurrency = async (message, resultMessage, currencylist) => {
  const upperMessage = message.text.toUpperCase()

  if (currencylist.dollarlist.includes(upperMessage)) {
    const url = 'https://www.bloomberght.com/chart/ekonomi/doviz/detay/dolar'

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Fetch currency price error`)
    const output = await res.json()

    const symbol = '₺'
    const price = Number(String(output.body.foreignCurrencyDetail.items.lastPrice).replace(',', '.')).toFixed(4)
    const change = `${Number(String(output.body.foreignCurrencyDetail.items.percentChange).replace(',', '.')).toFixed(2)}%`

    if (resultMessage !== '') {
      resultMessage += '\n'
    }

    resultMessage += `Dolar: ${symbol}${price}  ${change}`
  }

  if (currencylist.goldlist.includes(upperMessage)) {
    const url = 'https://www.bloomberght.com/chart/ekonomi/altin/detay/altin-ons'

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Fetch commodity price error`)
    const output = await res.json()

    const symbol = '$'
    const price = Number(String(output.body.goldDetail.items.lastPrice).replace('.', '').replace(',', '.')).toFixed(2)
    const change = `${Number(String(output.body.goldDetail.items.percentChange).replace(',', '.')).toFixed(2)}%`

    if (resultMessage !== '') {
      resultMessage += '\n'
    }

    resultMessage += `Ons Altın: ${symbol}${price}  ${change}`
  }

  if (currencylist.silverlist.includes(upperMessage)) {
    const url = 'https://www.bloomberght.com/chart/ekonomi/borsa/piyasa/emtia/detay/gumus-ons'

    const res = await fetch(url)
    if (!res.ok) throw new Error(`Fetch commodity price error`)
    const output = await res.json()

    const symbol = '$'
    const price = Number(String(output.body.stockMarketDetail.items.lastPrice).replace(',', '.')).toFixed(2)
    const change = `${Number(String(output.body.stockMarketDetail.items.percentChange).replace(',', '.')).toFixed(2)}%`

    if (resultMessage !== '') {
      resultMessage += '\n'
    }

    resultMessage += `Ons Gümüş: ${symbol}${price}  ${change}`
  }

  return resultMessage
}