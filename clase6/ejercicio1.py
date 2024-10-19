'''
1) Control de stock de productos:
Desarrollá un programa que permita a quienes interactúen con él ingresar el nombre de
varios productos y la cantidad en stock que hay de cada uno. El programa debe seguir
pidiendo que ingrese productos hasta que el usuario decida salir, ingresando "salir" como
nombre de producto. Después de que el bucle termine el programa debe mostrar la cantidad
total de productos ingresados.
Tips:
● Vas a necesitar un contador.
● Tené presente las estructuras condicionales.
'''
titulo = 'Stock de productos'
print('\n',titulo)
print('-' * (len(titulo)+2),'\n')
contador = 0
producto = input('Ingrese nombre del producto (salir para terminar): ')
while producto != 'salir':
    stock = int(input('Ingrese cantidad: '))
    contador += 1
    producto = input('Ingrese nombre del producto (salir para terminar): ')

print(f'Cantidad total de productos ingresados: {contador}')