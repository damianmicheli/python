# Creá un programa que solicite el ingreso de dos números enteros. Realizá las siguientes
# operaciones: suma, resta, multiplicación y módulo. Luego, mostrá el resultado de cada
# operación en un formato claro. Asegurate de incluir mensajes personalizados que expliquen
# cada resultado, por ejemplo: "La suma de tus números es: X".

primer_numero = int(input("Ingresá un número entero: "))
segundo_numero = int(input("Ingresá otro número entero: "))

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
modulo = primer_numero % segundo_numero

print(f"La suma de tus números es: {suma}")
print(f"La resta de tus números es: {resta}")
print(f"La multiplicación de tus números es: {multiplicacion}")
print(f"El módulo de tus números es: {modulo}")