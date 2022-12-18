#Ejercicio 18:

import os

cantidad_de_productos=float (input ("Cantidad de productos: "))
precio_unitario=float (input ("Precio del articulo: "))
importe_compra=precio_unitario*cantidad_de_productos
primer_descuento=importe_compra*0.15
segundo_descuento=(importe_compra-primer_descuento)+0.15
importe_a_pagar=(importe_compra-primer_descuento-segundo_descuento)

print("El importe de la compra S/." + repr (importe_compra))
print("El importe del primer descuento S/." + repr (primer_descuento))
print("El importe del segundo descuento S/." + repr (segundo_descuento))
print("El importe a pagar: " + repr (importe_a_pagar))
print()
os.system ('pause')




