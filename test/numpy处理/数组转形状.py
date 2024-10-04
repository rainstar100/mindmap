

a=range(153)


def devideIterator(object,length):
    params=[]
    temp=[]
    index=0
    for item in object:
        temp.append(item)
        if (index+1)%length==0:
            params.append(temp)
            temp=[]
        index=index+1
    params.append(temp)  
    return params

params=devideIterator(a,10)

    

print(params)