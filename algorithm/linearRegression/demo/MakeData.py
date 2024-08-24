# get original data 
import pandas as pd
OriginalData_train=pd.read_csv('../housePrice/data_train.csv',encoding='gbk')
# filter out param of non-number
new_train= OriginalData_train.select_dtypes(include=['int64', 'float64'])
# save to csv
new_train.to_csv('./new_train.csv',encoding='utf-8',index=False)

#handle test data by the same method as train data
OriginalData_test=pd.read_csv('../housePrice/data_test.csv',encoding='gbk')
new_test= OriginalData_train.select_dtypes(include=['int64', 'float64'])
new_test.to_csv('./new_test.csv',encoding='utf-8',index=False)
