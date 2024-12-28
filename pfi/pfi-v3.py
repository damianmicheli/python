#-------------------------------------
# Talento Tech
# Proyecto Final Integrador
#
# SISTEMA DE GESTION DE INVENTARIO
#
# Damián Micheli - 2024
#-------------------------------------


#----------------------
#  Imports
#----------------------

import sqlite3
from colorama import init, Fore, Back, Style

#----------------------
#  Funciones
#----------------------

# Función que pausa la ejecución y pide la presión de una tecla para seguir
def pausa():
    input(Fore.YELLOW + "\nPresione una tecla para continuar...")

# Función para crear la tabla de productos si aun no existe
def crear_tabla_productos():
    print(Fore.BLUE + "\nCreando tabla productos...")
    
    # Conectar a la base de datos
    conexion = sqlite3.connect("inventario.db") 
    cursor = conexion.cursor()

    # Crear la tabla productos si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')

    # Confirmar la creación de la tabla y cerrar la conexión
    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "Tabla Productos creada con éxito o ya existía.")


#Función que carga datos de prueba si la tabla productos esta vacía
def precargar_datos():
    print(Fore.BLUE + "\nCargando datos de ejemplo...")

    nuevos_productos = [
        ("Pan", "Pan casero recién horneado", 20, 120.0, "Panadería"),
        ("Manzana", "Fruta fresca y deliciosa", 50, 200.5, "Frutas"),
        ("Banana", "De Ecuador", 30, 130.5, "Frutas"),
        ("Uvas", "Sin semilla", 15, 320.0, "Frutas"),
        ("Yogur Vainilla", "Firme y cremoso", 23, 145.5, "Lácteos"),
    ]

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    
    resultados = cursor.fetchall()
    
    if not resultados:

        for producto in nuevos_productos:
            nombre = producto[0]
            descripcion = producto[1]
            cantidad = producto[2]
            precio = producto[3]
            categoria = producto[4]
            
            cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)", (nombre, descripcion, cantidad, precio, categoria))
            
            conexion.commit()
            
            print(Fore.GREEN + f"Producto {producto} registrado con éxito.")
    else:
        print(Fore.RED + "Ya existen registros en la tabla Productos. Se omite la carga inicial.")

    conexion.close()


# Función del menú principal que permite acceder a cada función
def mostrar_menu():

    opcion = "0"

    while opcion != "8":

        print(Style.BRIGHT + Fore.CYAN + "\nMenú de Gestión de Inventario:")
        print(Style.BRIGHT + Fore.CYAN + "-" * 30)
        print(Fore.CYAN + "\n1. Registrar producto 📝 ")
        print(Fore.CYAN + "2. Mostrar productos 👀 ")
        print(Fore.CYAN + "3. Actualizar producto 🎯 ")
        print(Fore.CYAN + "4. Eliminar producto ❌ ")
        print(Fore.CYAN + "5. Buscar producto 🔍 ")
        print(Fore.CYAN + "6. Reporte de Bajo Stock 📉 ")
        print(Fore.CYAN + "7. Vender producto 🛒 ")
        print(Fore.MAGENTA + "\n8. Salir 🚪🚶")

        opcion = input(Fore.YELLOW + "\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            vender_producto()
        elif opcion == "8":
            print(Fore.BLUE + "\nSaliendo del programa...")
            print(Fore.BLUE + Style.BRIGHT +  "Gracias por utilizar SISTEMA DE GESTION DE INVENTARIO!\n\n")
        else:
            print(Back.RED + "\nOpción inválida. Por favor, intente nuevamente.")
                

# Función para registrar un nuevo producto en la base de datos
def registrar_producto():
    
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    nombre = input(Fore.YELLOW + "Ingrese el nombre del producto: ")
    descripcion = input(Fore.YELLOW + "Ingrese una breve descripción: ")
    cantidad = int(input(Fore.YELLOW + "Ingrese la cantidad disponible: "))
    while cantidad <= 0:
            print(Back.RED + "Error: La cantidad debe ser mayor a cero.")
            cantidad = int(input(Fore.YELLOW + "Ingrese la cantidad disponible: "))

    precio = float(input(Fore.YELLOW + "Ingrese el precio del producto: "))
    while precio <= 0:
        print(Back.RED + "Error: El precio debe ser mayor a cero.")
        precio = float(input(Fore.YELLOW + "Ingrese el precio del producto: "))

    categoria = input(Fore.YELLOW + "Ingrese la categoría del producto: ")

    # Agregar el producto a la tabla productos
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)", (nombre, descripcion, cantidad, precio, categoria))

    conexion.commit()

    print(Fore.GREEN + "Producto registrado con éxito.")

    conexion.close()
    pausa()

