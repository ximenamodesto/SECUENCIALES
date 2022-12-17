#Ejercicio 02: Metros a cm, pulgadas, pies y yardas

import os

metros = float (input ('Ingresa el valor de metros: '))
pulgadas=metros*39.27 
cm=pulgadas*2.54
pies=pulgadas/12
yardas=pies/3
print ('Valor de pulgadas ' + repr (pulgadas))
print ('Valor de cm: ' + repr (cm))
print ('Valor de pies: ' + repr (pies))
print ('Valor de yardas: ' + repr (yardas))
print ()
os.system ('pause')



