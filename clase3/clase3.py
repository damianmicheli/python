# input/print

nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre}")
edad = int(input("Ingresá tu edad: "))
print(f"Tenés {edad + 5} años.")


# operaciones
import math # Importamos el módulo math para usar Pi
radio = 5
area = math.pi * (radio ** 2)
# Calculamos el área
print(f"El área del círculo con radio {radio} es {area:.2f}") # 2 decimales