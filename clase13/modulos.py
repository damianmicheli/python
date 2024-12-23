import math
# Redondear hacia abajo
numero = 4.7
redondeado = math.floor(numero)
print("El número redondeado hacia abajo es:", redondeado)
# Calcular la raíz cuadrada de un número
raiz = math.sqrt(16)
print("La raíz cuadrada de 16 es:", raiz)


import random
# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print("Número aleatorio entre 1 y 10:", numero_aleatorio)
# Seleccionar un elemento aleatorio de una lista
colores = ["rojo", "verde", "azul", "amarillo"]
color_aleatorio = random.choice(colores)
print("Color aleatorio:", color_aleatorio)


from math import sqrt
# Ahora podemos usar sqrt directamente sin escribir math.
raiz = sqrt(25)
print("La raíz cuadrada de 25 es:", raiz)