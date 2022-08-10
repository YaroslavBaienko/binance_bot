from distutils.command.clean import clean
import mylib
from binance.client import Client
import matplotlib
import json
import pandas as pd


client = Client(
    mylib.api_key,
    mylib.secret_key,
    #  testnet=True
)


tickers = client.get_all_tickers()


cake = list()
for item in tickers:
    a = item["symbol"]
    if "CAKE" in a:
        print(item)
        cake.append(item)
    else:
        continue

# print(cake)


info = client.get_account()
df = pd.DataFrame(info["balances"])
df["free"] = df["free"].astype(float).round(4)
df = df[df["free"] > 0]
# print(df)

trades = client.get_historical_trades(symbol="CAKEUSDT")
# print(trades)
cakehistory = dict()
for trade in trades:
    print(str(trade['time']) + ": " + trade["price"])
    cakehistory[trade["time"]] = trade["price"]


avges = client.get_avg_price(symbol="CAKEUSDT")
print(avges)
