
# Menú de opciones
fallos = 0
opcion = 0
inventario = []
while opcion != 3:
    print("\nMenú de Gestión de Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")

    if fallos > 0:
        opcion = int(input(f"Seleccioná una opción válida (ya te equivocaste {fallos} vez/veces!): "))
    else:
        opcion = int(input("Por favor, seleccioná una opción: "))

    if opcion == 1:
        
        fallos = 0 # reestablezco la cantidad de fallos a cero

        # Lista de productos: nombre, precio y cantidad
        
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
                        precio = float(input('Ingrese nuevo precio del producto: '))
                        while precio <= 0:
                            precio = float(input('El precio debe ser mayor a 0. Ingrese precio del producto: '))

                        cantidad = int(input('Ingrese nueva cantidad del producto: '))
                        while cantidad < 0:
                            cantidad = int(input('La cantidad no puede ser negativa. Ingrese cantidad del producto: '))    
                        inventario[indice][1] = precio
                        inventario[indice][2] = cantidad
                    break
                indice += 1
            if not repetido:
                precio = float(input('Ingrese precio del producto: '))
                while precio <= 0:
                    precio = float(input('El precio debe ser mayor a 0. Ingrese precio del producto: '))
                cantidad = int(input('Ingrese cantidad del producto: '))
                while cantidad < 0:
                    cantidad = int(input('La cantidad no puede ser negativa. Ingrese cantidad del producto: '))
                producto.append(precio)
                producto.append(cantidad)
                inventario.append(producto)
            continuar = input('Agregar mas productos? (s/n): ')

                
    elif opcion == 2:

        fallos = 0

        if len(inventario) == 0:
            print("\nEl inventario se encuentra vacío")
        else:
        # Mostrar el inventario actualizado
            print("\nInventario actualizado:")
            print("-------------------------\n")
            indice = 0
            while indice < len(inventario):
                producto = inventario[indice]
                print(f'Producto: {producto[0]}')
                print(f'Precio: ${producto[1]:.2f}')
                print(f'Cantidad disponible: {producto[2]}')
                print("-------------------------")
                indice = indice + 1
        
    elif opcion == 3:
        print("\nSaliendo del sistema. Muchas gracias por utilizar Gestión de Productos!")
    else:
        print("\nOpción no válida. Por favor, ingresá una opción entre 1 y 3.")
        fallos += 1
