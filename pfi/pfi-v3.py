import sqlite3

# Función para crear la tabla de productos si aun no existe
def crear_tabla_productos():
    
    # Conectar a la base de datos
    conexion = sqlite3.connect("base_datos.db") 
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

    print("Tabla Productos creada con éxito.")


#Función que carga datos de prueba si la tabla productos esta vacía
def precargar_datos():

    nuevos_productos = [
        ("Pan", "Pan casero recién horneado", 20, 1.0, "Panadería"),
        ("Manzana", "Fruta fresca y deliciosa", 50, 0.5, "Frutas"),
    ]

    conexion = sqlite3.connect("base_datos.db")
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
            
            print(f"Producto {producto} registrado con éxito.")
    else:
        print("Ya existen registros en la tabla Productos. Se omite la carga inicial.")

    conexion.close()


# Función del menú principal que permite acceder a cada función
def mostrar_menu():

    opcion = "0"

    while opcion != "8":

        print("\nMenú de Gestión de Inventario:")
        print("-" * 30)
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de Bajo Stock")
        print("7. Vender producto")
        print("\n8. Salir")

        opcion = input("\nSeleccione una opción: ")

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
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
                

# Función para registrar un nuevo producto en la base de datos
def registrar_producto():
    
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una breve descripción: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    while cantidad <= 0:
            print("Error: La cantidad debe ser mayor a cero.")
            cantidad = int(input("Ingrese la cantidad disponible: "))

    precio = float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        print("Error: El precio debe ser mayor a cero.")
        precio = float(input("Ingrese el precio del producto: "))

    categoria = input("Ingrese la categoría del producto: ")

    # Agregar el producto a la tabla productos
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)", (nombre, descripcion, cantidad, precio, categoria))

    conexion.commit()

    print("Producto registrado con éxito.")

    conexion.close()


# Función para mostrar todos los productos registrados en la base de datos
def mostrar_productos():

    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM productos")
    
    resultados = cursor.fetchall()
    
    if resultados:
        print("\nListado de productos registrados:")
        print("-" * 30)
        
        for producto in resultados:
            print(f"\nCódigo: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Descripción: {producto[2]}")
            print(f"Cantidad: {producto[3]}")
            print(f"Precio: {producto[4]}")
            print(f"Categoría: {producto[5]}\n")
            print("-" * 30)
    else:
        print("El inventario está vacío.")
    
    conexion.close()


def actualizar_producto():
    foo = "bar"
    # codigo = int(input("Ingrese el código del producto que desea actualizar: "))
    # if codigo in inventario:
    #     nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    #     inventario[codigo]["cantidad"] = nueva_cantidad
    #     print("Producto", codigo, "actualizado con éxito.")
    # else:
    #     print("Producto no encontrado.")


def eliminar_producto():
    foo = "bar"
    # codigo = int(input("Ingrese el código del producto que desea eliminar: "))
    # if codigo in inventario:
    #     del inventario[codigo]
    #     print("Producto con código", codigo, "eliminado con éxito.")
    # else:
    #     print("Producto no encontrado.")

def buscar_producto():
    foo = "bar"
    # codigo = int(input("Ingrese el código del producto a buscar: "))
    # if codigo in inventario:
    #     datos = inventario[codigo]
    #     print("Nombre:", datos['nombre'])
    #     print("Descripción:", datos['descripcion'])
    #     print("Cantidad:", datos['cantidad'])
    #     print("Precio:", datos['precio'])
    #     print("Categoría:", datos['categoria'])
    # else:
    #   print("Producto no encontrado.")

def reporte_bajo_stock():
    foo = "bar"
    # limite = int(input("Ingrese el límite de stock para generar el reporte: "))
    # print("Productos con stock igual o inferior a", limite, ":")
    # for codigo, datos in inventario.items():
    #     if datos["cantidad"] <= limite:
    #         print("Código:", codigo)
    #         print("Nombre:", datos['nombre'])
    #         print("Cantidad:", datos['cantidad'])

def vender_producto():
    foo = "bar"
    # codigo = int(input("Ingrese el código del producto vendido: "))
    # if codigo in inventario:
    #     cantidad_vendida = int(input("Ingrese cantidad vendida: "))
    #     stock = inventario[codigo]["cantidad"]
    #     if cantidad_vendida <= stock:
    #         inventario[codigo]["cantidad"] = stock - cantidad_vendida
    #         print("Venta registrada.")
    #     else:
    #         print("Error: No hay stock suficiente para completar la venta.")
    # else:
    #     print("Error: Producto no encontrado.")


# Invocar la función para crear la tabla
crear_tabla_productos()

# Invocar la función para insertar datos
precargar_datos()

# Iniciar el programa llamando al menú principal
mostrar_menu()