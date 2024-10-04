import requests
from tools.parallel import parallel
from tools.decorator import timetry
from tools.tool import devideIterator
import numpy as np
import pandas as pd
from brenda_crawl_parallel import crawl


#set path of input and output
input_path='./data/database/brenda_raw/'
#read ecNumbers

def eclist():
    #read ecNumbers
    df=pd.read_csv(input_path+'brenda_ecNumbers.csv')
    return df

if __name__ == '__main__' :
    #parallel request

    allEC = eclist() #all params
    params_pool=devideIterator(allEC.iloc[2372:,0],20)

    for params in params_pool:
        parallel(crawl,params)
