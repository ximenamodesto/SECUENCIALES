#Ejercicio 04:

import os 

pie=int ( input ("Pies: "))
pulgadas=int (input ("Pulgadas: "))

estatura_en_metros=( ( (pie*12) + pulgadas)*2.54)/100
print("Estatura en metros: " + repr (estatura_en_metros))
print ()
os.system ('pause')



