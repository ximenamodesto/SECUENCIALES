#Ejercicio 06: Mayor y menor de 3 edades

import os

a = float (input ('Ingresa el valor de a: '))
b = float (input ('ingresa el valor de b: '))
c = float (input ('Ingresa el valor de c: '))
if a>b:
    mayor=a
    menor=b
else:
    mayor=b
    menor=a
if mayor<c:
    mayor=c
if menor>c:
    menor=c
print ('Valor de mayor: ' + repr (mayor))
print ('Valor de menor: ' + repr (menor))
print ()
os.system ('pause')