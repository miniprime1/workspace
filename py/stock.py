# pip install yahoo-fin
# pip install requests

from yahoo_fin.stock_info import *
import json
import requests

print("Stock, version 1.0")
print("Copyright (C) 2020 miniprime1")
print("[Powered by Yahoo Finance]\n")

symbol = input("Enter Stock Symbol: ")
print("")

url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
result = requests.get(url).json()
for x in result['ResultSet']['Result']: 
    if x['symbol'] == symbol: 
        company = x['name']

try: 
    quote_table = json.loads(json.dumps(get_quote_table(symbol)))
    print("Company Name:", company)
    print("Symbol:", symbol.upper())
    for name in quote_table: print(f"{name}: {quote_table[name]}")
    # Time Piece Code 1
except Exception as e: 
    print(f"Error: {e}!")

# Test Code 1
# from yahoo_fin.stock_info import *
# import json, requests
# url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
# result = requests.get(url).json()
# for x in result['ResultSet']['Result']: 
#   if x['symbol'] == 'aapl': 
#     company = x['name']
# quote_table = json.loads(json.dumps(get_quote_table('aapl')))
# for name in quote_table: print(f"{name}: {quote_table[name]}")

# Time Piece Code 1
# apikey = '0e1a0c0ce8b16e6007db23008a76dafb'
# price_list = []
# history = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?serietype=line&apikey={apikey}").json()
# history = history["historical"]
# df = pandas.DataFrame.from_dict(history)
# df = df.rename({'close': symbol}, axis=1)
# price_list.append(df)
# dfs = [d.set_index('date') for d in price_list]
# concat = pandas.concat(dfs,axis=1)
# concat = concat/concat.iloc[0]
# concat.plot()
# plt.show()