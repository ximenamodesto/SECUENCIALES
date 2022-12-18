#Ejercicio 17:

import os

donacion= float(input("Ingrese el monto de la donacion: "))
centro_de_salud = donacion*0.25
comedor_infantil = donacion*0.35
escuela_infantil = donacion*0.25
asilo_de_ancianos = donacion*0.15

print("El centro de salud recibe S/." + repr (centro_de_salud))
print("El comedor infantil recibe S/." + repr (comedor_infantil))
print("La escuela infantil recibe S/." + repr (escuela_infantil))
print("El asilo de ancianos recibe S/." + repr (asilo_de_ancianos))
print()
os.system ('pause')

