#Ejercicio 15. Juan y Rosa aportan en dólares y Daniel en soles. Desarrolle el programa que determine el capital en dólares y que porcentaje de dicho capital aporta cada uno. Dólar = S/. 3.00

ju=int(input("ingresa aporte de juan\n"))
ro=int(input("ingresa aporte de rosa\n"))
da=int(input("ingresa aporte de daniel\n"))

dol = 3.00

total=ju+ro+dol

porcro = (ro/total)*100
porcda = (dol/total)*100
porcju = (ju/total)*100
print("El capital total es " + str(total)+"\n" + "El porcentaje de aporte de juan es " + str(porcju)+"\n" +
"El porcentaje de aporte de rosa es " + str(porcro)+"\n" + "El porcentaje de aporte de daniel es " + str(porcda))
