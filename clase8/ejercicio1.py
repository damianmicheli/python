'''
Registro de ventas por día:
Desarrollá un programa que permita registrar las ventas diarias de un comercio durante
cinco días. Al finalizar, el sistema debe mostrar el total de ventas realizadas en cada día y el
promedio de ventas.
Tips:
● Utilizá un bucle while que permita a la persona usuaria ingresar el monto de las
ventas diarias.
● Asegurate de validar que el monto ingresado sea un valor positivo.
● Usá un acumulador para la suma de las ventas.
'''

total_productos = 0 # Inicializamos el contador
acumulador_ventas = 0
dias_de_ventas = 5
for dia in range(dias_de_ventas):# Supongamos que ingresamos productos durante 5 días
    print("Día",dia + 1, ":")
    productos_vendidos = int(input("Productos vendidos en el día: "))
    total_productos += 1
    acumulador_ventas += productos_vendidos
# Cada vez que agregamos productos, sumamos 1 al contador
print("Se ingresaron",total_productos,"productos en total al inventario.")
print(f'Se acumularon {acumulador_ventas} productos')