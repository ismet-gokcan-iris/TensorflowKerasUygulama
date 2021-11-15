import numpy as np
import matplotlib.pyplot as plt

numpyDizisi = np.linspace(0,10,20)

numpyDizisi2=numpyDizisi**2

(benimFigur,benimEksen)=plt.subplots()


benimEksen.plot(numpyDizisi,numpyDizisi2,color="#3A95A8",alpha=0.9,linewidth=1.0,linestyle="--",marker="o",markersize=4,markerfacecolor="r")
benimEksen.plot(numpyDizisi2,numpyDizisi,"r")


plt.show()