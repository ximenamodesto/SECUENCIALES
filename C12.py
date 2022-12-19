#Ejercicio 01:

import os

unidades = int(input("Ingrese la cantidad de unidades: "))
if unidades <=25:
    precio_uni=27
elif unidades >=26:
    precio_uni=25
elif unidades >=51:
    precio_uni=23

print("El precio unitario es: " + repr(precio_uni))

importe = unidades*precio_uni

if unidades>50:
    descuento = importe*0.15
else:
    descuento = importe*0.05
total=importe-descuento

print("El importe de la compra es: " + repr(importe))
print("El descuento es de: " + repr(descuento))
print("El total a pagar es: " + repr(total))
print()
os.system ('pause')




        


