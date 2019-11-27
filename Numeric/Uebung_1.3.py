import math

a = 0
b = 1
result = 1/27*(13 * math.sqrt(13) - 8)

def x(t):
	return t*t

def y(t):
	return t*t*t

def f(x):
	return math.pow(math.sqrt(x), 3)

#a)
def simpson():
	return (b-a)(1/6)

print(result)


