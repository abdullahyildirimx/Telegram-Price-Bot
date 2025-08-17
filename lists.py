import requests

currencylist = ['DOLAR', 'USD']
gaslist = ['GAS']
mexclist = ['CEEK', 'RACA']

url = "https://api.binance.com/api/v3/exchangeInfo"
response = requests.get(url)
data = response.json()
binancelist = [s["baseAsset"] for s in data["symbols"] if s["symbol"].endswith("USDT") and s["status"] == "TRADING"]
binancelist = sorted(binancelist)

url = "https://www.binance.tr/open/v1/common/symbols"
response = requests.get(url)
data = response.json()
binancetrlist = [s["baseAsset"] for s in data["data"]["list"] if s["symbol"].endswith("TRY")]
binancetrlist = sorted(binancetrlist)