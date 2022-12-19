#Ejercicio 08:

import os

examen_1=float (input ('Ingresa la nota del primer examen: '))
examen_2=float (input ('Ingresa la nota del segundo examen: '))
examen_3=float (input ('Ingresa la nota del tercer examen: '))
propina_mensual=20
if examen_1 > 13:
    propina_1= propina_mensual + 5
if examen_1 < 13:
    propina_1=propina_mensual
if examen_2 > 13:
    propina_2= propina_mensual + 5
if examen_2 < 13:
    propina_2=propina_mensual
if examen_3 > 13:
    propina_3= propina_mensual + 5
if examen_3 < 13:
    propina_3=propina_mensual
monto_total = propina_1+propina_2+propina_3

print("El monto total de la propina es: " + repr(monto_total))
print()
os.system ('pause')