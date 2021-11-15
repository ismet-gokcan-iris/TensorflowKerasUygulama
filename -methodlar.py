import numpy as np

list(range(0,10))

b=np.arange(0,10)
print(b)

t=np.arange(0,10,2)
print(t)

##zeros

y=np.zeros((5,5))
print(y)

p=np.ones((5,5))
print(p)

#linspace

q=np.linspace(0,20,50)
print(q)

##eye

v=np.eye(3)
print(v)

##random

x=np.random.randn(4,4)
print(x)

m=np.random.randint(1,20)
print(m)

n=np.random.randint(1,20,4)
print(n)

##numpy dizi methodları

benimNumpyDizim = np.arange(0,30)

benimRandomDizim=np.random.randint(1,200,50)

g=benimNumpyDizim.reshape(5,6)
print(g)

j=benimRandomDizim.reshape(5,10)
print(j)


l=benimRandomDizim.argmin()
print(l)

I=g.shape
print(I)