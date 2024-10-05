if __name__=='__main__':

    error_type=3

    try:
        if error_type==1:

            raise ValueError('raise1')  # raise python buidin error

        if error_type==2:

            raise KeyError('no key')
        if error_type==3:

            raise BufferError('overflow')
    
    except Exception as e:
        print(e)
        print('continue--------')