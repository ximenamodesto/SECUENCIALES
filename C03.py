#Ejercicio 04: 

import os

nota_1 = float (input ('Ingresa el valor de nota 1: '))
nota_2 = float (input ('Ingresa el valor de nota 2: '))
nota_3 = float (input ('Ingresa el valor de nota 3: '))
if nota_3>=10 and nota_3<18:
    nota_3=nota_3+2
promedio=(nota_1+nota_2+nota_3)/3
print ('Valor de promedio final: ' + repr (promedio))
print ()
os.system ('pause')