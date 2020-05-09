MARKET_CURRENCY_MAPPING = {
    'BTC-USD': 'BTC',
    'LTC-USD': 'LTC',
    'ETH-USD': 'ETH',
    'XRP-USD': 'XRP',
}

CURRENCIES = list(MARKET_CURRENCY_MAPPING.values())
MARKETS = list(MARKET_CURRENCY_MAPPING.keys())

INITIAL_WALLET = {
    'USD': 3000,
    'BTC': 0,
    'LTC': 0,
    'ETH': 0,
    'XRP': 0,
}

TRADING_FEE = 0.0010

BITBAY_API_URL = 'https://api.bitbay.net/rest/trading/ticker/'

