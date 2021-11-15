from matplotlib import figure
import matplotlib.pyplot as plt
import numpy as np

yasListesi = [20,30,50,70,45,65,55,70,33,50]
kiloListesi = [66,75,98,87,80,90,97,60,78,88]

numpyYasListesi=np.array(yasListesi)
numpyKiloListesi=np.array(kiloListesi)


plt.xlabel("Yas")
plt.ylabel("kilo")

plt.plot(numpyYasListesi,numpyKiloListesi,"g")



numpyDizisi1=np.linspace(0,10,20)
numpyDizisi2=numpyDizisi1**3

plt.subplot(1,2,1)
plt.plot(numpyDizisi1,numpyDizisi2,"r*-")
plt.subplot(1,2,2)
plt.plot(numpyDizisi2,numpyDizisi1,"g--")
plt.show()

benimFigure = plt.figure()

figureAxes=benimFigure.add_axes([0.1,0.1,0.3,0.3])
figureAxes=plt.plot(numpyDizisi1,numpyDizisi2,"g")

plt.show()

figure2=plt.figure()

eksen1=figure2.add_axes([0.1,0.1,0.7,0.7])
eksen2=figure2.add_axes([0.2,0.4,0.3,0.3])

eksen1.plot(numpyDizisi1,numpyDizisi2,"g")
eksen1.set_xlabel("x ekseni")
eksen1.set_ylabel("y ekseni")
eksen1.set_title("ana grafik")
eksen2.plot(numpyDizisi2,numpyDizisi1,"r")
eksen2.set_xlabel("x ekseni")
eksen2.set_ylabel("y ekseni")
eksen2.set_title("küçük grafik")

plt.show()

plt.subplot()

plt.show()

(benimFigure,benimEksenler)=plt.subplots(nrows=1,ncols=2)

for eksen in benimEksenler:
    eksen.plot(numpyDizisi1,numpyDizisi2,"g")
    eksen.set_xlabel("x ekseni")
plt.tight_layout()
plt.show()

yeniFigur=plt.figure()
yeniEksen=yeniFigur.add_axes([0.1,0.1,0.8,0.8])
yeniEksen.plot(numpyDizisi1,numpyDizisi1**2,label="numpyDizisi**2")
yeniEksen.plot(numpyDizisi1,numpyDizisi1**3,label="numpyDizisi**3")
yeniEksen.legend()
plt.show()

yeniFigur.savefig("benimFigur.png",dpi=200)








