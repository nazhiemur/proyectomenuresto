#en este solo codigo se resuelven los ejercicios 6 y 7
#con la linea de codigo que posee el "if" se resuelve el ejercicio 7
#quitando esa linea queda resuelto el ejercicio 6
#ejercicio 8 en el if se agrega "or i % 5 == 0" para que cuente los que son divisibles 5 
import time
i = 0
while i < 100 :
    i += 1
    time.sleep(0.50)
    if i % 2 == 0 or i % 5 == 0:
        print("Cargando... ",i,end='\r')
else:
    time.sleep(1)
    print("Fin del programa")