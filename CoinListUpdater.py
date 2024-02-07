import json
import urllib.request

currencylist = ['DOLAR', 'USD']
gaslist = ['GAS']
mexclist = ['CEEK', 'RACA']
coingeckolist = []
okxlist = []

user_agent = 'Mozilla/5.0'
url = "https://api.binance.com/api/v3/ticker/24hr"
headers={'User-Agent':user_agent,}
request=urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)
data = response.read()
output = json.loads(data)

binancelist = [entry["symbol"] for entry in output if entry["symbol"].endswith("USDT") and entry["bidPrice"] != "0.00000000"]
for i in range(0,len(binancelist)):
    binancelist[i]=binancelist[i].replace("USDT", "")
try:
    binancelist.pop(binancelist.index("BNBUP"))
    binancelist.pop(binancelist.index("BNBDOWN"))
    binancelist.pop(binancelist.index("BTCUP"))
    binancelist.pop(binancelist.index("BTCDOWN"))
    binancelist.pop(binancelist.index("ETHUP"))
    binancelist.pop(binancelist.index("ETHDOWN"))
    binancelist = sorted(binancelist)
except:
    pass

paribulist = []
user_agent = 'Mozilla/5.0'
url = "https://web.paribu.com/initials/config"
headers={'User-Agent':user_agent,} 
request=urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)
data = response.read()
output = json.loads(data)
paribulistTemp = list(output["payload"]["currencies"].keys())
		
for i in paribulistTemp:
	if output["payload"]["currencies"][i]["hide_if_void"]==False:
		paribulist.append(i.upper())
            
print("binancelist = ", binancelist)
print("coingeckolist = ", coingeckolist)
print("currencylist = ", currencylist)
print("gaslist = ", gaslist)
print("mexclist = ", mexclist)
print("okxlist = ", okxlist)
print("paribulist = ", paribulist)