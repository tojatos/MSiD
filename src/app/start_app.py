import pandas as pd
from datetime import datetime

from app import cryptocompare
from app import plot
from app.config import START_TIME, END_TIME, SIM_END_TIME

def get_adjusted_data():
    data = cryptocompare.get_data(
        datetime.timestamp(START_TIME),
        datetime.timestamp(END_TIME),
    )

    for d in data:
        d['time'] = datetime.fromtimestamp(d['time'])

    df = pd.DataFrame(data)
    df['per_ch'] = (df['close'] - df['open']) / df['open'] * 100.0
    return df


if __name__ == "__main__":
    df = get_adjusted_data()

    plot.plot(df)
