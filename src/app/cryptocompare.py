from app.config import MARKET_1, MARKET_2
from app.utils import get_json_data

def get_data(timestamp_from, timestamp_to):
    url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={MARKET_1}&tsym={MARKET_2}&allData=true'
    data = get_json_data(url)['Data']['Data']
    filtered_data = [d for d in data if d['time'] >= timestamp_from and d['time'] <= timestamp_to]
    return filtered_data
