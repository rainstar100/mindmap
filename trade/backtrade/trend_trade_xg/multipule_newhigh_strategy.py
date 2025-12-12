import backtrader as bt
import datetime

class MultipuleNewHighStrategy(bt.Strategy):
    params=(
        ('look_back_period',90),
        ('stake', 100),
        ('printlog', True),
        ('fixed_amount', 10000)
    )



    def __init__(self):
        self.signal_dates={}
        self.orders={}
        self.h30={}
        self.v90={}
        self.ma5={}

        for data in self.datas:
            stock_code=data._name
            self.signal_dates[stock_code]=None
            self.orders[stock_code]=None
            self.h30[stock_code]=bt.indicators.Highest(data.high,period=30)
            self.v90[stock_code]=bt.indicators.Highest(data.volume,period=90)
            self.ma5[stock_code]=bt.indicators.SimpleMovingAverage(data.close,period=5)


    def next(self):

        if len(self)<90:
            return

        for  data in self.datas:
            stock_code=data._name

            if (not self.getposition(data))  :

                if  self.orders[stock_code]:
                    return
                if data.high[-1]==self.h30[stock_code][-1] and data.volume[-1]==self.v90[stock_code][-1] and data.high[0]/data.close[-1]>=1.09:   
                    self.signal_dates[stock_code]=data.datetime.date(0)
                    print(f'{stock_code} of {self.signal_dates[stock_code]}-->Buy signal detected')
                    current_price = data.close[0]
                    size = int(self.p.fixed_amount / current_price/100)*100
                    days=data.datetime.date(0)+datetime.timedelta(days=5)
                    self.orders[stock_code]=self.buy(data=data,exectype=bt.Order.Stop,size=size,price=data.close[0]*1.09,valid=days)
                    #self.buy()
                else:
                    #print(f'{data[stock_code].datetime.date(0)}-->No buy signal')
                    pass
            else:

                # if  self.orders[stock_code]:
                #     return    
                #sell
                if data.close[-1]<self.ma5[stock_code][-1] and data.close[0]<self.ma5[stock_code][0] :
                    self.orders[stock_code]=self.sell(data=data,exectype=bt.Order.Market,size=self.getposition(data).size)
                
                else:
                #add
                    if  self.orders[stock_code]:
                        return                  
                    condition1=data.datetime.date(0)>self.signal_dates[stock_code] and data.datetime.date(0)<=self.signal_dates[stock_code]+datetime.timedelta(days=30)
                    condition2=data.high[0]/self.h30[stock_code][-1]>=1.09
                    #print(condition1,condition2)
                    if  condition1 and condition2:
                        print(f'{stock_code} of {data.datetime.date(0)}-->Add position signal detected')
                        current_price = data.close[0]
                        size = int(self.p.fixed_amount / current_price/100)*100
                        days=data.datetime.date(0)+datetime.timedelta(days=5)
                        self.orders[stock_code]=self.buy(data=data,exectype=bt.Order.Stop,size=size,price=data.close[0]*1.09,valid=days)
                    else:
                        pass


    def notify_order(self, order):

        for stock_code ,tracked_order in self.orders.items():

            if order==tracked_order:

                if order.status in [order.Submitted, order.Accepted]:
                    direction = 'BUY' if order.isbuy() else 'SELL'
                    trade_info = (
                        f"{bt.num2date(order.created.dt)}| "
                        f"{stock_code}| "
                        f"{direction} Accepted | "
                        f"Bar: {len(self)}"
                    )
                    print(trade_info)

                if order.status in [order.Completed]:
                    direction = 'BUY' if order.isbuy() else 'SELL'
                
                    trade_info = (
                        f"{bt.num2date(order.executed.dt)}| "
                        f"{stock_code}| "
                        f"{direction} EXECUTED | "
                        f"Price: {order.executed.price:.4f} | "
                        f"Size: {order.executed.size} | "
                        f"Cost: {order.executed.value:.2f} | "
                        f"Comm: {order.executed.comm:.4f} | "
                        f"Bar: {len(self)}"
                    )
                    
                    print(trade_info)
                    self.orders[stock_code]=None
            
                elif order.status == order.Canceled:
                    print(f"Order Canceled - Ref:{order.ref}")
                    self.orders[stock_code]=None

            
                elif order.status == order.Margin:
                    print("Order Margin")
                    self.orders[stock_code]=None

            
                elif order.status == order.Rejected:
                    print(f"Order Rejected - Ref:{order.ref}")
                    self.orders[stock_code]=None
                elif order.status == order.Expired:
                    print(f"Order Expired - Ref:{order.ref}")
                    self.orders[stock_code]=None

   
