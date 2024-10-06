import multiprocessing
import os 
import time
#difine task
def square_number(n):  
    print(f"Process ID: {os.getpid()}, Number: {n}, Square: {n**2}") 
    # time.sleep(30)

# start process in __main__
if __name__=='__main__':

    #create a process ,initial process
    # have own python interpreter who has itsself cpu mennery == an new interpreter.
    process1=multiprocessing.Process(target=square_number,args=(2,))
    # process2=multiprocessing.Process(target=square_number,args=(3,))
    # process3=multiprocessing.Process(target=square_number,args=(4,))
    # start process, subprocess must be in main process.
    process1.start()
    # process2.start()
    # process3.start()
    # waiting for process until process finished
    process1.join()  
    # close process
    process1.close()#release and clean process resource
    # process stopped still have some resource

    print("All processes have finished execution.")