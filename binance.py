import requests

def handleBinance(message, resultMessage, binancelist):
    upperMessage = message.text.upper()
    speciallist = ["ETHBTC"]

    if (upperMessage in binancelist) or (upperMessage in speciallist):
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + upperMessage + "USDT"
        if upperMessage == "ETHBTC":
            url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + "ETH" + "BTC"
        response = requests.get(url)
        output = response.json()
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

        binancelist = [entry["symbol"] for entry in output if entry["symbol"].endswith("USDT") and entry["bidPrice"] != "0.00000000"]
        for i in range(0,len(binancelist)):
            binancelist[i]=binancelist[i].replace("USDT", "")
        binancelist = sorted(binancelist)
        
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