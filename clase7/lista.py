compras = ["manzanas", "pan", "leche", "queso"]
print(compras[0])
# Imprime "manzanas"
print(compras[2])
# Imprime "leche"
compras[1] = "yogur"
print(compras)
# Ahora la lista es ["manzanas", "yogur", "leche","queso"]
compras.append("cereales")
print(compras)
# Ahora la lista es ["manzanas", "yogur", "leche", "queso", "cereales"]
compras.remove('leche')
print(compras)
print(len(compras))

indice = 0
while indice < len(compras):
        print(f'Producto {indice + 1}: {compras[indice]}')
        indice += 1