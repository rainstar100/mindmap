
#有异常的函数，开多线程

import threading
import time
import numpy as np

#异常处理装饰器
def mytry(func):

    def wrapper(*args, **kwargs): 
        try:
            result=func(*args, **kwargs)
            return result
        except:
            string_raise='raise----'+str(args[0])+'\n'
            print('raise----',*args,'\n')
            with open('./log.txt','a') as f:
                f.write(str(*args)+',\n')
            #发生错误后，可以返回值，也可以不返回值

    return wrapper

##模拟爬取，如果发生异常则记录到log
@mytry
def crawl(i):

    if i%2!=0:
        string='I am '+str(i)+'-single number, no raise\n'
        print(string)
        return i*10
    elif i%2==0:
        raise ValueError('raise')  # raise python buidin error

#thread 函数
def parallel(func,params):
    #Asynchronous running function
    threads = []
    # 为每个URL创建一个线程
    for param in params:
        thread = threading.Thread(target=func, args=(param,))
        threads.append(thread)
        thread.start()
    # 等待所有线程完成
    for thread in threads:
        thread.join()


def main():
    params = np.arange(0,1000) #线程数量
    parallel(crawl,params)

    print("所有页面标题抓取完成!")


if __name__ == '__main__':
    main()
