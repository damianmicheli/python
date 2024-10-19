
# Vamos a escribir un programa que calcule el costo total de una salida a cenar para un grupo
# de personas. En el mismo se pide la cantidad de personas, el precio promedio del plato y
# una propina fija del 10%.


cantidad_personas = int(input("Ingrese la cantidad de personas: "))
precio_promedio_plato = float(input("Ingrese el precio promedio del plato: "))
porcentaje_propina = 10

monto = cantidad_personas * precio_promedio_plato

propina = monto * porcentaje_propina / 100

total = monto + propina

print(f"El costo total de la salida es de ${total:.2f}")