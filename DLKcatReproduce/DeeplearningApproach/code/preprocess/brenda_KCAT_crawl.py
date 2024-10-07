import requests
from tools.parallel import parallel
from tools.decorator import timetry
from tools.tool import devideIterator
import numpy as np
import pandas as pd
from brenda_crawl_func import crawl


#set path of input and output
input_path='./data/database/brenda_raw/'
#read ecNumbers

def eclist():
    #read ecNumbers
    df=pd.read_csv(input_path+'brenda_ecNumbers.csv')
    return df.iloc[:,0] #slice on ecNumbers

if __name__ == '__main__' :
    #parallel request

    allEC = eclist()[3249:]#all params  if test ,please slice 4-10 ecNumbers
    Maxnumber_threads=20 # the max number of threads at one time 
    params_pool=devideIterator(allEC,Maxnumber_threads)

    for params in params_pool:
        parallel(crawl,params)
