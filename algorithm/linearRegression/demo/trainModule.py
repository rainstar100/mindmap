#import package 
import pandas as pd
import numpy as np
import toolFunction
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
#import data
new_train=pd.read_csv('./new_train.csv',encoding='utf-8')

#filter out the columns with na
new_train=new_train.dropna(axis=1,how='any')



X=new_train.iloc[:,1:-1]
mean,std,X=toolFunction.z_normal(X)
print(X)
y=new_train.iloc[:,-1]


model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)

diff=np.average((model.predict(X)-y)/y)
print(diff)











