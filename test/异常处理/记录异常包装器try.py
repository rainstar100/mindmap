'''
把他写成包装器，当异常的时候可以记录异常位置
'''

def mytry(func):

    def wrapper(*args, **kwargs): 
        try:
            result=func(*args, **kwargs)
            return result
        except:
            print('raise----',*args)
            with open('log.txt','a') as f:
                f.write(str(*args)+',\n')
            #发生错误后，可以返回值，也可以不返回值

    return wrapper

@mytry
##模拟爬取，如果发生异常则记录到log
def crawl(i):

    if i%2!=0:
        print(i)
        return i*10
    elif i%2==0:
        raise ValueError('raise')  # raise python buidin error

            

if __name__=='__main__':

    print(crawl(3))
    print(crawl(4))
    print(crawl(5))
    print(crawl(6))
    print('done')

