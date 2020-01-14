import numpy as np
import math

m = 100

tj = np.random.rand(m)
yj = np.zeros(m)


a = 0
b = 0
c = 0


def y(t, a, b, c):
	return (a + b*t) * np.e**(-c*t) * np.cos(t)

def dya(t, c):
	return np.e**(-c * t) * np.cos(t)

def dyb(t, c):
	return t * np.e**(-c * t) * np.cos(t)

def dyc(t, a, b):
	return -t * (a + b * t) * np.e**(-c * t) * np.cos(t)

def loss(a,b,c):
	global yj
	global tj

	return np.sum((y(tj,a,b,c) - yj)**2)

def backPropagation(lr):
	global a
	global b
	global c

	newA = a + np.sum(dya(tj, c)) * lr
	newB = b + np.sum(dyb(tj, c)) * lr
	newC = c + np.sum(dyc(tj, a, b)) * lr

	a = newA
	b = newB
	c = newC


#--------------------------------------------- Run --------------------------------------------
yj = y(tj,4,5,6)

while loss(a,b,c) > 0.1:
	backPropagation(0.001)
	print(a)
	print(b)
	print(c)

