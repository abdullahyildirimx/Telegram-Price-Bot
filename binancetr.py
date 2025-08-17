import requests

def handleBinanceTr(message, resultMessage, binancetrlist):
    upperMessage = message.text.upper()

    if (upperMessage in binancetrlist):
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + upperMessage + "TRY"
        response = requests.get(url)
        output = response.json()
        symbol = "₺"
        price = format(float(output['lastPrice']))
        percent = "  {:.2f}%".format(float(output['priceChangePercent']))
        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "BinanceTR -> " + upperMessage + ': ' + symbol + price + percent

    return resultMessage