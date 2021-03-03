## Se importan Librerias

import math
import pylab
from sys import exit

#se definen constantes
a=0.0
b=math.pi
N=100
I=30
tol=1.0e-5
x=[]
fx=[]
fo=[]
delta=(b-a)/float(N-1)

#defino la funcion
def funcion(x):
	y=math.cos(x)-x
	return y

for i in range (N-1):
	x.append(a+delta*float(i))
for i in range (N-1):
	fx.append(funcion(x[i]))
	fo.append(0.0)

p=math.pi/4.0
for n in range (I):

	#	print 'n:', n, 'a:', a,'F(a):',funcion(a), 'b:', b, 'F(b):',funcion(b), 'p:', p, 'F(p):',funcion(p), 'abs:', abs(a-b), tol

	if funcion(p)==0 or abs(b-a)<tol:
		print 'La raiz es:', p
		print 'Iteraciones:',n+1
		break
	elif n==I:
		print 'La raiz no cenverge, es:', p
		print 'Fallo tras:' , n , 'iteraciones.'
	
	if (funcion(p)*funcion(a)<0.0):
		b=p
	else:
		a=p

	if (a-b)<tol:
		N=100	

	p=(b+a)/2.0

#print x , fx
pylab.plot(x,fx,'g-')
pylab.plot(x,fo,'r-')
pylab.plot(p,0,'ro')
pylab.show()		
