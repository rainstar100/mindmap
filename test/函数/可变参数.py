def func(*args): # *args 可变参数,将参数打包成元组
    print(args)
    print('-'*20)
    print(*args) #将元组解包

func(1,2,3) # (1, 2, 3) args=(1, 2, 3)