#Ejercicio 34:

import os

altura_en_m = float (input ('Ingresa el valor de altura en m: '))
peso_en_kg = float (input ('Ingresa el valor de peso en kg: '))
IMC=peso_en_kg/altura_en_m/altura_en_m
if IMC<20:
    print ('Grado de Obesidad: Delgado')
if IMC>=20 and IMC<25:
    print ('Grado de obesidad: Normal')
if IMC>=25 and IMC<27:
    print ('Grado de obesidad: Sobrepeso')
if IMC>=27:
    print ('Grado de obesidad: Obesidad')
print ('Valor de IMC: ' + repr (IMC))
print ()
os.system ('pause')