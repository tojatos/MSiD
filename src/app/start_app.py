from app import cryptocompare
from app import plot
from pprint import pprint
from datetime import datetime

if __name__ == "__main__":
    start_time = datetime(2020, 5, 1)
    end_time = datetime(2020, 5, 21)
    data = cryptocompare.get_data(datetime.timestamp(start_time), datetime.timestamp(end_time))
    for d in data:
        d['time'] = datetime.fromtimestamp(d['time'])
    plot.plot(data)
