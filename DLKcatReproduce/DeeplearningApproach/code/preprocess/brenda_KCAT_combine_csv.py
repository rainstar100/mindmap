import pandas as pd
import os

def combineFiles(input_path,output_path):
    '''
    combine dataframes into one file ,and save with csv.
    workflow:readfilename-combinefile-save
    input_path :files path before combine
    output_path:file path after combine for store.
    '''

    # #read file 
    # file_names = os.listdir(input_path)     #read all files name
    # files=[pd.read_csv(input_path+file_name,encoding='utf-8',header=1) for file_name in file_names[:4]]
    # print(f'got {len(files)} dataframe in list')
    # #combie file
    # df=pd.DataFrame()
    # df=[pd.concat([df,file]) for file in files if not file.empty]
    # # for file in files:
    # #     df=pd.concat([df,file]) 
    # print(f'the combined dataframe shape---->{df.shape}')
 
    #read all files name
    file_names = os.listdir(input_path)
    #read file with generator 
        

if __name__=='__main__':


    #inputpath
    input_path='./Data/database/brenda_csv/'
    output_path='./Data/database/combine/'
    combineFiles(input_path,output_path)