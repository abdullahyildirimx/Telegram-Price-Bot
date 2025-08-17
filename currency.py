import requests

def handleCurrency(message, resultMessage, currencylist):
    if message.text.upper() in currencylist:
        url = "https://www.bloomberght.com/chart/ekonomi/doviz/detay/dolar"
        response = requests.get(url)
        output = response.json()
        price = float(str(output["body"]["foreignCurrencyDetail"]["items"]["lastPrice"]).replace(",", "."))
        change = float(str(output["body"]["foreignCurrencyDetail"]["items"]["percentChange"]).replace(",", "."))
        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += f'Dolar: ₺{price:.4f}  {change:.2f}%'
    return resultMessage
