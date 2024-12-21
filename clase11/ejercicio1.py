'''

Gestión de descuentos

Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos. Vas a
desarrollar un programa que permita calcular el precio final de un producto después de
aplicar un descuento. Para hacerlo:

    1. Crea una función que reciba como parámetros el precio original del producto y el
    porcentaje de descuento, y que retorne el precio final con el descuento aplicado.
    2. Luego, solicitá que se ingrese el precio y el porcentaje de descuento. Mostrá el
    precio final después de aplicar el descuento.

'''

def aplicar_descuento (precio, descuento):
    resultado = precio - (precio * descuento / 100 )

    return resultado

precio = float(input("Ingrese precio: "))
descuento = float(input("Ingrese descuento: "))

total = aplicar_descuento(precio, descuento)

print(f"El precio final con el descuento es: ${total:.2f}")