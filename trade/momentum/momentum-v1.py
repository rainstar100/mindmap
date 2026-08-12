

import pandas as pd
from pathlib import Path
from scipy import stats
import numpy as np
import os
from datetime import datetime



# tool,func
def read_stocklist_fromtdx():
    folder_path = Path('d:/方正证券/小方/vipdoc/')
    stocklist = [p.stem[2:] for p in folder_path.glob('*/lday/*.day') if not p.stem.lower().startswith('bj')]
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

def head(num=20):
    stocklist = read_stocklist_fromtdx()
    scores = {}
    for stock_code in stocklist:
        dataname = read_tdxfile(stock_code)
        if dataname is not None:
            ts = get_ts(dataname)
            score = momentum_score(ts)
            scores[stock_code] = score
            print(f'Stock code: {stock_code}, Momentum Score: {score:.2f}')
        else:
            print(f"Data for stock code {stock_code} could not be read.")
    return sorted(scores,key=scores.get,reverse=True)[:num]


def code_to_tdx(code: str) -> str:

    if code.startswith(('6', '5')):      
        return '1' + code
    elif code.startswith(('0', '3')):    
        return '0' + code
    elif code.startswith(('8', '4')):    
        return '2' + code
    else:
        return '0' + code  
def save(head20):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    tdx_path = r'D:\lh\momentum\blk'  
    zxg_file = os.path.join(tdx_path, timestamp+'.blk')

    tdx_lines = [code_to_tdx(c) for c in head20]
    print(f"准备写入 {len(tdx_lines)} 只股票到自选股")

    
    with open(zxg_file, 'w', encoding='gbk') as f:
        f.write('\n'.join(tdx_lines))

    print(f"成功写入 {len(tdx_lines)} 只股票到自选股")


if __name__ == "__main__":
    head20 = head(20)
    save(head20)
