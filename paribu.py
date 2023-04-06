import json
import urllib.request
from lists import paribulist

def handleParibu(message, resultMessage):
    if message.text.upper() in paribulist:
        lowerMessage = message.text.lower()
        upperMessage = message.text.upper()
        user_agent = 'Mozilla/5.0'
        pair = lowerMessage + "_tl"

        url = "https://web.paribu.com/market/" + pair + "/latest-matches"
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)
        output2 = output["payload"]
        price = float(output2[list(output2)[0]]["price"])

        url = "https://web.paribu.com/chart/history?symbol=" + pair + "&period=1D&type=basic"
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)
        price2 = float(output["c"][0])
        change = 100*((price-price2)/price2)

        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "Paribu -> " + upperMessage + ': ₺' + format(price) + "  %{:.2f}".format(change)
    return resultMessage    
