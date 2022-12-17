#Ejercicio 11: Signo de un número entre positivo, negativo y cero.

numero_como_cadena = input("Escribe un número: ")
numero = float(numero_como_cadena)
if numero == 0:
    print("Neutro")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")