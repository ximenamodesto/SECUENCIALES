#Ejercicio 08: Area base, área lateral y área total de un cilindro.

import os, math


altura = float (input ('Ingresa el valor de altura: '))
radio = float (input ('Ingresa el valor de radio: '))
areabase=math.pi*radio*radio
arealateral=2.0*math.pi*radio*altura
areatotal=2.0*(areabase)*(arealateral)
print ('Valor de areabase: ' + repr (areabase))
print ('Valor de arealateral: ' + repr (arealateral))
print ('Valor de areatotal: ' + repr (areatotal))
print ()
os.system ('pause')

