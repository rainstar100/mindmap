import backtrader as bt
import datetime
from tool import get_tradeday , next_tradeday

#generate trade dates
tradeday=get_tradeday()

class NewHighStrategy(bt.Strategy):
    params=(
        ('look_back_period',30),
        ('stake', 100),
        ('printlog', True),
        ('fixed_amount', 10000)
    )


    def log(self, txt, dt=None, doprint=False):
        '''日志函数'''
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.data.v90=bt.indicators.Highest(self.data.volume,period=90)
        self.data.h30=bt.indicators.Highest(self.data.close,period=30)
        self.data.ma5=bt.indicators.SimpleMovingAverage(self.data.close,period=5)
        self.signal_date=None
        self.order={'BUY':None,'SELL':None}

    def next(self):

        if len(self)<90:
            return
        if not self.signal_date:

            if self.data.high[-1]==self.data.h30[-1] and self.data.volume[-1]==self.data.v90[-1] and self.data.high[0]/self.data.close[-1]>=1.09:
                self.signal_date=self.data.datetime.date(0)
                print(f'{self.signal_date}-->Buy signal detected')
                buy_price = self.data.close[0]*1.09
                size = int(self.p.fixed_amount / buy_price/100)*100
                print(f'signal day price {self.data.close[0]}/// Placing buy stop order at {buy_price} for size {size}')
                validity=next_tradeday(self.data.datetime.date(0),tradeday)
                if self.order['BUY'] is None:
                    self.order['BUY']=self.buy(exectype=bt.Order.Stop,size=size,price=buy_price,valid=validity)
                if self.order['SELL'] is None:
                    self.order['SELL']=buy_order=self.sell(exectype=bt.Order.Stop,size=self.position.size,price=self.data.low[0]*0.99,valid=validity)
            else:
                #print(f'{self.data.datetime.date(0)}-->No buy signal')
                pass
        else:

            condition1=self.data.datetime.date(0)>self.signal_date and self.data.datetime.date(0)<=self.signal_date+datetime.timedelta(days=60)
            condition2=self.data.high[0]/self.data.h30[-1]>=1.09
                #print(condition1,condition2)
            if  condition1 and condition2:
                print(f'{self.data.datetime.date(0)}-->Add position signal detected')
                current_price = self.data.close[0]
                size = int(self.p.fixed_amount / current_price/100)*100
                #validity=self.data.datetime.date(0)+datetime.timedelta(days=1)
                validity=next_tradeday(self.data.datetime.date(0),tradeday)
                if self.order['BUY'] is None:
                    self.order['BUY']=self.buy(exectype=bt.Order.Stop,size=size,price=self.data.close[0]*1.09,valid=validity)
                if self.order['SELL'] is None:
                    self.order['SELL'] =self.sell(exectype=bt.Order.Stop,size=self.position.size,price=self.data.low[0]*0.99,valid=validity)
            elif self.data.datetime.date(0)>self.signal_date+datetime.timedelta(days=60):
                self.signal_date=[]


    def notify_order(self, order):


        if order in self.order.values():

            direction = 'BUY' if order.isbuy() else 'SELL'

            if order.status in [order.Submitted]:
  
                trade_info = (
                    f"{direction} Submitted | "
                    f"Price: {order.price} | "
                    f"Size: {order.size} | "
                    f"Cost: {order.valid} | "
                    f"Bar: {len(self)}"
                    )
                self.log(trade_info)

            
            elif order.status in [order.Accepted]:
  
                trade_info = (
                    f"{direction} Accepted | "
                    f"Price: {order.price} | "
                    f"Size: {order.size} | "
                    f"Cost: {order.valid} | "
                    f"Bar: {len(self)}"
                    )
                self.log(trade_info)


    
            elif order.status in [order.Completed]:
                direction = 'BUY' if order.isbuy() else 'SELL'
                trade_info = (
                    f"{direction} EXECUTED | "
                    f"Price: {order.executed.price:.4f} | "
                    f"Size: {order.executed.size} | "
                    f"Cost: {order.executed.value:.2f} | "
                    f"Comm: {order.executed.comm:.4f} | "
                    f"Bar: {len(self)}"
                )
                self.log(trade_info)
                self.order[direction]=None

        
            elif order.status == order.Canceled:
                self.log(f"Order Canceled - Ref:{order.ref}")
                self.order[direction]=None

        
            elif order.status == order.Margin:
                self.log("Order Margin")
                self.order[direction]=None

        
            elif order.status == order.Rejected:
                self.log(f"Order Rejected - Ref:{order.ref}")
                self.order[direction]=None

            elif order.status == order.Expired:

                trade_info = (
                    f"{direction} Expired| "
                    f"Price: {order.price} | "
                    f"Size: {order.size} | "
                    f"Cost: {order.valid} | "
                    f"Bar: {len(self)}"
                    )
                self.log(trade_info)
                self.order[direction]=None

   
