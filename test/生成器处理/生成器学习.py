

'''
节省内存，内存够的话，没有列表推到式快
'''

def file_generator():
    for i in [1,2,3,5,6]:
        yield i 

for file in file_generator(): 
    print(file)