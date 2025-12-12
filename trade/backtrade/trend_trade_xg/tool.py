import backtrader as bt
import pandas as pd
import datetime
import matplotlib.dates as mdates
import akshare as ak

def read_stocklist(filename):
    import pandas as pd
    res=pd.read_csv(filename,encoding='gbk',sep='\t')
    stocklist=res['品种代码'].astype('str').str.zfill(6).tolist()
    #print(stocklist)
    return stocklist
    

def read_tdxfile(stock_code):
    from tdxpy.reader import TdxDailyBarReader 
    tdx_reader = TdxDailyBarReader('d:/方正证券/小方/vipdoc/')
    if stock_code.startswith('6'):
        market = 'sh'
    if stock_code.startswith('0') or stock_code.startswith('3'):
        market = 'sz'
    try:
        dataname=tdx_reader.get_df(stock_code, market)
        return dataname
    except Exception as e:
        print('reading error:', e)
        return None

def init_bt_engine(commission=0.0, initial_cash=50000):
    cerebro = bt.Cerebro()
    cerebro.broker.setcommission(commission)
    cerebro.broker.setcash(initial_cash)
    cerebro.addanalyzer(bt.analyzers.PyFolio, _name='PyFolio')
    cerebro.addanalyzer(bt.analyzers.Transactions, _name='transactions')
    print('Initial Portfolio Value: %.2f' % cerebro.broker.getvalue())
    print('Commission: %.4f' % commission)
    print('*'*30)
    return cerebro

def add_data_to_bt(stocklist, cerebro, fromdate='2021-01-01', todate='2025-11-01'):
    for stock_code in stocklist:
        dataname = read_tdxfile(stock_code)
        if dataname is not None:
            data=bt.feeds.PandasData(dataname=dataname,fromdate=pd.Timestamp(fromdate),todate=pd.Timestamp(todate))
            cerebro.adddata(data, name=stock_code)
            print(f'Added data for stock code: {stock_code}--->{len(cerebro.datas)/len(stocklist)*100:.2f}%')
            
        else:
            raise ValueError(f"Data for stock code {stock_code} could not be read.")
    return cerebro

def analyze_results(results,cerebro,stock_code,profit):

    strat = results[0]

    pyfolio_stats = strat.analyzers.PyFolio.get_pf_items()
    returns, positions, transactions, gross_lev = pyfolio_stats


    print("\n1. 将收益率转换为资金曲线并保存到CSV:")
 
    initial_cash = cerebro.broker.startingcash
    cumulative_returns = (1 + returns).cumprod()
    portfolio_value = cumulative_returns * initial_cash

    output_df = pd.DataFrame({
        'Date': returns.index,
        'Portfolio_Value': portfolio_value.round(2),
        'Daily_Return': returns.round(6)
    })
    # 保存到CSV文件
    csv_filename = f'results/{stock_code}/{stock_code}_profit.csv'
    output_df.to_csv(csv_filename, index=False)
    print(f"   资金曲线数据已保存至: {csv_filename}")

    #保存交易明细到CSV
    print("\n2. 保存交易记录到CSV:")
    transactions['profit']=profit
    transactions['stock_code']=stock_code
    transactions.to_csv(f'results/{stock_code}/{stock_code}_transactions.csv', index=True)
 
def next_tradeday(date,tradeday):

    try:
        index=tradeday.index(date)+1
        return tradeday[index]
    except:
        print('out of  history day')

    pass
def get_tradeday():

    return read_tdxfile('000001').index.date.tolist()


if __name__=='__main__':
    
    trade_day=get_tradeday()
    print(next_tradeday(datetime.date(2024,8,16),trade_day))


