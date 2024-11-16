# Diccionario de productos con cantidad en stock
productos = {
    "Manzanas": 50,
    "Peras": 30,
    "Bananas": 20
}

# Recorremos el diccionario para mostrar los productos
print("Inventario de productos:")
for producto, cantidad in productos.items():
    print("Producto:", producto, "- Cantidad en stock:", cantidad)

# Calculamos el total de productos en stock
total_productos = sum(productos.values())
print("Total de productos en stock:", total_productos)