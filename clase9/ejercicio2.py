'''

Mostrar los códigos de productos ingresados

En un sistema de inventario, cada producto tiene un código que lo identifica. Escribí un
programa que permita ingresar los códigos de 4 productos y luego indicá que se muestren
uno por uno, junto con su posición en la lista. 

Ejemplo: si los códigos ingresados son
"P001", "P002", "P003", "P004", el programa debe mostrar:
Producto 1: P001
Producto 2: P002
Producto 3: P003
Producto 4: P004

Tips:
    ● Utilizá un bucle for y range() para recorrer los códigos e imprimirlos.

'''
productos=[]
cantidad_de_productos = int(input("Cuantos productos quiere registrar?: "))

for i in range(cantidad_de_productos):
    cod = input("Ingrese el código del producto {}: ".format(i+1))
    productos.append(cod)

for i, producto in enumerate(productos):
    print(f"Producto {i+1}: {producto}")