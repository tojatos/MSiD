#!/usr/bin/env python3

import urllib.request, json
from time import sleep

market_names = [
    'BTC',
    'LTC',
    'ETH',
    'XRP',
]

apis = [
    'bittrex',
    'bitbay',
    'kraken',
    'binance',
]

market_mappings = {
    'bittrex': [
        'USD-BTC',
        'USD-LTC',
        'USD-ETH',
        'USD-XRP',
    ],
    'bitbay': [
        'BTC-USD',
        'LTC-USD',
        'ETH-USD',
        'XRP-USD',
    ],
    'kraken': [
        'XBTUSD',
        'LTCUSD',
        'ETHUSD',
        'XRPUSD',
    ],
    'binance': [
        'BTCTUSD',
        'LTCTUSD',
        'ETHTUSD',
        'XRPTUSD',
    ],
}

urls = {
    'bittrex': 'https://api.bittrex.com/api/v1.1/public/getticker?market=',
    'bitbay':  'https://api.bitbay.net/rest/trading/ticker/',
    'kraken':  'https://api.kraken.com/0/public/Ticker?pair=',
    'binance': 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=',
}

def get_json_data(url):
    with urllib.request.urlopen(url) as u:
        return json.loads(u.read().decode())

def extract_buy_sell(api, data):
    if api == 'bittrex':
        return (data['result']['Bid'], data['result']['Ask'])
    if api == 'bitbay':
        return (float(data['ticker']['highestBid']), float(data['ticker']['lowestAsk']))
    if api == 'kraken':
        values = next(iter(data['result'].values()))
        return (float(values["b"][0]), float(values["a"][0]))
    if api == 'binance':
        return (float(data['bidPrice']), float(data['askPrice']))

def get_buy_sell(api, market):
    url = f"{urls[api]}{market}"
    data = get_json_data(url)
    return extract_buy_sell(api, data)

def gather_data():
    data = {}
    for i, market in enumerate(market_names):
        data[market] = {api: get_buy_sell(api, market_mappings[api][i]) for api in apis}
    return data

def print_best_arbitrage(data, market):
    d = data[market]

    max_buy_market = max(d, key=lambda x: d[x][0])
    min_sell_market = min(d, key=lambda x: d[x][1])

    if max_buy_market == min_sell_market:
        return

    max_buy = d[max_buy_market][0]
    min_sell = d[min_sell_market][1]

    if max_buy > min_sell:
        print(f'Arbitrage possible on {market}:')
        print(f'buy on {min_sell_market} for {min_sell} $')
        print(f'sell on {max_buy_market} for {max_buy} $')
        print(f'to gain {round(max_buy - min_sell, 2)} $')
        print()

def print_best_arbitrages():
    data = gather_data()
    for market in market_names:
        print_best_arbitrage(data, market)

def monitor_best_arbitrages():
    while True:
        print_best_arbitrages()
        sleep(5)

if __name__ == "__main__":
    monitor_best_arbitrages()
