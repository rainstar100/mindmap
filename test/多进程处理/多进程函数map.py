import multiprocessing
import os 
def parallel_multiprocess_map(func,params,number_processes):
    '''
    func :task 
    params: params of task
    pool_size: also mean the numbers of process in pool
    number_processes: number of processes in pool
    '''
    #create the pool and intial processes
    pool=multiprocessing.Pool(number_processes)
        
    #assign task to process in pool
    pool.map(func,params)

    #close pool and cant submit tasks to pool
    pool.close()
    #wait until all subprocesses finish
    pool.join()

#difine task
def square_number(n):  
    print(f"Process ID: {os.getpid()}, Number: {n}, Square: {n**2}") 

if __name__=='__main__':

    parallel_multiprocess_map(square_number,[1,2,3,4,5,6,7,8,9,10],4)


'''
函数定以在主进程内，否则子进程找不到，子进程应该在新的解释器里，重新执行该模块，所以函数应该定义在模块内。
'''
