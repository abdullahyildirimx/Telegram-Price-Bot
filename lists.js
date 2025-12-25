export const currencylist = {
  dollarlist: ['DOLAR', 'DOLLAR', 'USD'],
  goldlist: ['ALTIN', 'ALTİN', 'GOLD', 'XAU'],
  silverlist: ['GÜMÜŞ', 'GUMUS', 'SILVER', 'XAG']
}
export let binancelist = []
export let binancetrlist = []

const digitsFromTickSize = (tickSize) => {
  const [, decimals = ''] = tickSize.split('.')
  return decimals.replace(/0+$/, '').length
}

const fetchJson = async (url) => {
  const res = await fetch(url)
  if (!res.ok) throw new Error('Network response was not ok')
  return res.json()
}

const refreshLists = async () => {
  try {
    const binanceData = await fetchJson(
      'https://api.binance.com/api/v3/exchangeInfo'
    )

    binancelist = binanceData.symbols
      .filter(s => s.symbol.endsWith('USDT') && s.status === 'TRADING')
      .map(s => {
        const tickSize = s.filters[0].tickSize ?? '1'
        const digits = digitsFromTickSize(tickSize)

        return {
          name: s.baseAsset,
          digits
        }
      })
      .sort((a, b) => a.name.localeCompare(b.name))

    const binanceTrData = await fetchJson(
      'https://www.binance.tr/open/v1/common/symbols'
    )

    binancetrlist = binanceTrData.data.list
      .filter(s => s.symbol.endsWith('TRY'))
      .map(s => {
        const tickSize = s.filters[0].tickSize ?? '1'
        const digits = digitsFromTickSize(tickSize)

        return {
          name: s.baseAsset,
          digits
        }
      })
      .sort((a, b) => a.name.localeCompare(b.name))
  } catch (e) {
    console.error('Fetch list error:', e)
  }
}

await refreshLists()

setInterval(refreshLists, 60000)