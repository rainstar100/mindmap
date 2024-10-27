<<<<<<< HEAD


'''
节省内存，内存够的话，没有列表推到式快
'''

=======
import time
>>>>>>> DLKcat-reproduce
def file_generator():
    for i in [1,2,3,5,6]:
        yield i
        print(i+2)

iterator=iter(file_generator())
print(next(iterator))


for file in file_generator(): 
    print(file,'do things about 1s')
    time.sleep(2)
