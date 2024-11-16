'''

Consultar stock en inventario

El inventario de una tienda está almacenado en un diccionario, donde las claves son los
nombres de los productos y los valores son las cantidades disponibles en stock. Creá un
programa que:

    1. Te permita ingresar el nombre de un producto.
    2. Utilice el método .get() para buscar el stock disponible. Si el producto no existe,
    deberá mostrar un mensaje diciendo "Producto no encontrado".
    3. Si el producto está disponible, mostrará cuántas unidades quedan en stock.

Diccionario inicial:

productos = {
"Manzanas": 50,
"Naranjas": 30,
"Peras": 25
}

Ejemplo de salida esperada:

Ingresá el nombre del producto: Peras
Stock disponible de Peras: 25

'''

productos = {
    "Manzanas": 50,
    "Naranjas": 30,
    "Peras": 25
}

producto = input("Ingrese el nombre del producto: ")

stock = productos.get(producto)

if stock != None:
    print(f"Stock disponible de {producto}: {stock}")
else:
    print ("Producto no encontrado")
