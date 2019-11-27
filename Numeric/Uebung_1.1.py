'''
Bei der Annäherung an das Ergebnis wird bei jedem Schritt überpruft,
ob das Arithmetische Mittel (x) von den gewählen Grenzen a & b größer oder kleiner als die gesuchte Zahl ist.

Ist f(x) kleiner als der f(gesuchte Zahl) (y) wird die untere Grenze (a) auf x vergrößert.
Ist f(x) größer als die f(gesuchte Zahl) (y) wird die obere Grenze (b) auf x verkleinert.

Dies wird so lange wirderholt, bis die gewünschte Genauigkeit erreicht wird.

Im Bereich [a,b] muss die Funktion f(x) stätig und monoton sein.

Der Abstand zwischen den Rändern [a,b] halbiert sich jeden Schritt.

'''

from decimal import Decimal

alive = True

stellen = 12

genauigkeit =  Decimal(Decimal(1)/Decimal(pow(10,stellen))) #Decimal.from_float(1E-12) # -> %

a = Decimal(1)
b = Decimal(2)
y = Decimal(3)

loops = 0

def f(x):
	return Decimal(x)*Decimal(x)

def result(a,b):
	return (Decimal(a)+Decimal(b))/Decimal(2)

while alive:

	x = result(a,b)

	fx = f(x)

	if fx > y:
		b = x
	else:
		a = x

	if (Decimal(abs(f(result(a,b)) - y)))/y < genauigkeit:
		alive = False

	loops += 1
	print("res: %E" % (Decimal(result(a,b))-Decimal('1.7320508075688772935274463415058723669428052538103806280558069794519330169088000370811461867572485756')))

print("\n")
print("Loops: "  + str(loops))
print("a: %E" % a)
print("b: %E" % b)
print("res: %E" % result(a,b))
print("res: %E" % (Decimal(result(a,b))-Decimal('1.7320508075688772935274463415058723669428052538103806280558069794519330169088000370811461867572485756')))