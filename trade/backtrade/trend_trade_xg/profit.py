import pandas as pd
from tool import *
import matplotlib.pyplot as plt

stock_lsit=read_stocklist('xghc20251209.xls')
profit_summary=pd.read_csv(f'results/{stock_lsit[0]}/profit.csv')
#print(profit_summary.columns)
profit_summary.set_index('Date',inplace=True)
profit_summary['Portfolio_Value']=0
#print(profit_summary.head())

def fill(


for stock_code in read_stocklist('xghc20251209.xls'):
 
    item=pd.read_csv(f'results/{stock_code}/profit.csv')
    item.set_index('Date',inplace=True)
    print(f'{stock_code} of rows-->{len(item)}')

    for date in profit_summary.index.values:
        if date not in item.index.values:
            profit_summary.at[date,'Portfolio_Value']=profit_summary.at[date,'Portfolio_Value'] + 100
            #print(profit_summary.at[date,'Portfolio_Value'])
        else:
            profit_summary.at[date,'Portfolio_Value']=profit_summary.at[date,'Portfolio_Value']+item.at[date,'Portfolio_Value']/10000

print(profit_summary.head(1))
print(profit_summary.tail(1))

profit_summary.to_csv('results/total_profit.csv',index=True)

