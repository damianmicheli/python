'''
Consultar el stock de productos
Tu programa debe permitir consultar el inventario de una tienda para verificar si un producto
está en stock. Si el producto está en la lista, el programa debe informarlo, si no, debe
mostrar un mensaje indicando que no está disponible.
Tips:
● Usá una lista para almacenar los productos en stock.
● Permití que el usuario ingrese el nombre de un producto a consultar.
● Recorré la lista con un bucle while para verificar si el producto está en stock.
'''

# Lista de productos: nombre, precio y cantidad
inventario = [
["manzanas", 100, 50],
["pan", 50, 20],
["leche", 60, 30]
]

buscar = input('Ingrese producto a buscar: ').lower()
indice = 0 
encontrado = False

while indice < len(inventario) and not encontrado:
    if inventario[indice][0] == buscar:
        encontrado = True
    else:
        indice += 1

if encontrado:
    print(f'Producto encontrado: {inventario[indice][0]}, Precio: {inventario[indice][1]:.2f}, Cantidad: {inventario[indice][2]}')
else:
    print('No se encontro el producto')