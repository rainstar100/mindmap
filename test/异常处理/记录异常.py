
'''
 I consider to crawl by asynchronous
#if occur error , the position can be recorded
        except:
            print('raise----',i)
            with open('log.txt','a') as f:
                f.write(str(i)+',\n')

'''
    

def crawl(i):

        try: 
                if i%2!=0:
                    print(i)
                elif i%2==0:
                    raise 
        except:
            print('raise----',i)
            with open('log.txt','a') as f:
                f.write(str(i)+',\n')


            
if __name__=='__main__':

    crawl(1)
    crawl(2)

