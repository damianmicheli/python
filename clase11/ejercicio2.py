'''

Cálculo de promedio de ventas

Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:

    1. Creá una función que reciba como parámetro una lista de ventas diarias y devuelva
    el promedio de esas ventas.
    2. Solicitá a la persona que ingrese las ventas de cada día durante una semana (7
    días). Usá la función para calcular y mostrar el promedio de ventas al finalizar.

'''

def calcular_promedio(ventas):
    total = 0
    
    for venta in ventas:
        total += venta

    promedio = total / len(ventas)

    return promedio

ventas = []

for _ in range(7):
    venta = float(input("Ingrese una venta: "))
    ventas.append(venta)

print (f"El promedio de las ventas ingresadas es: {calcular_promedio(ventas):.2f}")