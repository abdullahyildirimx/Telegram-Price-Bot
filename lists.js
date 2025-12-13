export const currencylist = ['DOLAR', 'USD']
export let binancelist = []
export let binancetrlist = []

const fetchJson = async (url) => {
  const res = await fetch(url)
  if (!res.ok) throw new Error(`Request failed: ${res.status}`)
  return res.json()
}

const refreshLists = async () => {
  const binanceData = await fetchJson(
    'https://api.binance.com/api/v3/exchangeInfo'
  )

  binancelist = binanceData.symbols
    .filter(s => s.symbol.endsWith('USDT') && s.status === 'TRADING')
    .map(s => s.baseAsset)
    .sort()

  const binanceTrData = await fetchJson(
    'https://www.binance.tr/open/v1/common/symbols'
  )

  binancetrlist = binanceTrData.data.list
    .filter(s => s.symbol.endsWith('TRY'))
    .map(s => s.baseAsset)
    .sort()
}

await refreshLists()

setInterval(refreshLists, 60000)