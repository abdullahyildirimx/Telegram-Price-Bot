import requests
from lists import currencylist

def handleCurrency(message, resultMessage):
    if message.text.upper() in currencylist:
        url = "https://www.bloomberght.com/doviz/dolar"
        response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
        output = response.text
        index = output.find('"son_fiyat"  data-secid="USDTRY Curncy">')
        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += ('Dolar: ₺' + output[index+40:index+46])
    return resultMessage
