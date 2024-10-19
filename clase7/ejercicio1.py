'''
Registro de productos en un inventario
Te proponemos implementar un sistema básico para registrar productos en el inventario de
una tienda. El programa debe permitir que se agreguen productos a una lista hasta que se
decida no agregar más. Luego, deberás mostrar todos los productos ingresados al
inventario.
Tips:
● Usá una lista para almacenar los productos.
● Usá un bucle while para seguir ingresando productos mientras el usuario lo desee.
● Mostrá todos los productos registrados al final.
'''

# Lista de productos: nombre, precio y cantidad
inventario = []
continuar = ''

while continuar.lower() != 'n':
    producto=[]
    producto.append(input('Ingrese nombre del producto: '))
    indice = 0
    repetido = False
    while indice < len(inventario):
        if inventario[indice][0] == producto[0]:
            repetido = True
            modificar = input(f'El producto "{producto[0]}" ya se encuentra registrado. Modificar? (s/n): ')
            if modificar.lower() == 's':
                inventario[indice][1] = float(input('Ingrese nuevo precio del producto: '))
                inventario[indice][2] = int(input('Ingrese nueva cantidad del producto: '))
            break
        indice += 1
    if not repetido:
        producto.append(float(input('Ingrese precio del producto: ')))
        producto.append(int(input('Ingrese cantidad del producto: ')))
        inventario.append(producto)
    continuar = input('Agregar mas productos? (s/n): ')


# Mostrar el inventario actualizado
print("\nInventario actualizado:")
indice = 0
while indice < len(inventario):
    producto = inventario[indice]
    print(f'Producto: {producto[0]}')
    print(f'Precio: ${producto[1]:.2f}')
    print(f'Cantidad disponible: {producto[2]}')
    print("-------------------------")
    indice = indice + 1