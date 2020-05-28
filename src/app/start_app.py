from app import cryptocompare
from pprint import pprint

if __name__ == "__main__":
    pprint(cryptocompare.get_data(1590033180, 1590681234))
