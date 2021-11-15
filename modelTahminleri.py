# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 15:05:34 2021

@author: ismet
"""


import pandas as pd
data1 = pd.read_excel("bisiklet_fiyatlari.xlsx")
print(data1)

a=data1.head()
print(a)

import seaborn as sbn

import matplotlib.pyplot as plt





from sklearn.model_selection import train_test_split


y=data1["Fiyat"].values
print(y)

x=data1[["BisikletOzellik1","BisikletOzellik2"]].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=15)

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()

scaler.fit(x_train)

X_train=scaler.transform(x_train)
X_test=scaler.transform(x_test)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model=Sequential()

model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))

model.add(Dense(1))
          
model.compile(optimizer="rmsprop",loss="mse")
model.fit(X_train,y_train,epochs=250)

loss=model.history.history["loss"]


sbn.lineplot(x=range(len(loss)),y=loss)
plt.show()
sbn.pairplot(data1)

plt.show()

trainLoss=model.evaluate(X_train,y_train,verbose=0)

tstLoss=model.evaluate(X_test,y_test,verbose=0)

testTahminleri=model.predict(X_test)
testTahminleri.shape



testTahminleri=pd.Series(testTahminleri.reshape(330,))



tahminDf=pd.DataFrame(y_test,columns=["gerçek y"])


tahminDf=pd.concat([tahminDf,testTahminleri],axis=1)

tahminDf.columns=["gerçek y","tahmin y"]

sbn.scatterplot(x="gerçek y",y="tahmin y" , data =tahminDf)

from sklearn.metrics import mean_absolute_error, mean_squared_error

a=mean_absolute_error(tahminDf["gerçek y"],tahminDf["tahmin y"])

ö=data1.describe()

yeniBisikletOzellikleri = [[1760,1758]]
yeniBisikletOzellikleri=scaler.transform(yeniBisikletOzellikleri)
ç=model.predict(yeniBisikletOzellikleri)

from tensorflow.keras.models import load_model
model.save("bisiklet_modeli.h5")





