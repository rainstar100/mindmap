def response_to_txt(file_name,response):
    print(file_name)
    with open(file_name, 'w',encoding='utf-8') as f: 
        f.write(response.text)
    print('saved')

def loop(func):
    print('loop start----------')
    for ecNumber in ecNumbers:
        response=func(ecNumber)
        print(ecNumber,field)
        response_to_txt(response,ecNumber,field)
    print('loop end-----------')