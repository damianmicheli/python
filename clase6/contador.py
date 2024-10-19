total_productos = 0 # Inicializamos el contador
acumulador_productos = 0
for dia in range(3):# Supongamos que ingresamos productos durante 3 días
    print("Día",dia + 1, ":")
    productos_agregados = int(input("Productos ingresados en el día: "))
    total_productos += 1
    acumulador_productos += productos_agregados
# Cada vez que agregamos productos, sumamos 1 al contador
print("Se ingresaron",total_productos,"productos en total al inventario.")
print(f'Se acumularon {acumulador_productos} productos')