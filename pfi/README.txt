#-------------------------------------
# Talento Tech
# Proyecto Final Integrador
#
# SISTEMA DE GESTION DE INVENTARIO
#
# Damián Micheli - 2024
#-------------------------------------


README


Descripción del sistema:

El SISTEMA DE GESTION DE INVENTARIO es una aplicación en Python que permite 
gestionar el inventario de una pequeña tienda.
La aplicación es capaz de registrar, actualizar, eliminar y mostrar productos
en el inventario.
Además, incluye funcionalidades para realizar búsquedas, generar reportes de
stock y registrar ventas.


Requerimientos:

La aplicación requiere Python 3 instalado, y utiliza la libreria Colorama, la cual
deberá ser instalada si no se encuentra disponible en el sistema.


Ejecución:

Para iniciar la aplicación se debe posicionar en el directorio que contiene el archivo
"inventario.py" desde la terminal o consola y ejecutar el siguiente comando:

    python3 inventario.py

Si existe un archivo de base de datos "inventario.db" se utilizará el mismo, caso contrario
se creará uno nuevo con datos de prueba.


Funcionalidad:

El sistema cuenta con las siguientes opciones:

* Registrar producto: La aplicación permite al usuario
agregar nuevos productos al inventario, solicitando los
siguientes datos: nombre, descripción, cantidad, precio y
categoría.

* Mostrar productos: La aplicación muestra todos los productos
registrados en el inventario, incluyendo su ID, nombre, 
descripción, cantidad, precio y categoría.

* Actualizar producto: La aplicación permite al usuario 
actualizar la cantidad disponible de un producto
específico utilizando su ID.

* Eliminar producto: La aplicación permite al usuario eliminar
un producto del inventario utilizando su ID.

* Buscar producto: La aplicación permite buscar productos por
su ID, mostrando los detalles del producto encontrado.

* Reporte de Bajo Stock: La aplicación permite generar un reporte
de productos que tengan una cantidad igual o inferior a un
límite especificado por el usuario

* Vender producto: La aplicación permite registrar la venta de
productos por su ID, actualizando el stock disponible.