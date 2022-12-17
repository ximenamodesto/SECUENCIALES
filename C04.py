#Ejercicio 20: Determinar si es orden ascendente, descendente o desordenado

import os

a = float (input ('Ingresa el valor de a: '))
b = float (input ('Ingresa el valor de b: '))
c = float (input ('Ingresa el valor de c: '))
if a<b<c: 
    print ('Orden ascendente')
if a>b>c:
    print ('Orden descendente')
if a<b>c:
    print ('Desordenado')
if a>b<c:
    print ('Desordenado')
print ()
os.system ('pause')
