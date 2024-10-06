import multiprocessing
import os 
import time
#difine task
def square_number(n,queue):  #queue for restore function results
    print(f"Process ID: {os.getpid()}, Number: {n}, Square: {n**2}") 
    queue.put(n**2)

# start process in __main__
if __name__=='__main__':

    #create queue for receiving return value
    queue=multiprocessing.Queue()
    #create a process ,initial process
    # have own python interpreter who has itsself cpu mennery == an new interpreter.
    process1=multiprocessing.Process(target=square_number,args=(2,queue))
    # start process, subprocess must be in main process.
    process1.start()
    # waiting for process until process finished
    process1.join()  
    # close process
    process1.close()#release and clean process resource
    # process stopped still have some resource
    print(f'the result({queue.get()})is in queue')
    print("All processes have finished execution.")