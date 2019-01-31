import numpy as np 
import matplotlib.pyplot as plt
from numpy import genfromtxt
tabel = genfromtxt('hydrostatics_table.csv',delimiter = ',')
tabel = tabel/1000
value = tabel[1:,1:]
stns = tabel[1:,0]
for i in range(0, value.shape[1]):
	print('wls no :', tabel[i+1][0])
	plt.plot(stns, value[0:,i])
plt.show()