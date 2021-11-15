import numpy as np
import pandas as pd


sozlukVerisi= {"istanbul": [30,29,np.nan],"ankara":[20,np.nan,25],"izmir":[40,39,38]}
havaDurumuDataFrame=pd.DataFrame(sozlukVerisi)

print(havaDurumuDataFrame)

a=havaDurumuDataFrame.dropna()
print(a)

b=havaDurumuDataFrame.dropna(axis=1)
print(b)

yeniDataFrame=pd.DataFrame({"istanbul": [30,29,np.nan],"ankara":[20,np.nan,25],"izmir":[40,39,38],"antalya":[35,np.nan,np.nan]})

print(yeniDataFrame)

x=yeniDataFrame.dropna(axis=1,thresh=2)
print(x)

v=yeniDataFrame.fillna(20)
print(v)

