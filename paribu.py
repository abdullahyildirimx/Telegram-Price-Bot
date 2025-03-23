import requests
from lists import paribulist

def handleParibu(message, resultMessage):
    if message.text.upper() in paribulist:
        lowerMessage = message.text.lower()
        upperMessage = message.text.upper()
        pair = lowerMessage + "_tl"
        url = "https://web.paribu.com/initials/ticker/extended"
        response = requests.get(url)
        output = response.json()
        price = float(output["payload"][pair]["last"])
        change = float(output["payload"][pair]["percentage"])

        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "Paribu -> " + upperMessage + ': ₺' + format(price) + "  {:.2f}%".format(change)
    return resultMessage    
