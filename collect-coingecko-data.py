from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# btc_price = cg.get_price(ids='bitcoin', vs_currencies='usd')
# {'bitcoin': {'usd': 9186.89}}
# btc_price

# multi_price = cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
# multi_price

# usd_price = cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
# usd_price

# coin_list = cg.get_coins_list()
# coin_list
# for item in coin_markets:
#    print("Symbol: {} Name: {} Id: {}\n".format(item['symbol'],item['name'],item['id']))

# For Coin markets:
#   {
#     "id": "bitcoin",
#     "symbol": "btc",
#     "name": "Bitcoin",
#     "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579",
#     "current_price": 9186.79,
#     "market_cap": 169480345274,
#     "market_cap_rank": 1,
#     "total_volume": 16054018229,
#     "high_24h": 9218.76,
#     "low_24h": 9106.67,
#     "price_change_24h": 28.71,
#     "price_change_percentage_24h": 0.31347,
#     "market_cap_change_24h": 583005660,
#     "market_cap_change_percentage_24h": 0.34518,
#     "circulating_supply": 18437281,
#     "total_supply": 21000000,
#     "ath": 19665.39,
#     "ath_change_percentage": -53.27264,
#     "ath_date": "2017-12-16T00:00:00.000Z",
#     "atl": 67.81,
#     "atl_change_percentage": 13451.47515,
#     "atl_date": "2013-07-06T00:00:00.000Z",
#     "roi": null,
#     "last_updated": "2020-07-20T02:52:42.433Z"
#   },
#   etc...
# vs_currency=usd&order=market_cap_desc&per_page=250&page=10&sparkline=false&price_change_percentage=24h%2C30d

print("Rank, Symbol, Name, ID, Price, MarketCap, Volume, 24h_high, 24h_low, Price_change_24h, Price_change_30d, MarketCap_change_24hr, Circulated_supply, Total_supply, All-time_high_percentage, All-time_low_percentage")

coin_markets_page1 = cg.get_coins_markets(vs_currency='usd',per_page='250',page='1',price_change_percentage='24h,30d')
for item in coin_markets_page1:
    print("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(item['market_cap_rank'],item['symbol'],item['name'],item['id'],item['current_price'],item['market_cap'],item['total_volume'],item['high_24h'],item['low_24h'],item['price_change_percentage_24h_in_currency'],item['price_change_percentage_30d_in_currency'],item['market_cap_change_percentage_24h'],item['circulating_supply'],item['total_supply'],item['ath_change_percentage'],item['atl_change_percentage']))

coin_markets_page2 = cg.get_coins_markets(vs_currency='usd',per_page='250',page='2',price_change_percentage='24h,30d')
for item in coin_markets_page2:
    print("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(item['market_cap_rank'],item['symbol'],item['name'],item['id'],item['current_price'],item['market_cap'],item['total_volume'],item['high_24h'],item['low_24h'],item['price_change_percentage_24h_in_currency'],item['price_change_percentage_30d_in_currency'],item['market_cap_change_percentage_24h'],item['circulating_supply'],item['total_supply'],item['ath_change_percentage'],item['atl_change_percentage']))

coin_markets_page3 = cg.get_coins_markets(vs_currency='usd',per_page='250',page='3',price_change_percentage='24h,30d')
for item in coin_markets_page3:
    print("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(item['market_cap_rank'],item['symbol'],item['name'],item['id'],item['current_price'],item['market_cap'],item['total_volume'],item['high_24h'],item['low_24h'],item['price_change_percentage_24h_in_currency'],item['price_change_percentage_30d_in_currency'],item['market_cap_change_percentage_24h'],item['circulating_supply'],item['total_supply'],item['ath_change_percentage'],item['atl_change_percentage']))

coin_markets_page4 = cg.get_coins_markets(vs_currency='usd',per_page='250',page='4',price_change_percentage='24h,30d')
for item in coin_markets_page4:
    print("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(item['market_cap_rank'],item['symbol'],item['name'],item['id'],item['current_price'],item['market_cap'],item['total_volume'],item['high_24h'],item['low_24h'],item['price_change_percentage_24h_in_currency'],item['price_change_percentage_30d_in_currency'],item['market_cap_change_percentage_24h'],item['circulating_supply'],item['total_supply'],item['ath_change_percentage'],item['atl_change_percentage']))

coin_markets_page5 = cg.get_coins_markets(vs_currency='usd',per_page='250',page='5',price_change_percentage='24h,30d')
for item in coin_markets_page5:
    print("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(item['market_cap_rank'],item['symbol'],item['name'],item['id'],item['current_price'],item['market_cap'],item['total_volume'],item['high_24h'],item['low_24h'],item['price_change_percentage_24h_in_currency'],item['price_change_percentage_30d_in_currency'],item['market_cap_change_percentage_24h'],item['circulating_supply'],item['total_supply'],item['ath_change_percentage'],item['atl_change_percentage']))

coin_markets_page6 = cg.get_coins_markets(vs_currency='usd',per_page='250',page='6',price_change_percentage='24h,30d')
for item in coin_markets_page6:
    print("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(item['market_cap_rank'],item['symbol'],item['name'],item['id'],item['current_price'],item['market_cap'],item['total_volume'],item['high_24h'],item['low_24h'],item['price_change_percentage_24h_in_currency'],item['price_change_percentage_30d_in_currency'],item['market_cap_change_percentage_24h'],item['circulating_supply'],item['total_supply'],item['ath_change_percentage'],item['atl_change_percentage']))

coin_markets_page7 = cg.get_coins_markets(vs_currency='usd',per_page='250',page='7',price_change_percentage='24h,30d')
for item in coin_markets_page7:
    print("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(item['market_cap_rank'],item['symbol'],item['name'],item['id'],item['current_price'],item['market_cap'],item['total_volume'],item['high_24h'],item['low_24h'],item['price_change_percentage_24h_in_currency'],item['price_change_percentage_30d_in_currency'],item['market_cap_change_percentage_24h'],item['circulating_supply'],item['total_supply'],item['ath_change_percentage'],item['atl_change_percentage']))

