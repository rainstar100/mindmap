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
        ('fixed_amount', 100000),
        ('monitor_period', 60)
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
        self.monitor_startdate=None
        self.monitor_enddate=None

        self.order={'BUY':None,'SELL':None}

    def next(self):

        if len(self)<90:
            return
        #generate order validity date
        validity=next_tradeday(self.data.datetime.date(0),tradeday)
        current_date=self.data.datetime.date(0)

        #place sell order first
        if self.position.size>0:
            sell_price=max(self.data.ma5[0],self.data.low[0])
            self.order['SELL']=self.sell(exectype=bt.Order.Stop,size=self.position.size,price=sell_price,valid=validity)
        
        ##generate buy signal
        ###check monitor start date if none
        #----->if monitor sart date is None ,check condition to set monitor start date
        if self.monitor_startdate is None:
            #set monitor start condition
            monitor_start_condition=self.data.high[-1]==self.data.h30[-1] and self.data.volume[-1]==self.data.v90[-1]
            #check monitor start codition
            if monitor_start_condition:
                #set monitor start date and end date
                self.monitor_startdate=self.data.datetime.date(-1)
                self.monitor_enddate=self.monitor_startdate+datetime.timedelta(days=60)
                print(f'{self.monitor_startdate}-->monitor signal detected, start monitoring period')
        #----->if monitor sart date not None, skip set and check monitor period
        if self.monitor_startdate:
            #check monitor period
            #----->if within monitor period, check for new high signal
            if current_date<=self.monitor_enddate:
 
                #new high--->buy
                if  self.data.high[0]/self.data.h30[-1]>=1.09:
                    print(f'{self.data.datetime.date(0)}-->Buy signal detected')
                    buy_price = self.data.close[0]*1.01
                    size = int(self.p.fixed_amount / buy_price/100)*100
                    if self.order['BUY'] is None:
                        self.order['BUY']=self.buy(exectype=bt.Order.Stop,size=size,price=buy_price,valid=validity)  
                #----->else, continue monitoring
                else:
                    #No new high detected during monitoring period
                    pass
            #----->if beyond monitor period, end monitoring  and reset monitor dates to None       
            else:
                #end monitoring period
                self.monitor_startdate=None
                self.monitor_enddate=None
                print(f'{current_date}-->end monitor')
    def notify_order(self, order):


        if order in self.order.values():

            direction = 'BUY' if order.isbuy() else 'SELL'

            if order.status in [order.Submitted]:
  
                trade_info = (
                    f"{direction} Submitted | "
                    f"Number: {order.ref} | "
                    f"Price: {order.price} | "
                    f"Size: {order.size} | "
                    f"Cost: {order.valid} | "
                    f"Bar: {len(self)}"
                    )
                self.log(trade_info)

            
            elif order.status in [order.Accepted]:
  
                trade_info = (
                    f"{direction} Accepted | "
                    f"Number: {order.ref} | "
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
                    f"Number: {order.ref} | "
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
                    f"Number: {order.ref} | "
                    f"Price: {order.price} | "
                    f"Size: {order.size} | "
                    f"Cost: {order.valid} | "
                    f"Bar: {len(self)}"
                    )
                self.log(trade_info)
                self.order[direction]=None

   
