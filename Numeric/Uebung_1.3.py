import math

result = 1 / 27 * (13 * math.sqrt(13) - 8)

#Bogenlänge = |P'(t)|
# Siehe Block 3a
def curve(t):
	return math.sqrt(t * t * (4 + 9 * t * t))

#a)
def simpson(a,b,f):
    return (b - a) * (1 / 6 * f(a) + 4 / 6 * f(a + ((b - a) / 2)) + 1 / 6 * f(b))

#b)
def intervall(a,b,segNr,f):
    h = (b - a) / segNr
    sum = 0
    for i in range(segNr):
        #print(a + i * h)
        #print(a + (i+1) * h)
        sum = sum + simpson((a + i * h),(a + (i + 1) * h),f)
        #print("Segm" + str(i) + ":" + str(sum))
    return sum


print("Länge:\t" + str(result))
print("a):\t" + str(simpson(0,1,curve)))


#b) i)
precision = 10 ** -8

i = 1
while abs(intervall(0,1,i,curve)-result) > precision:
    i = i + 1

print("b) i) In " + str( i-1 ) + " Segmente" )
singlePrec = intervall(0,1,i-1,curve)
print("\t" + str(singlePrec))

doublePrec = intervall(0,1,(i-1)*2,curve)
print("b) ii)\t" + str(doublePrec))
print("Faktor: " + str((singlePrec-result) / (doublePrec-result)))

#c)
m = 1.894668589221

def p(t):
    return 1 + 1/2*math.sin(t)

def mass(t):
    p(t)*curve(t)

print("c)")
print("Mass:\t" + str(m))
print("simpson:\t" + str(simpson(0,1,mass)))
print("Segments i)")
singlePrec = intervall(0,1,i-1,mass)
print("\t" + str(singlePrec))

i = 1
while abs(intervall(0,1,i,curve)-result) > precision:
    i = i + 1
doublePrec = intervall(0,1,(i-1)*2,mass)
print("ii)\t" + str(doublePrec))
print("Faktor: " + str((singlePrec-result) / (doublePrec-result)))