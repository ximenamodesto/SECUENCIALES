#Ejercicio 09. Determinar la suma de cifras de un número entero. 

def getSum(n):

    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum
n = 3521
print(getSum(n))
