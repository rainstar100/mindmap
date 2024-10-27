import json
import pandas as pd
with open('./json处理/output.json', 'r', encoding='utf-8') as file:  
    dj=json.load(file)
print(dj)
df=pd.read_json('./json处理/output.json', encoding='utf-8')
print(df)

'''
用json记录数据集，下面2中格式
1.数组[元素，元素]，元素可以任务，有序，与python列表对应
2.对象{key:vlue}, value 可以是字典，与python字典对应

'''