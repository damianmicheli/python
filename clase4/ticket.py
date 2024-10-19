# Ticket de compra
# ¡Vamos a crear tu propio ticket de compra! El desafío es escribir un programa que le pida al
# usuario el nombre, la cantidad y el valor unitario de tres productos. Después, tu programa
# tiene que calcular el importe de IVA (21%) de cada uno y mostrar en la terminal un ticket de
# compra con todos los datos.

iva = 21

nombre1 = input("Ingrese nombre de producto: ")
cantidad1 = int(input("Ingrese cantidad: "))
valor_unitario1 = float(input("Ingrese valor unitario: "))
subtotal1 = cantidad1 * valor_unitario1

nombre2 = input("Ingrese nombre de producto: ")
cantidad2 = int(input("Ingrese cantidad: "))
valor_unitario2 = float(input("Ingrese valor unitario: "))
subtotal2 = cantidad2 * valor_unitario2

nombre3 = input("Ingrese nombre de producto: ")
cantidad3 = int(input("Ingrese cantidad: "))
valor_unitario3 = float(input("Ingrese valor unitario: "))
subtotal3 = cantidad3 * valor_unitario3

total = (subtotal1 + subtotal1 + subtotal3) * (1 + iva / 100)

print("GRACIAS POR SU COMPRA")
print("Producto\tCantidad\tPrecio\tSubtotal")
print(f"{nombre1}\t\t{cantidad1}\t\t{valor_unitario1}\t{subtotal1}")
print(f"{nombre2}\t\t{cantidad2}\t\t{valor_unitario2}\t{subtotal2}")
print(f"{nombre3}\t\t{cantidad3}\t\t{valor_unitario3}\t{subtotal3}")
print(f"Total: {total}")