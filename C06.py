#Ejercicio 23:

import os

nota_de_matematica = float (input ('Ingresa el valor de nota de matematica: '))
nota_de_fisica = float (input ('Ingresa el valor de nota de fisica: '))
propina=0
promedio=(nota_de_matematica+nota_de_fisica)/2
if nota_de_matematica>=17:
    propina=propina+nota_de_matematica*3
else:
    propina=propina+nota_de_matematica
if nota_de_fisica>=15:
    propina=propina+nota_de_fisica*2
else: 
    propina=propina+nota_de_fisica*0.5
if promedio>16:
    print('Le regala un reloj')
else:
    print('No le regala un reloj')
print ('Valor de propina: ' + repr (propina))
print ()
os.system ('pause')
