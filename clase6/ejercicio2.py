'''
2) Validación de precios de productos:
Escribí un programa que permita ingresar el precio de un producto, pero que sólo acepte
valores mayores a 0. Si la persona ingresa un valor inválido (negativo o cero), el programa
debe mostrar un mensaje de error y solicitar nuevamente el valor hasta que se ingrese uno
válido. Al final, el programa debe mostrar el precio aceptado.
Tips:
● Antes de empezar, pensá si es necesario usar contadores o acumuladores.
● Recordá que input() siempre devuelve cadenas de caracteres.
'''

precio = float(input("Ingresá el precio del producto: "))

while precio <= 0:
    print("Error: El monto debe ser mayor que 0.")
    precio = float(input("Por favor, ingresá nuevamente el precio del producto: "))
print(f"Has ingresado un precio válido: ${precio:.2f}")