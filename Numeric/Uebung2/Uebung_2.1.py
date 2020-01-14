import math

def x(k):
	return math.pow(10,-k)

def f1(x):
	return math.sqrt(1+x) - 1

def f2(x):
	return x / (1+math.sqrt(1+x))

def fTaylor(x):
	return (1/2) * x - (1/8) * math.pow(x,2) + (1/16) * math.pow(x,3) - (5/128) * math.pow(x,4) + (7/256) * math.pow(x,5) - (21/1024) * math.pow(x,6)  + (33/2048) * math.pow(x,7) - (429/32768) * math.pow(x,8) + (715/65536) * math.pow(x,9) - (2431/262144) * math.pow(x,10)

#b)
for k in range(15):
	print("K: "+str(k))
	print(f1(x(k)));
	print(f2(x(k)));
	print(fTaylor(x(k)));