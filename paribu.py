import requests

def handleParibu(message, resultMessage):
    paribulist = []
    url = "https://web.paribu.com/initials/config"
    response = requests.get(url)
    output = response.json()
    paribulistTemp = list(output["payload"]["currencies"].keys())
            
    for i in paribulistTemp:
        if output["payload"]["currencies"][i]["hide_if_void"]==False:
            paribulist.append(i.upper())

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
