def file_generator():
    for i in [1,2,3,5,6]:
        yield i 

for file in file_generator(): 
    print(file)