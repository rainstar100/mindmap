import threading

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
###################################
print("import successfully---",id(parallel))