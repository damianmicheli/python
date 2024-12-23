'''

Generación de valores únicos con random
Escribe un programa en Python que genere cinco códigos únicos de cinco
 dígitos para usarlos como identificadores de productos en un inventario. 
 Para esto, utiliza el módulo random. Cada código generado debe ser diferente
   de los otros.
Tip: Puedes usar random.randint() para generar números dentro de un rango 
determinado.

'''
from random import randint

valores = []

def valor_ya_existe(valor_buscado):
    existe = False
    for valor in valores:
        if valor == valor_buscado:
            existe = True
            break
    
    return existe

for _ in range (5):
    nuevo_valor = randint(10000,99999)
    while valor_ya_existe(nuevo_valor):
            nuevo_valor = randint(10000,99999)

    valores.append(nuevo_valor)

print (valores)