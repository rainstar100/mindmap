############################################################
import time
from datetime import datetime
def timetry(func):  
    def wrapper(*args, **kwargs):  
        start_time = time.time()  # 记录开始时间  
        succes=0
        while succes<100:
            try:
                start_time = time.time()  # 记录开始时间  
                result = func(*args, **kwargs)  # 执行函数  
                end_time = time.time()  # 记录结束时间  
                execution_time = end_time - start_time  # 计算执行时间  
                print(f"Function {func.__name__} executed in {execution_time:.4f} seconds")    
                return result  # 返回函数的结果  
            except:
                #raise
                with open('./log/log.txt','a') as f:
                    f.write(str(*args)+','+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n')
                time.sleep(1)
                succes += 1
                print('try',succes)
    return wrapper  
########################################################