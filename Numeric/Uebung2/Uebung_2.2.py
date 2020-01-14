import math
import sympy
import numpy as np

maxIter = 20

#Anfangswerte
x = (0.9, 0.5)

vars = sympy.symbols('x1 x2')
f = sympy.sympify(['x1*x1 + x2*x2', 'x1*x1*x1*x1 + x2*x2*x2*x2'])
J = sympy.zeros(len(f),len(vars))

def f1(x):
	return math.pow(x[0],2) + math.pow(x[1],2)

def f2(x):
	return math.pow(x[0],4) + math.pow(x[1],4)


def it():
	global x
	global J
	global f

	r1 = f1(x)
	r2 = f2(x)

	r = np.array([r1,r2])

	#print(r)
	#print(f)

	for i, fi in enumerate(f):
		for j, s in enumerate(vars):
			df = sympy.diff(fi, s)
			J[i,j] = df.evalf(subs={vars[0]: x[0], vars[1]: x[1]})

	
	#print(J)
	Jinv = sympy.inv_quick(J)
	#print(Jinv)

	r = r * (-1)
	delta = np.dot(Jinv,r)
	#print(x)
	x = x + r
	return x
	#print(x)
	

for i in range(maxIter):
	print(it())