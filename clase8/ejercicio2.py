'''
Actualización del inventario a partir de un arreglo:

En una tienda es necesario actualizar el inventario cuando se venden productos. A
continuación, te proporcionamos un arreglo con una lista de productos, donde cada
producto tiene un código, una descripción y una cantidad en stock. Escribí un programa que
permita:

    ● Seleccionar un producto a partir de su código.
    ● Ingresar la cantidad vendida (que debe ser mayor que cero).
    ● Actualizar la cantidad en stock de ese producto restando la cantidad vendida.

El arreglo de productos disponibles es el siguiente:

productos = [
["P001", "Manzanas", 50],
["P002", "Peras", 40],
["P003", "Bananas", 30],
["P004", "Naranjas", 60]
]

El script que tenés que hacer debe modificar la cantidad en stock de acuerdo a cada venta
realizada. Si la cantidad vendida es mayor que la cantidad disponible en stock, el programa
debe mostrar un mensaje de error.

'''

productos = [
    ["P001", "Manzanas", 50],
    ["P002", "Peras", 40],
    ["P003", "Bananas", 30],
    ["P004", "Naranjas", 60]
]

codigo = input("Ingrese el código de producto: ")

indice = 0
encontrado = False

while indice < len(productos) and not encontrado:
    producto = productos[indice]
    if codigo == producto[0]:
        encontrado = True
        stock_actual = producto[2]

        venta = int(input("\nIngrese unidades vendidas (mayor a 0): "))
        while venta <= 0:
            venta = int(input("\nError. La cantidad debe ser mayor a 0. Ingrese unidades vendidas: "))
        if venta > stock_actual:
            print(f"\nNo se puede vender {venta} unidades, ya que el stock disponible es de {stock_actual}")
        else:
            stock = stock_actual - venta
            productos[indice][2] = stock
            print(f"\nSe vendieron {venta} {producto[1]}, el stock pasó de {stock_actual} a {stock}")


    indice += 1

if not encontrado:
    print("El código ingresado no se encuentra registrado")

# Mostrar el inventario actualizado
input("\nPresione una tecla para continuar...")
print("\nInventario actualizado:")
print("----------------------\n")
indice = 0
while indice < len(productos):
    producto = productos[indice]
    print(f'Código: {producto[0]}')
    print(f'Producto: {producto[1]}')
    print(f'Cantidad disponible: {producto[2]}')
    print("\n-------------------------\n")
    indice = indice + 1