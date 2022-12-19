#Ejercicio 03:

import os

valor_del_ángulo = float (input ('Ingresa el valor del ángulo: '))
if valor_del_ángulo==0:
    print ('nulo')
if valor_del_ángulo>0 and valor_del_ángulo<90:
    print ('Agudo')
if valor_del_ángulo==90:
    print ('Recto')
if valor_del_ángulo>90 and valor_del_ángulo<180:
    print ('Obtuso')
if valor_del_ángulo==180:
    print ('Llano')
if valor_del_ángulo>180 and valor_del_ángulo<360:
    print ('Cóncavo')
if valor_del_ángulo==360:
    print ('Completo')
print ()
os.system ('pause')


