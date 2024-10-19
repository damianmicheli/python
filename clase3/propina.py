# Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante.
# El script debe solicitar el monto total de la cuenta y el porcentaje de propina que deseás
# dejar. Utilizando operadores aritméticos, calculá la cantidad de propina y el total a pagar
# (incluyendo la propina). Finalmente, mostrá los resultados en la pantalla.

monto = float(input("ingrese el monto: "))
porcentaje_propina = int(input("ingrese porcentaje de propina: "))

propina = monto * porcentaje_propina / 100

total = monto + propina

print(f"El monto de tu ticket es de ${monto:.2f}")
print(f"El porcentaje de propina es el {porcentaje_propina}% del monto.")
print(f"La propina es de ${propina:.2f}")
print(f"El total es de ${total:.2f}")
