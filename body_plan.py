import numpy as np 
import matplotlib.pyplot as plt
from numpy import genfromtxt
tabel = genfromtxt('hydrostatics_table.csv',delimiter = ',')
tabel = tabel/1000
value = tabel[1:,1:]
w_lines = tabel[0,1:]
for i in range(0, value.shape[0]):
	print('stn no :', tabel[i+1][0]*1000)
	if(i < value.shape[0]/2):
		value[i] = -1*value[i]
	plt.plot(value[i], w_lines)
plt.show()