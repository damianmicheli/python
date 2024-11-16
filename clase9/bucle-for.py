productos = ["manzanas", "naranjas", "bananas", "peras"]
for producto in productos:
    print(f"Producto disponible: {producto}")


# Lista de productos
productos = ["P001", "P002", "P003", "P004", "P005"]
# Producto que queremos encontrar
producto_a_buscar = "P004"
# Recorremos la lista buscando el producto
print("Buscando", end="")
for producto in productos:
    if producto == producto_a_buscar:
        print("\n\nProducto encontrado:", producto)
        break
# Detenemos el bucle al encontrar el producto
    print(".", end="")
print("Fin de la búsqueda.")


for i in range(5):
    print(i)

frutas = ["manzana", "banana", "naranja"]
for i, fruta in enumerate(frutas):
    print(f"Fruta {i+1}: {fruta}")
