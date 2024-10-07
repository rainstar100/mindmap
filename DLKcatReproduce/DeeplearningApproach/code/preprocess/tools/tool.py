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
    if temp:
        params.append(temp)  
    return params

def response_to_txt(file_name,response):
    print(file_name)
    with open(file_name, 'w',encoding='utf-8') as f: 
        f.write(response.text)
    print('saved')

if __name__=='__main__':
    #test devideIteratro
    a=devideIterator([1,2],1)
    print(a)