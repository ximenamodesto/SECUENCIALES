#Ejercicio 12: 

import os

dia_de_la_semana = int (input ('Ingresa el valor de dia de la semana: '))
if dia_de_la_semana==1:
    print ('Lunes')
if dia_de_la_semana==2:
    print ('Martes')
if dia_de_la_semana==3:
    print ('Miércoles')
if dia_de_la_semana==4:
    print ('Jueves')
if dia_de_la_semana==5:
    print ('Viernes')
if dia_de_la_semana==6:
    print ('Sábado')
if dia_de_la_semana==7:
    print ('Domingo')
if dia_de_la_semana<1 or dia_de_la_semana>7:
    print ('Número no válido')
print ()
os.system ('pause')