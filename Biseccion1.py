## Se importan Librerias

import math
import pylab
#import matplotlib
#matplotlib.use('Agg') # no UI backend
#import matplotlib.pyplot as plt
import numpy as np
from sys import exit

#se definen constantes
a=1.0
b=2.0
N=100
I=30
tol=1.0e-5
x=[]
fx=[]
fo=[]
delta=(b-a)/float(N-1)

#defino la funcion
def funcion(x):
	y=x**3+4*x**7-10
	return y

for i in range (N-1):
	x.append(a+delta*float(i))
for i in range (N-1):
	fx.append(funcion(x[i]))
	fo.append(0.0)

for n in range (I):
	p=(b+a)/2.0
		
	print ('n', n, '"a"', a, '"F"',funcion(a), 'b:', b, 'F(b):',funcion(b), 'p:', p, 'F(p):',funcion(p), 'abs:', abs(a-b), tol )

	if funcion(p)==0 or abs(b-a)<tol:
		print ('La raiz es:', p)
		break
	elif n==I-1:
		print ('La raiz no cenverge, es:', p)
		print ('Fallo tras:' , n , 'iteraciones.')
	
	if (funcion(p)*funcion(a)<0.0):
		b=p
	else:
		a=p

	if (a-b)<tol:
		N=100	


#print (x , fx)
pylab.plot(x,fx,'g-')
pylab.plot(x,fo,'r-')
pylab.plot(p,0,'ro')
pylab.title('Biseccion1 prueba')
pylab.savefig("Biseccion1.png")  #savefig, don't sw
#pylab.show()

#plt.plot(x, fx )
#plt.show()
#plt.savefig("Biseccion1.png")  #savefig, don't sw
