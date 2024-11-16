'''

Gestión de inventario con diccionarios.

En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa
que permita:

    1. Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en
    un diccionario donde la clave es el nombre del producto y el valor es su precio.
    2. Una vez ingresados, mostrará todos los productos y sus precios en pantalla.

Ejemplo de salida esperada:

Producto: Manzanas, Precio: 100
Producto: Naranjas, Precio: 150
Producto: Peras, Precio: 120

'''

inventario = {}

for _ in range(3):
    producto = input("Ingrese nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    inventario[producto] = precio

for producto, precio in inventario.items():
    print(f"Producto: {producto}, Precio: {precio:.2f}")