import threading
import time

#funcion a ejecutar
def prueba ():
    print ("inicio")

    

threads =list ()

#ejecutando los hilos
for i in range (2):
    t=threading.Thread(target=prueba)
    threads.append(t)
    t.start()

#for t in threads:
 #   t.join




def contar():
    contador = 0
    while contador<10:
        contador+=1
        print('Hilo:', threading.current_thread().getName(),'con identificador:', threading.current_thread().ident,'Contador:', contador)

NUM_HILOS = 8

for num_hilo in range(NUM_HILOS):
    hilo = threading.Thread(name='hilo%s' %num_hilo, target=contar)    
    #hilo.start()

