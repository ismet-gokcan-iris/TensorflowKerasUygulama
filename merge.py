import pandas as pd
import numpy as np


mergeSozluk={"isim":["ahmet","mehmet","zeynek","atil"],"spor":["koşu","yüzme","koşu","basketbol"]}

mergeDataFrame1=pd.DataFrame(mergeSozluk)


mergeSozluk2={"isim":["ahmet","mehmet","zeynek","atil"],"kalori":[100,200,350,700]}

mergeDataFrame2=pd.DataFrame(mergeSozluk2)


sonDataFrame=pd.merge(mergeDataFrame1,mergeDataFrame2,on="isim")

print(sonDataFrame)

maasSozluk = {"Isim": ["Atil","İsmet","Osman","Bilal"],
"Departman": ["Yazılım","Satış","Pazarlama","Yazılım"],
"Maas":[200,300,400,500]}

maasSozlukDataFrame=pd.DataFrame(maasSozluk)

print(maasSozlukDataFrame)

m=maasSozlukDataFrame["Departman"].unique()
print(m)

ö=maasSozlukDataFrame["Departman"].nunique()
print(ö)

ç=maasSozlukDataFrame["Departman"].value_counts()
print(ç)


def bruttenNete(maas):

    return maas * 0.66

z=maasSozlukDataFrame["Maas"].apply(bruttenNete)
print(z)

q=maasSozlukDataFrame.isnull()

print(q)

yeniBirVeri = {"Karakter Sınıfı":["South Park","South Park","Simpson","Simpson","Simpson"],
"Karakter Ismi":["Cartman","Kenny","Homer","Bart","Bart"],
"Karakter Yas":[20,10,50,70,70]}

yeniDataFrame=pd.DataFrame(yeniBirVeri)

print(yeniDataFrame)

ü=yeniDataFrame.pivot_table(values="Karakter Yas",index=["Karakter Sınıfı","Karakter Ismi"],aggfunc=np.sum)
print(ü)