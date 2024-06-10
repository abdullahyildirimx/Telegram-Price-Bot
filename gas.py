import json
import urllib.request
from lists import gaslist
from keys import etherscankey

def handleGas(message, resultMessage):
    if message.text.upper()=="GAS":
        upperMessage = message.text.upper()
        user_agent = 'Mozilla/5.0'
        url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=" + etherscankey
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)

        if resultMessage != "":
            resultMessage += "\n"

        resultMessage += "Low: " + output['result']['SafeGasPrice'] + " Gwei\n"
        resultMessage += "Average: " + output['result']['ProposeGasPrice'] + " Gwei\n"
        resultMessage += "High: " + output['result']['FastGasPrice'] + " Gwei\n"
    return resultMessage