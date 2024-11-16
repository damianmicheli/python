# Inventario inicial
inventario = {
    "Manzanas": 50,
    "Peras": 30,
    "Bananas": 40
}

# Diccionario para registrar ventas del día
ventas_dia = {}

# Pedimos al usuario que ingrese el producto y la cantidad vendida
# Supongamos que vendemos 3 productos diferentes en el día
for _ in range(3):
    producto = input("Ingresá el producto vendido: ")

    if producto in inventario: # Si el producto está en el inventario, registramos la venta

        cantidad_vendida = int(input("Ingresá la cantidad vendida: "))
        if producto in ventas_dia:
            if cantidad_vendida + ventas_dia[producto] <= inventario[producto]: # Valido que haya stock
                ventas_dia[producto] = ventas_dia[producto] + cantidad_vendida # Actualizamos el diccionario de ventas
            else:
                print("El stock es insuficiente")
        else:    
            if cantidad_vendida <= inventario[producto]: # Valido que haya stock
                ventas_dia[producto] = cantidad_vendida # Actualizamos el diccionario de ventas
            else:
                print("El stock es insuficiente")
    else:
        print("Producto no encontrado en inventario.")

# Actualizamos el inventario con las ventas del día
for producto, cantidad in ventas_dia.items():
    inventario[producto] = inventario[producto] - cantidad

print("Inventario actualizado:", inventario)