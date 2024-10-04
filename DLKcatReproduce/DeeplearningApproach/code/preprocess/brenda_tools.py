

def loop(func):
    print('loop start----------')
    for ecNumber in ecNumbers:
        response=func(ecNumber)
        print(ecNumber,field)
        response_to_txt(response,ecNumber,field)
    print('loop end-----------')