# Función para mostrar todos los productos registrados en la base de datos
def mostrar_productos():

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM productos")
    
    resultados = cursor.fetchall()
    
    if resultados:
        print(Style.BRIGHT + Fore.BLUE + "\nListado de productos registrados:")
        print(Style.BRIGHT + Fore.BLUE + "-" * 30)
        
        for producto in resultados:
            print(f"\nCódigo: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Descripción: {producto[2]}")
            print(f"Cantidad: {producto[3]}")
            print(f"Precio: {producto[4]}")
            print(f"Categoría: {producto[5]}\n")
            print("-" * 30)
    else:
        print(Fore.RED + "El inventario está vacío.")
    
    conexion.close()
    pausa()

# Función para actualizar la cantidad de un producto específico en la base de datos
def actualizar_producto():

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    codigo = int(input(Fore.YELLOW + "Ingrese el código del producto que desea actualizar: "))
    nueva_cantidad = int(input(Fore.YELLOW + "Ingrese la nueva cantidad: "))
    
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id_producto = ?",(nueva_cantidad, codigo))
    
    if cursor.rowcount > 0:
        print(Fore.GREEN + f"Producto {codigo} actualizado con éxito.")
    else:
        print(Back.RED +"Producto no encontrado.")

    conexion.commit()
    conexion.close()
    pausa()  

# Función para eliminar un producto específico de la base de datos
def eliminar_producto():
    
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    codigo = int(input(Fore.YELLOW + "Ingrese el código del producto que desea eliminar: "))
    
    cursor.execute("DELETE FROM productos WHERE id_producto = ?", (codigo,))
    
    if cursor.rowcount > 0:
        print(Fore.GREEN + f"Producto con código {codigo} eliminado con éxito.")
    else:
        print(Back.RED + "Producto no encontrado.")
    
    conexion.commit()
    conexion.close()
    pausa()

# Función para buscar un producto en la base de datos
def buscar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    codigo = int(input(Fore.YELLOW + "Ingrese el código del producto a buscar: "))

    cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (codigo,))
    
    resultado = cursor.fetchone()

    if resultado:
        print(Fore.BLUE + "\nInformación del producto encontrado:")
        print(Fore.BLUE + "-" * 30)
        print("Nombre:", resultado[1])
        print("Descripción:", resultado[2])
        print("Cantidad:", resultado[3])
        print("Precio:", resultado[4])
        print("Categoría:", resultado[5])

    else:
        print(Back.RED + "Producto no encontrado.")

    conexion.close()
    pausa()

# Función para generar un reporte de productos con bajo stock
def reporte_bajo_stock():

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    limite = int(input(Fore.YELLOW + "Ingrese el límite de stock para generar el reporte: "))


    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    resultados = cursor.fetchall()

    if resultados:
        print(Fore.BLUE + f"\nProductos con stock igual o inferior a {limite}:")
        print(Fore.BLUE + "-" * 30)

        for producto in resultados:
            print(f"Código: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")
    else:
        print(Fore.GREEN + "No se encontraron productos con stock bajo.")
    
    conexion.close()
    pausa()


# Función para registrar la venta de un producto
def vender_producto():

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    codigo = int(input(Fore.YELLOW + "Ingrese el código del producto vendido: "))

    cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (codigo,))
    
    resultado = cursor.fetchone()

    if resultado:
        cantidad_vendida = int(input(Fore.YELLOW + "Ingrese cantidad vendida: "))

        while cantidad_vendida <= 0:
            print(Back.RED + "Error: La cantidad vendida debe ser mayor a cero.")
            cantidad_vendida = int(input(Fore.YELLOW + "Ingrese cantidad vendida: "))

        stock = resultado[3]
        nueva_cantidad = stock - cantidad_vendida

        if nueva_cantidad >= 0:
            cursor.execute("UPDATE productos SET cantidad = ? WHERE id_producto = ?",(nueva_cantidad, codigo))
            
            if cursor.rowcount > 0:
                print(Fore.GREEN + "Venta registrada.")
            else:
                print(Back.RED + "Ocurrió un error inesperado.")

            conexion.commit()
        else:
            print(Back.RED + "Error: No hay stock suficiente para completar la venta.")

    else:
        print(Back.RED + "Producto no encontrado.")

    conexion.close()
    pausa()

#----------------------
#  Programa principal   
#----------------------

# Inicializar Colorama
init(autoreset=True)

# Invocar la función para crear la tabla si no existe
crear_tabla_productos()

# Invocar la función para insertar datos si la tabla está vacía
precargar_datos()

# Iniciar el programa llamando al menú principal
mostrar_menu()