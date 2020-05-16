WALLET_TABLE = 'Wallet'
TICKER_TABLE = 'Tickers'

import sqlite3
from time import gmtime, strftime

conn = sqlite3.connect('app/database/database.db', check_same_thread=False)
c = conn.cursor()

def fetchall(sql):
    return c.execute(sql).fetchall()

def get_wallet():
    return fetchall(f'SELECT Currency, Value FROM {WALLET_TABLE}')

def insert_into_wallet(currency_value_map):
    for currency, value in currency_value_map.items():
        c.execute(f'INSERT INTO {WALLET_TABLE} (Currency, Value) VALUES (?, ?)', (currency, value))
    conn.commit()

def update_in_wallet(currency, value):
    c.execute(f'UPDATE {WALLET_TABLE} SET Value=(?) WHERE Currency=(?)', (value, currency))
    conn.commit()

def delete_wallet():
    c.execute(f'DELETE FROM {WALLET_TABLE}')
    conn.commit()

def insert_market_data(buy, sell, market):
    c.execute(f'INSERT INTO {TICKER_TABLE} (buy, sell, market) VALUES (?, ?, ?)', (buy, sell, market))
    conn.commit()
