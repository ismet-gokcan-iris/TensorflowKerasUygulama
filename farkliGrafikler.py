import numpy as np
import matplotlib.pyplot as plt

numpyDizisi = np.linspace(0,10,20)

numpyDizisi2=numpyDizisi**2


plt.scatter(numpyDizisi,numpyDizisi2)

plt.show()


a=np.random.randint(0,100,50)


plt.hist(a)
plt.show()


plt.boxplot(a)
plt.show()
