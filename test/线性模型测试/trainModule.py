#import package 
import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
import toolFunction as toolFunction
#import data
new_train=pd.read_csv('./ex1data2.txt',encoding='utf-8')


X=new_train.iloc[:,:2]
mean,std,X=toolFunction.z_normal(X)
print(mean)
print(std)
print(X)
y=new_train.iloc[:,2]


model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
x=[1630,3]
x=(x-mean)/std
print(x)
y_pred=model.predict([x])
print(y_pred)





