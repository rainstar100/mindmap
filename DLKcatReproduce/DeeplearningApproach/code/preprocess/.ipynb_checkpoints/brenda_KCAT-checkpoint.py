#import package 
import pandas as pd
from brenda_crawl import crawl
from brenda_tools import response_to_txt

#set path of input and output
input_path='../../data/database/brenda_raw/'
output_path='../../data/database/brenda_raw/KCAT/'

#read ecNumbers
df=pd.read_csv(input_path+'brenda_ecNumbers.csv')

## crawl and save
for ecNumber in df.iloc[1533:,0]:
    response=crawl(params = {'ecno':ecNumber,})
    file_name = output_path+'EC' + ecNumber+ '_KCAT' +'.txt'
    response_to_txt(file_name,response)


