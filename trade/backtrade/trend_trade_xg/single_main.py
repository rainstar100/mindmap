import backtrader as bt
from newhigh_strategy_v2 import NewHighStrategy
import pandas as pd
import datetime
from tool import *
import os
from MultiTaskProcessor import MultiThreadTaskProcessor as mttp

def task_backtrade(stock_code):
        try:
            os.mkdir(f'results/{stock_code}')
        except FileExistsError:
            pass
        print(f'{stock_code} is being processed')
        cerebro = init_bt_engine(commission=0.0005, initial_cash=1000000)
        inital_capital=cerebro.broker.getvalue()
        dataname=read_tdxfile(stock_code)
        data=bt.feeds.PandasData(dataname=dataname,fromdate=pd.Timestamp('2020-06-01'),todate=pd.Timestamp('2025-11-01'))
        cerebro.adddata(data)
        cerebro.addstrategy(NewHighStrategy)
        results=cerebro.run()
        profit= cerebro.broker.getvalue()-inital_capital
        analyze_results(results,cerebro,stock_code,profit)
        print('*' * 50)
        print(f'{stock_code} is completed--->profit:{profit}')
        print('*' * 50)
        return [stock_code,profit]
       

if __name__ == '__main__':

    # Create an instance of the MultiTaskProcessor

    #task_list= read_stocklist('xghc20251209.xls')
    task_list=['000062']
    processor = mttp(task_list ,task_backtrade,num_workers=1)

    processor.start()
    processor.wait_completion()
    results=processor.get_results()
    results_df=pd.DataFrame(results,columns=['stock_code','profit'])
    results_df.to_csv('results/summary_results.csv',index=False)
    print('All tasks completed.')
    print(results_df['profit'].sum())
    print(results_df['profit'].describe())
