#Ejercicio 07:

import os

n1 = float (input ('Ingresa el valor de n1: '))
n2 = float (input ('Ingresa el valor de n2: '))
n3 = float (input ('Ingresa el valor de n3: '))

if n1 > n2 and n1 < n3:
    numero_intermedio = n1
    print("El número intermedio es: " + repr(n1))
if n2 > n1 and n2 < n3:
    numero_intermedio = n2
    print("El número intermedio es: " + repr(n2))
if n3 > n2 and n3 < n1:
    numero_intermedio = n3
    print("El número intermedio es: " + repr(n3))
print()
os.system ('pause')