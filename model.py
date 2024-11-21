# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SVygm-Fi0KxiA7EE1f8debEZlI__BzAi
"""
#importing necessary libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

#loading the dataset
df=pd.read_csv("/content/sample_data/Quarterly_Retail_Sales_Tax_Data_by_County_and_City.csv")
print(df)

# to see the general overview of the data
df.shape
df.info()
df.describe(include='O')
df.duplicated()
df.isnull().sum()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df[""]=le.fit_transform("")

X=df.drop("",axis=1)
y=df[""]

# to change the categorical variable into binary[0,1]
categorical_features=["","",""]

one_hot=OneHotEncoder()
transformer=ColumnTransformer([('one_hot',one_hot,categorical_features)],
                              remainder='passthrough')
transformed_X=transformer.fit_transform.transformer()
print(transformed_X)
pd.DataFrame(transformed_X)

# to split variables into training and testing sets[80% train, 20% test]

X_train,y_train,X_test,y_test=train_test_split(transformed_X,
							y,test_size=0.2)
#fitting linear regression 
lr=LinearRegression()

y_lr=lr.fit(X_train,y_train)

y_lr_train_pred=lr_predict(X_train)
y_lr_test_pred=lr_predict(X_test)

print(y_lr_train_pred)
print(y_lr_test_pred)
#evaluation of the linear regression performance[mean squared errors and r2 scores compared]
lr_train_mse=mean_squared_error(y_train,y_lr_train_pred)
lr_test_mse=mean_squared_error(y_test,y_lr_test_pred)

lr_train_r2=r2_score(y_train,y_lr_train_pred)
lr_test_r2=r2_score(y_test,y_lr_test_pred)

print(lr_train_mse)
print(lr_test_mse)
print(lr_train_r2)
print(lr_test_r2)

lr_result=pd.DataFrame(["LinearRegression","lr_train_mse","lr_test_mse",
                        "lr_train_r2","lr_test_r2"]).Transpose()
lr_result.columns=["method","training mse","training r2","test mse","test r2"]

print(lr_result)
