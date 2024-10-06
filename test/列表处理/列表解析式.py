a=[1,2,3]
b=[i**2 for i in a] #返回一个列表（元素是对源列表元素的处理结果），类似与导致语句，前面是表达式/循环体，后面是for循环头 ,就是对元素都进行一个操作
def cub(i):
    return i*i*i
c=map(cub,a) # 对列表中的元素操作后，返回一个迭代对象，而不是一个列表
print(b)
for i in c:
    print(i)

