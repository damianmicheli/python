# Consumo de combustible
# En este ejercicio, vas a crear una aplicación en Python que calcule el consumo de
# combustible de un coche durante un viaje. El programa va a solicitar para funcionar que se
# ingrese cuántos litros de combustible gasta el auto por cada 100 km, el costo por litro del
# mismo y la distancia del viaje. Con estos datos, tu programa va a calcular cuánto consumió
# el vehículo y cuánto dinero se gastó en combustible.

consumo = float(input("Ingrese litros consumidos cada 100km: "))
costo_combustible = float(input("Ingrese el costo de un litro de combustible: "))
distancia = float(input("Ingrese la distancia del viaje en km: "))

consumido = consumo / 100 * distancia
monto = consumido * costo_combustible

print(f"El vehículo consumió {consumido:.2f} litros de combustible.")
print(f"Se gastó ${monto:.2f}")