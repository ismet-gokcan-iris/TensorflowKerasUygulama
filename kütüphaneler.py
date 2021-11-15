import numpy
import matplotlib.pyplot as matplot


maasListesi = numpy.random.normal(4000,500,1000)
a= numpy.mean(maasListesi)
print(a)

matplot.hist(maasListesi,50)
matplot.show()

