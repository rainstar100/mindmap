import time 
from datetime import datetime
print(datetime.now()) #日期时间
print(time.time())# 自19700101以来的秒数

str='aa'+datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(str)