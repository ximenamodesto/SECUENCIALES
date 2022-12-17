#Ejercicio 21: 

import os

informacion = int (input ('Ingresa el valor de informacion: '))
estado_civil=(informacion%10000-informacion%100)//1000
if estado_civil==1:
    print ('Soltero')
if estado_civil==2:
    print ('Casado')
if estado_civil==3:
    print ('Viudo')
if estado_civil==4:
    print ('Divorciado')
edad=(informacion%1000-informacion%10)//10
sexo=informacion%10
if sexo==1:
    print ('Femenino')
if sexo==2:
    print ('Masculino')
print ('Valor de edad: ' + repr (edad))
print ('Valor de estado civil: ' + repr (estado_civil))
print ('Valor de sexo: ' + repr (sexo))
print ()
os.system ('pause')