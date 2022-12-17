#Ejercicio 06: Calcular el área total y volumen de un cilindro 

import os, math

altura = float (input ('Ingresa el valor de altura: '))
radio = float (input ('Ingresa el valor de radio: '))
volumen=math.pi*radio*radio*altura
area=2.0*math.pi*radio*(radio+altura)
print ('Valor de area: ' + repr (area))
print ('Valor de volumen: ' + repr (volumen))
print ()
os.system ('pause')

