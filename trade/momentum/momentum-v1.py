

import pandas as pd

import matplotlib.dates as mdates

from pathlib import Path
from scipy import stats
import numpy as np

# tool,func
def read_stocklist_fromtdx():
    folder_path = Path('d:/方正证券/小方/vipdoc/')
    stocklist = [p.stem for p in folder_path.glob('*/lday/*.day') if not p.stem.lower().startswith('bj')]
    return stocklist


def read_tdxfile(stock_code):
    from tdxpy.reader import TdxDailyBarReader 
    tdx_reader = TdxDailyBarReader('d:/方正证券/小方/vipdoc/')
    if stock_code.startswith('6'):
        market = 'sh'
    if stock_code.startswith('0') or stock_code.startswith('3'):
        market = 'sz'
    if stock_code.startswith('9') :
        market = 'bj'
    try:
        dataname=tdx_reader.get_df(stock_code, market)
        return dataname
    except Exception as e:
        print('reading error:', e)
        return None


def get_ts(stock_data, fromdate='2021-01-01', todate='2025-11-01'):

    ts = stock_data.tail(10)['close']
    return ts
def momentum_score(ts) :
    x=np.arange(len(ts))
    log_ts=np.log(ts)
    slop,intercept,r_value,p_value,std_err=stats.linregress(x,log_ts)
    annualized_slope=((1+slop)**252-1)*100 
    score=annualized_slope*(r_value**2)
    return score

def main():
    stocklist = read_stocklist_fromtdx()
    scores = {}
    for stock_code in stocklist:
        dataname = read_tdxfile(stock_code[2:])
        if dataname is not None:
            ts = get_ts(dataname)
            score = momentum_score(ts)
            scores[stock_code] = score
            print(f'Stock code: {stock_code}, Momentum Score: {score:.2f}')
        else:
            print(f"Data for stock code {stock_code} could not be read.")
    return sorted(scores,key=scores.get,reverse=True)[:20]

if __name__ == "__main__":
    print(main())