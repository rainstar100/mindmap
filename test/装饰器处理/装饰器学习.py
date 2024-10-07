def decorator(func):
    def wrapper(*args,**kwargs):

        result=func(*args,**kwargs) #返回func调用执行后的结果 to result
        result=result*2 #wrapper 处理func返回值
        return result
    return wrapper  #返回的是wrapper调用执行后的结果===return wrapper(add(1,2))

@decorator
def add(a,b):
   return a+b

if __name__=='__main__':

    print(add(1,2))#===wrapper(add(1,2))
