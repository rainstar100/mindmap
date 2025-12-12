import backtrader as bt
import datetime

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
        self.order=None

    def next(self):

        if len(self)<90:
            return
        #print(f'Processing date: {self.data.datetime.date(0)}')

        #if (not self.position)  :
        if not self.signal_date:

            if  self.order:
                return

            if self.data.high[-1]==self.data.h30[-1] and self.data.volume[-1]==self.data.v90[-1] and self.data.high[0]/self.data.close[-1]>=1.09:
                self.signal_date=self.data.datetime.date(0)
                print(f'{self.signal_date}-->Buy signal detected')
                buy_price = self.data.close[0]*1.09
                size = int(self.p.fixed_amount / buy_price/100)*100
                print(f'signal day price {self.data.close[0]}/// Placing buy stop order at {buy_price} for size {size}')
                validity=self.data.datetime.date(0)+datetime.timedelta(days=5)
                self.order=self.buy(exectype=bt.Order.Stop,size=size,price=buy_price,valid=validity)
                #self.buy()
            else:
                #print(f'{self.data.datetime.date(0)}-->No buy signal')
                pass
        else:
            #if self.data.close[-1]<self.data.ma5[-1] and self.data.close[0]<self.data.ma5[0] :
            if self.data.close[0]<self.data.h30[0]:
                self.order=self.sell(exectype=bt.Order.Market,size=self.position.size)
            
            else:
                if  self.order:
                    return
                condition1=self.data.datetime.date(0)>self.signal_date and self.data.datetime.date(0)<=self.signal_date+datetime.timedelta(days=60)
                condition2=self.data.high[0]/self.data.h30[-1]>=1.09
                #print(condition1,condition2)
                if  condition1 and condition2:
                    print(f'{self.data.datetime.date(0)}-->Add position signal detected')
                    current_price = self.data.close[0]
                    size = int(self.p.fixed_amount / current_price/100)*100
                    validity=self.data.datetime.date(0)+datetime.timedelta(days=5)
                    self.order=self.buy(exectype=bt.Order.Stop,size=size,price=self.data.close[0]*1.09,valid=validity)
                elif self.data.datetime.date(0)>self.signal_date+datetime.timedelta(days=60):
                    self.signal_date=None


    def notify_order(self, order):


        if order==self.order:

            if order.status in [order.Submitted, order.Accepted]:
                direction = 'BUY' if order.isbuy() else 'SELL'
                
                trade_info = (
                    f"{direction} Accepted | "
                    f"Price: {order.price} | "
                    f"Size: {order.size} | "
                    f"Cost: {order.valid} | "
                    f"Bar: {len(self)}"
                    )
                self.log(trade_info)

    
            if order.status in [order.Completed]:
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
                self.order=None

        
            elif order.status == order.Canceled:
                self.log(f"Order Canceled - Ref:{order.ref}")
                self.order=None

        
            elif order.status == order.Margin:
                self.log("Order Margin")
                self.order=None

        
            elif order.status == order.Rejected:
                self.log(f"Order Rejected - Ref:{order.ref}")
                self.order=None
            elif order.status == order.Expired:
                self.log(f"Order Valid - Ref:{order.ref}")
                self.order=None

   
