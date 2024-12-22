####################################
# Sistema de Gestión de Inventario #
# Proyecto Final Integrador        #
# Talento Tech                     #
# Damián Micheli - 2024            #
####################################

# Variables iniciales
fallos = 0
opcion = 0
inventario = []


# Función para mostrar el menu
def mostrar_menu():
    print("\nMenú de Gestión de Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")

def mostrar_menu():
    print("\nMenú de Gestión de Inventario:")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte de Bajo Stock")
    print("7. Salir")

# Función para leer y validad el precio o la cantidad de un producto
def leer_dato(tipo):

    while tipo != "precio" and tipo != "cantidad":
        tipo = input("El tipo es incorrecto: Ingresar 'precio' o 'cantidad': ")

    if tipo == "precio":
        dato = float(input(f'Ingrese precio del producto: '))
        while dato <= 0:
            dato = float(input('El precio debe ser mayor a 0. Ingrese precio del producto: '))
    
    else:
        dato = int(input(f'Ingrese cantidad del producto: '))
        while dato < 0:
            dato = int(input('La cantidad no puede ser negativa. Ingrese cantidad del producto: '))
    
    return dato


# Función para mostrar el inventario
def mostrar_inventario(inv): # Mostrar el inventario actualizado
    if len(inv) == 0:
        print("\nEl inventario se encuentra vacío")
    
    else:
        print("\nInventario actualizado:")
        print("-------------------------\n")
        for producto in inv:
            print(f'Producto: {producto[0]}')
            print(f'Precio: ${producto[1]:.2f}')
            print(f'Cantidad disponible: {producto[2]}')
            print("-------------------------")


# Inicio del programa
while opcion != 3:

    mostrar_menu()

    if fallos > 0:
        opcion = int(input(f"Seleccioná una opción válida (ya te equivocaste {fallos} vez/veces!): "))
    else:
        opcion = int(input("Por favor, seleccioná una opción: "))

    if opcion == 1:  # Se seleccionó la opción 1 - Agregar productos
        
        fallos = 0 # reestablezco la cantidad de fallos a cero

        continuar = ''

        while continuar.lower() != 'n':
            producto=[]
            producto.append(input('Ingrese nombre del producto: '))
            repetido = False
            
            for i, item in enumerate(inventario):
                if item[0] == producto[0]:
                    repetido = True
                    modificar = input(f'El producto "{producto[0]}" ya se encuentra registrado. Modificar? (s/n): ')
                    if modificar.lower() == 's':
                        inventario[i][1] = leer_dato("precio")
                        inventario[i][2] = leer_dato("cantidad")
                    break
             
            if not repetido:
                producto.append(leer_dato("precio"))
                producto.append(leer_dato("cantidad"))
                inventario.append(producto)
            continuar = input('Agregar mas productos? (s/n): ')


    elif opcion == 2: # Se seleccionó la opción 2 - Mostrar productos

        fallos = 0
        mostrar_inventario(inventario)
        
    elif opcion == 3: # Se seleccionó la opción 3 - Salir
        print("\nSaliendo del sistema. Muchas gracias por utilizar Gestión de Productos!")

    else:
        print("\nOpción no válida. Por favor, ingresá una opción entre 1 y 3.")
        fallos += 1

# Fin del programa