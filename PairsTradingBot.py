import numpy as np
import pandas as pd
import time
import datetime as dt
from datetime import time as dttime
from yahoo_fin import stock_info as si
from pandas_datareader import data as pdr

start = dt.datetime(2017, 1, 1)
end = dt.datetime.today()

tickers = ['BDX', 'BAX']

df = pdr.get_data_yahoo(tickers, start, end)['Adj Close']

stock1 = 'BDX'
stock2 = 'BAX'
live_ratio = (si.get_live_price(f'{stock1}')) / (si.get_live_price(f'{stock2}'))

S1 = df[stock1]
S2 = df[stock2]

ratio = S1 / S2

mkt_close = dttime(16, 0, 0)
mkt_open = dttime(9, 30, 0)
now = dt.datetime.now()
now_time = dt.datetime.time(now)

zscore = (live_ratio - ratio.mean()) / ratio.std()


def time_in_range(mkt_open, mkt_close, x):
    if mkt_close <= mkt_open:
        return mkt_close <= x <= mkt_open
    else:
        return mkt_close <= x or x <= mkt_open


while True:
    if time_in_range(mkt_close, mkt_open, now_time):
        if zscore > -1:
            print('Buy')
        elif zscore < 1:
            print('Sell')
        else:
            Print('Ratio is within standard deviation')
        print(zscore)
        time.sleep(10)
    else:
        pass