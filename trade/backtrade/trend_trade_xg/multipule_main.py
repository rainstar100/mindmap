import backtrader as bt
#from newhigh_strategy import NewHighStrategy
from multipule_newhigh_strategy import MultipuleNewHighStrategy 
import pandas as pd
import datetime
from tool import *



def main():
    cerebro = init_bt_engine(commission=0.0005, initial_cash=10000000)
    cerebro = add_data_to_bt(read_stocklist('xghc202501.xls'), cerebro,fromdate='2024-06-01', todate='2025-02-01')
    cerebro.addstrategy(MultipuleNewHighStrategy)
    results=cerebro.run()
    print(cerebro.broker.getvalue())
    analyze_results(results,cerebro)
    cerebro.plot(style='candle',upcolor='red',downcolor='green',volume=False)

if __name__ == '__main__':
    main()
