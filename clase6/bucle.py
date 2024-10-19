cantidad = int(input("Ingresá la cantidad de productos: "))

while cantidad <= 0:
    print("La cantidad debe ser mayor que 0.")
    cantidad = int(input("Por favor, ingresá nuevamente la cantidad de productos: "))
print("Has ingresado una cantidad válida:", cantidad)

fallos = 0
opcion = 0
while opcion != 3:
    print("\nMenú de Opciones")
    print("1. Ver productos")
    print("2. Agregar un producto")
    print("3. Salir")

    if fallos > 0:
        opcion = int(input(f"Seleccioná una opción (ya te equivocaste {fallos} vez/veces. pensá un poquito mas esta vez!): "))
    else:
        opcion = int(input("Seleccioná una opción: "))
    if opcion == 1:
        print("Mostrando productos...")
        fallos = 0
    elif opcion == 2:
        print("Agregando un producto...")
        fallos = 0
    elif opcion == 3:
        print("Saliendo del menú.")
    else:
        print("Opción no válida. Por favor, ingresá una opción entre 1 y 3.")
        fallos += 1