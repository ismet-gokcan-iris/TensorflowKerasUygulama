import numpy as np
matrixDizisi =[[10,20,30],[20,30,40],[50,60,70]]

benimMatrixDizim=np.array(matrixDizisi)

a=benimMatrixDizim[1][2]
print(a)
b=benimMatrixDizim[1:,2]
print(b)

c= benimMatrixDizim[2:,2:]
print(c)


yeniListe=[[10,20,30],[40,50,60],[70,80,90],[80,50,40],[90,50,20],[25,45,55]]

yeniMatrix=np.array(yeniListe)


t=yeniMatrix[[4,2,0]]
print(t)