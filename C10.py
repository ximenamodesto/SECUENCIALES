#Ejercicio 14:

import os

raspa_gana=int(input ("Ingrese el numero de la tarjeta: "))

if raspa_gana % 2 == 0 and raspa_gana > 100:
    porc=15
    resultado_1=raspa_gana * porc/100
    print("El numero secreto es par no menor de 100 y obtuvo el 15% de descuento, el descuento seria: " + repr (resultado_1) , "%")
elif raspa_gana < 100:
    porc=5
    resultado_2=raspa_gana * porc/100
    print("El numero secreto no es par no menor de 100 y obtuvo el 5% de descuento, el descuento seria: " + repr (resultado_2) , "%")
else:
    print("El numer secreto es impar, no se obtiene descuentos")
print()
os.system ('pause')
