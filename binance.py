import requests
from lists import binancelist

def handleBinance(message, resultMessage):
    upperMessage = message.text.upper()
    speciallist = ["USDT", "ETHBTC"]
    if (upperMessage in binancelist) or (upperMessage in speciallist):
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + upperMessage + "USDT"
        if upperMessage == "USDT":
            url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + "USDT" + "TRY"
        if upperMessage == "ETHBTC":
            url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + "ETH" + "BTC"
        response = requests.get(url)
        output = response.json()
        symbol = ""
        price = ""
        if upperMessage == "USDT":
            symbol = "₺"
            price = format(float(output['lastPrice']))
        elif upperMessage == "ETHBTC":
            symbol = "₿"
            price = format(float(output['lastPrice']))
        else:
            symbol = "$"
            price = format(float(output['lastPrice']))
        percent = "  {:.2f}%".format(float(output['priceChangePercent']))
        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "Binance -> " + upperMessage + ': ' + symbol + price + percent

    if message.text.upper()=="GAINERS" or message.text.upper()=="LOSERS":
        changePercentList = []
        url = "https://api.binance.com/api/v3/ticker/24hr"
        response = requests.get(url)
        output = response.json()
        for i in binancelist:
            upperMessage = i + "USDT"
            index = [j for j,_ in enumerate(output) if _['symbol'] == upperMessage][0]
            changePercentList.append([i,float(output[index]['lastPrice']),float(output[index]["priceChangePercent"])])

        if resultMessage != "":
            resultMessage += "\n"
        if message.text.upper()=="GAINERS":
            changePercentList.sort(key= lambda coin: coin[2], reverse=True)
            resultMessage += "Binance Top Gainers:"
        if message.text.upper()=="LOSERS":
            changePercentList.sort(key= lambda coin: coin[2])
            resultMessage += "Binance Top Losers:"

        for i in range(5):
            if resultMessage != "":
                resultMessage += "\n"
            resultMessage += changePercentList[i][0] + ': ' + format(changePercentList[i][1]) + "  {:.2f}%".format(float(changePercentList[i][2]))

    return resultMessage