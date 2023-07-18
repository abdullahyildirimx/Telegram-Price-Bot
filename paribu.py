import json
import urllib.request
from lists import paribulist

def handleParibu(message, resultMessage):
    if message.text.upper() in paribulist:
        lowerMessage = message.text.lower()
        upperMessage = message.text.upper()
        user_agent = 'Mozilla/5.0'
        pair = lowerMessage + "_tl"

        url = "https://web.paribu.com/initials/ticker/extended"
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)
        price = float(output["payload"][pair]["last"])
        change = float(output["payload"][pair]["percentage"])

        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "Paribu -> " + upperMessage + ': ₺' + format(price) + "  %{:.2f}".format(change)
    return resultMessage    
