#Ejercicio 12. 

segundos = int(input('Escribe la cantidad de segundos: '))

días = segundos // (24 * 60 * 60)
segundos =segundos % (24 * 60 * 60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
minutos = segundos // 60 
segundos = segundos % 60 

print('Días: {} - Horas: {} - Minutos: {} - Segundos: {}'.format(días, horas, minutos, segundos))