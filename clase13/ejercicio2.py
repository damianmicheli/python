'''

Simulación de precios con math y random
Supongamos que deseás simular los precios de 10 productos en un inventario. 
Escribí un programa que:
    * Utilice el módulo random para generar 10 precios aleatorios entre $10.00 
    y $100.00.
    * Redondee los precios generados a dos decimales usando una función del
    módulo math.

'''
precios = []

from random import uniform

for _ in range(10):
    precio = uniform(10, 100)
    precio = round(precio, 2)
    precios.append(precio)
print(precios)