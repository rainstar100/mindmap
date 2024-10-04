
#args解包后是元组
def params(*args,**kwargs):
    
    print(args)
    print(type(args[0]))
    print(str(args[0]))

params(1)

print('done')