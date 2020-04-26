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

for api in apis:
    print(api)
    print('-=-=-=-=-=-=-=-=-=-=-')
    for i, market in enumerate(market_mappings[api]):
        print(f'{market_names[i]}: {get_buy_sell(api, market)}')
    print('-=-=-=-=-=-=-=-=-=-=-')
    print()

