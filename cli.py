import ccxt
# import ccxt.async_support as ccxt

print("開始します")
# print(ccxt.exchanges)

zaif = ccxt.zaif()
bitflyer = ccxt.bitflyer()


print(f"ティッカー: {zaif.fetch_ticker('BTC/JPY')['last']}")
print(f"ティッカー: {zaif.fetch_ticker('XEM/JPY')['last']}")
print(f"ティッカー: {bitflyer.fetch_ticker('BTC/JPY')['last']}")

