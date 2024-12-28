import sqlite3

def crear_tabla_personas():
    
    # Conectar a la base de datos
    conexion = sqlite3.connect("base_datos.db") 
    cursor = conexion.cursor()

    # Crear la tabla Personas si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Personas (
            nombre TEXT,
            edad INTEGER,
            ciudad TEXT
        )
    ''')

    # Confirmar la creación de la tabla y cerrar la conexión
    conexion.commit()
    conexion.close()

    print("Tabla Personas creada con éxito.")


def precargar_datos():

    nuevas_personas = [
        ("Esteban", 32, "Mar del Plata"),
        ("Valeria", 27, "Bahía Blanca"),
        ("Fernando", 41, "Rosario"),
        ("Carolina", 29, "La Plata"),
        ("Juan", 35, "Córdoba")
    ]

    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Personas")
    
    resultados = cursor.fetchall()
    
    if not resultados:

        for persona in nuevas_personas:
            nombre = persona[0]
            edad = persona[1]
            ciudad = persona[2]
            
            cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES (?, ?, ?)", (nombre, edad, ciudad))
            
            conexion.commit()
            
            print(f"Persona {persona} registrada con éxito.")
    else:
        print("Ya existen registros en la tabla Personas.")

    conexion.close()


# Función para registrar una nueva persona en la base de datos
def registrar_persona():

    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    ciudad = input("Ingrese la ciudad de residencia: ")
    
    cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES (?, ?, ?)", (nombre, edad, ciudad))
    
    conexion.commit()
    
    print("Persona registrada con éxito.")
    conexion.close()


# Función para mostrar todas las personas registradas en la base de datos
def mostrar_personas():
    
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM Personas")
    
    resultados = cursor.fetchall()
    
    if resultados:
        print("Listado de personas registradas:")
        for registro in resultados:
            print("Nombre:", registro[0], "Edad:", registro[1], "Ciudad:", registro[2])
    else:
        print("No hay registros en la tabla Personas.")
    
    conexion.close()


# Función para actualizar la edad de una persona específica en la base de datos
def actualizar_persona():

    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre de la persona que desea actualizar: ")
    nueva_edad = int(input("Ingrese la nueva edad: "))
    
    cursor.execute("UPDATE Personas SET edad = ? WHERE nombre = ?",(nueva_edad, nombre))
    
    if cursor.rowcount > 0:
        print("La edad de", nombre, "ha sido actualizada con éxito.")
    else:
        print("No se encontró a una persona con ese nombre.")
    
    conexion.commit()
    conexion.close()


# Función para eliminar una persona específica de la base de datos
def eliminar_persona():
    
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre de la persona que desea eliminar: ")
    
    cursor.execute("DELETE FROM Personas WHERE nombre = ?", (nombre,))
    
    if cursor.rowcount > 0:
        print("La persona", nombre, "ha sido eliminada con éxito.")
    else:
        print("No se encontró a una persona con ese nombre.")
    
    conexion.commit()
    conexion.close()


# Función para buscar una persona en la base de datos
def buscar_persona():
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre de la persona que desea buscar: ")

    cursor.execute("SELECT * FROM Personas WHERE nombre = ?", (nombre,))
    
    resultado = cursor.fetchone()

    if resultado:
        print("Información de la persona encontrada:")
        print("Nombre:", resultado[0])
        print("Edad:", resultado[1])
        print("Ciudad:", resultado[2])
    else:
        print("No se encontró a una persona con ese nombre.")

    conexion.close()


# Función para generar un reporte de personas menores de 18 años
def reporte_menores_edad():

    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Personas WHERE edad < 18")
    resultados = cursor.fetchall()

    if resultados:
        print("Personas menores de edad:")
        for registro in resultados:
            print("Nombre:", registro[0], "Edad:", registro[1],"Ciudad:", registro[2])
    else:
        print("No se encontraron personas menores de edad.")
    
    conexion.close()


# Función del menú principal que permite acceder a cada función
def mostrar_menu():

    while True:
        print("\nMenú de Gestión de Personas:")
        print("1. Registrar persona")
        print("2. Mostrar personas")
        print("3. Actualizar edad de una persona")
        print("4. Eliminar persona")
        print("5. Buscar persona")
        print("6. Reporte de personas menores de edad")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_persona()
        elif opcion == "2":
            mostrar_personas()
        elif opcion == "3":
            actualizar_persona()
        elif opcion == "4":
            eliminar_persona()
        elif opcion == "5":
            buscar_persona()
        elif opcion == "6":
            reporte_menores_edad()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")


# Llamar a la función para crear la tabla
crear_tabla_personas()

# Llamar a la función para insertar datos
precargar_datos()

# Iniciar el programa llamando al menú principal
mostrar_menu()