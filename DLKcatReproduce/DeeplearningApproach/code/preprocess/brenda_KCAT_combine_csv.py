import pandas as pd
import os
from tools.decorator import timetry

@timetry
def combineFiles_generator(input_path,output_path):
    '''
    combine dataframes into one file ,and save with csv.
    workflow:readfilename-combinefile-save
    input_path :files path before combine
    output_path:file path after combine for store.
    '''
    #read all files name
    file_names = os.listdir(input_path)
    #read file into generator
    def file_generator():
        for file_name in file_names:
            print(f'read---->{file_name}')
            yield pd.read_csv(input_path+file_name,encoding='utf-8',header=1)
    #combine file to df
    df=pd.DataFrame()
    for file in file_generator():
        if not file.empty:
            df=pd.concat([df,file]) 
        print(f'shape-->{df.shape}')
    print(f'the combined dataframe shape---->{df.shape}')  


@timetry
def combineFiles_listInterpretor(input_path,output_path):
    '''
    combine dataframes into one file ,and save with csv.
    workflow:readfilename-combinefile-save
    input_path :files path before combine
    output_path:file path after combine for store.
    '''
    #read all files name
    file_names = os.listdir(input_path)
    #read file into list with interpretor
    files=[pd.read_csv(input_path+file_name,encoding='utf-8',header=1) for file_name in file_names]
    #combine file to df
    df=pd.DataFrame()
    for file in files:
        if not file.empty:
            df=pd.concat([df,file]) 
        print(f'shape-->{df.shape}')
    print(f'the combined dataframe shape---->{df.shape}')  



if __name__=='__main__':


    #inputpath
    input_path='./Data/database/brenda_csv/'
    output_path='./Data/database/combine/'
    combineFiles_listInterpretor(input_path,output_path)