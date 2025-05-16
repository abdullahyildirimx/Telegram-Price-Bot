import requests
from lists import mexclist

def handleMexc(message, resultMessage):
    if message.text.upper() in mexclist:
        upperMessage = message.text.upper()
        url = "https://api.mexc.com/api/v3/ticker/24hr?symbol=" + upperMessage + "_USDT"
        response = requests.get(url)
        output = response.json()
        price = format(float(output['lastPrice']))
        percent = "  {:.2f}%".format(100*float(output['priceChangePercent']))
        if resultMessage != "":
            resultMessage += "\n"
            
        resultMessage += "Mexc -> " + upperMessage + ': $' + price + percent
    return resultMessage        