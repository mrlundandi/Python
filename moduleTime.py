import time

hour = time.strftime('%H') 
minutes = time.strftime('%M') 

if int(hour) >= 19:
	print ("Stop working! Go home!") 
else:
	print ("{} hours and {} minutes left".format(18- int(hour), 59-int(minutes)))

'''En este segundo ejercicio tendréis que crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación 
para calcular el tiempo que queda de trabajo.'''