import numpy as np 
def simpson_1(value, n, h):
	#n should be even, n is no of waterline(n>=2), value is the y coordinate, h is the step size
	if(n < 2):
		raise TypeError('n should be more than or equal to 2')

	area = 0
	if(n%2 != 0):
		n = n-1
		area = h*(5*value[n] + 8*value[n-1] - 1*value[n-2])/12
	i = 0
	while(i<n):
		area = area + h*(1*value[i] + 4*value[i+1] + 1*value[i+2])/3
		i = i+2

	return area

def simpson_2(value, n, h):
	if(n < 2):
		raise TypeError('n should be more than or equal to 2')
	area = 0
	if(n%3 == 1):
		n = n-1
		area = h*(5*value[n] + 8*value[n-1] - 1*value[n-2])/12
	if(n%3 == 2):
		n = n-2
		area = h*(1*value[n] + 4*value[n-1] + 1*value[n-2])/3
	i = 0
	while(i<n):
		area = area + 3*h*(1*value[i] + 3*value[i+1] + 3*value[i+2] + 1*value[i+3])/8
		i = i+3

	return area
def simpson_3(value, n, h):
	if(value.shape[0] < 2):
		raise TypeError('number of rows of matrix must be greater than 2')
	if(n == 1):
		return h*(5*value[0] + 8*value[1] - 1*value[2])/12
	area = 0
	if(n == 0):
		return 0
	i = 0
	while(i<n-1):
		area = area + (5*value[i] + 8*value[i+1] - 1*value[i+2])
		i = i+1
	area = area + (5*value[n] + 8*value[n-1] - 1*value[n-2])

	return h*area/12
