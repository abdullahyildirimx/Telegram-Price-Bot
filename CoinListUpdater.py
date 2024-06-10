import requests

currencylist = ['DOLAR', 'USD']
gaslist = ['GAS']
mexclist = ['CEEK', 'RACA']

url = "https://api.binance.com/api/v3/ticker/24hr"
response = requests.get(url)
output = response.json()

binancelist = [entry["symbol"] for entry in output if entry["symbol"].endswith("USDT") and entry["bidPrice"] != "0.00000000"]
for i in range(0,len(binancelist)):
    binancelist[i]=binancelist[i].replace("USDT", "")
binancelist = sorted(binancelist)

paribulist = []
url = "https://web.paribu.com/initials/config"
response = requests.get(url)
output = response.json()
paribulistTemp = list(output["payload"]["currencies"].keys())
		
for i in paribulistTemp:
    if output["payload"]["currencies"][i]["hide_if_void"]==False:
        paribulist.append(i.upper())

with open('lists.py', 'w') as f:
    f.write(f"binancelist = {binancelist}\n")
    f.write(f"currencylist = {currencylist}\n")
    f.write(f"gaslist = {gaslist}\n")
    f.write(f"mexclist = {mexclist}\n")
    f.write(f"paribulist = {paribulist}\n")