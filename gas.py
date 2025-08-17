import requests
from keys import etherscankey

def handleGas(message, resultMessage, gaslist):
    if message.text.upper() in gaslist:
        url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=" + etherscankey
        response = requests.get(url)
        output = response.json()
        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "Low: " + output['result']['SafeGasPrice'] + " Gwei\n"
        resultMessage += "Average: " + output['result']['ProposeGasPrice'] + " Gwei\n"
        resultMessage += "High: " + output['result']['FastGasPrice'] + " Gwei\n"
    return resultMessage