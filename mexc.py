import requests
from lists import mexclist

def handleMexc(message, resultMessage):
    if message.text.upper() in mexclist:
        upperMessage = message.text.upper()
        url = "https://www.mexc.com/open/api/v2/market/ticker?symbol=" + upperMessage + "_USDT"
        response = requests.get(url)
        output = response.json()

        if resultMessage != "":
            resultMessage += "\n"
            
        resultMessage += "Mexc -> " + upperMessage + ': $' + format(float(output['data'][0]['last'])) + "  %{:.2f}".format(100*float(output['data'][0]['change_rate']))
    return resultMessage        