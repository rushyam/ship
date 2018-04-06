import numpy as np 
import matplotlib.pyplot as plt
from numpy import genfromtxt
from simpson import *

tabel = genfromtxt('hydrostatics_table.csv',delimiter = ',')
area_stns = tabel[0:,0:14]
tabel = tabel/1000
value = tabel[1:,1:]
w_lines = tabel[0,1:]
j=0
h = tabel[0][2] - tabel[0][1]
for i in range(0, value.shape[0]):
	for j in range(0, 13):
		v = value[i]
		area_stns[i+1][j+1] = simpson_3(v, j, h)

np.savetxt('area_stns.csv', np.transpose(area_stns), delimiter = ',')
