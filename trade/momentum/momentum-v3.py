

import pandas as pd
from pathlib import Path
from scipy import stats
import numpy as np
import os
from datetime import datetime
from MultiTaskProcessor import MultiThreadTaskProcessor as mttp



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
    if market:
        try:
            dataname=tdx_reader.get_df(stock_code, market)
            return dataname
        except Exception as e:
            print('reading error:', e)
            #return None



def get_ts(stock_data, fromdate='2021-01-01', todate='2025-11-01'):

    ts = stock_data.tail(10)['close']
    return ts
def momentum_score(stock_code) :


    stock_date = read_tdxfile(stock_code)
    if stock_date is not None:
        ts = get_ts(stock_date)
        x=np.arange(len(ts))
        log_ts=np.log(ts)
        slop,intercept,r_value,p_value,std_err=stats.linregress(x,log_ts)
        annualized_slope=((1+slop)**252-1)*100 
        score=annualized_slope*(r_value**2)
        print(f"{stock_code} score: {score:.2f}")
        return {'code':stock_code, 'score':np.round(score,2)}

def cal_score(stocklist,momentum_score):
    tasks = stocklist
    task_handler=momentum_score
    # create processor
    processor = mttp(task_list=tasks, task_handler=task_handler, num_workers=4)

    # start processor
    processor.start()

    # wait for all tasks to be completed
    processor.wait_completion()

    # get results
    results = processor.get_results()
    print("results:", results)
    return results


def code_to_tdx(code: str) -> str:

    if code.startswith(('6', '5')):      
        return '1' + code
    elif code.startswith(('0', '3')):    
        return '0' + code
    elif code.startswith(('8', '4')):    
        return '2' + code
    else:
        return '0' + code  
def save(results):
    filtered_results = [x for x in results if x is not None]
    sorted_results = sorted(filtered_results, key=lambda x: x['score'], reverse=True)[:20]

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    tdx_path = r'D:\lh\momentum\blk'  
    zxg_file = os.path.join(tdx_path, timestamp+'.blk')

    tdx_lines = [code_to_tdx(c['code']) for c in sorted_results]
    print(f"准备写入 {len(tdx_lines)} 只股票到自选股")

    
    with open(zxg_file, 'w', encoding='gbk') as f:
        f.write('\n'.join(tdx_lines))

    print(f"成功写入 {len(tdx_lines)} 只股票到自选股")
def main():
    stocklist = read_stocklist_fromtdx()
    results=cal_score(stocklist,momentum_score)
    save(results)

if __name__ == "__main__":
    main()
