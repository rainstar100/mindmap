'''
clean  the raw data from brenda website  which in KCAT file
'''
import os
from bs4 import BeautifulSoup
import re
import pandas as pd
from tools.multiprocess import parallel_multiprocess_map
from tools.decorator import timetry






#clean data
#@timetry
def cleanFile(file_name):
    '''
    read-clean-save
    '''
    # set path 
    input_path='./Data/database/brenda_raw/KCAT/'
    output_path='./Data/database/brenda_csv/'
    #read file
    file=input_path+file_name #set filepath
    with open(file,'r',encoding='utf-8') as f:
        raw_data=f.read()
        print(len(raw_data))
    #clean file
    soup = BeautifulSoup(raw_data, 'lxml')
    tags=soup.find_all('div',id=re.compile("^(tab44_head|tab44r)"))
    data_list=[]
    for tag in tags:
        row=tag.get_text().split('\n')
        #print(row)
        if len(row)==9 and row[4]!='-' and row[4]!='UNIPROT':
            data_list.append(row)
        else:
            #print('delete')
            pass
    #save data
    df=pd.DataFrame(data_list)
    outfile=output_path+file_name[:-3]+'csv'
    df.to_csv(outfile,encoding='utf-8',index=False)
    print('saved')
          
    return data_list


if __name__=='__main__':

    #read the raw data 
    ##Read all BRENDA file names:
    file_names = os.listdir(input_path)
    #cleanFile(file_names)
    number_processes=10
    parallel_multiprocess_map(cleanFile,file_names,number_processes)  #munipuleprocess to cleanHtml
    