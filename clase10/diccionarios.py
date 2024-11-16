# Diccionario de productos con nombre y cantidad
productos = {
    "manzanas": [50, 12.5],
    "peras": [30, 45.6],
    "bananas": [40, 23.5],
}

productos["naranjas"] = [10, 20.4]

for producto, info in productos.items():
    print(f"Producto: {producto}, Stock: {info[0]}, Precio: {info[1]}.")

buscar = input("Ingrese producto a buscar: ")

producto = productos.get(buscar.lower())
if producto != None:
    print(f"Cantidad {buscar}: {producto[0]}")
    print(f"Precio {buscar}: {producto[1]}")
else:
    print(f"El producto {buscar} no se encuentra registrado")