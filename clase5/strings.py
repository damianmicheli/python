nombre = "Alberto Torres"
print(nombre, "contiene", len(nombre), "caracteres.")

cadena1 = "Hola mundo!"
cadena2 = 'Hola mundo!'
cadena3 = "Hola 'mundo'"
cadena4 = 'Hola, "mundo"'
print(cadena1) # Imprime Hola mundo!
print(cadena2) # Imprime Hola mundo!
print(cadena3) # Imprime Hola 'mundo'
print(cadena4) # Imprime Hola, "mundo"

risa = "Ja "
carcajada1 = risa + risa + "Jaaaaaa!"
print(carcajada1) # Imprime Ja Ja Jaaaaaa!
carcajada2 = risa * 4
print(carcajada2) # Imprime Ja Ja Ja Ja
print("-"*20) # Imprime --------------------

# Definimos una cadena
palabra = "Python"
# Accedemos al primer carácter (índice 0)
primer_caracter = palabra[0]
print("El primer carácter es:", primer_caracter)
# Imprime El primer carácter es: P
# Accedemos al cuarto carácter (índice 3)
cuarto_caracter = palabra[3]
print("El cuarto carácter es:", cuarto_caracter)
# Imprime El cuarto carácter es: h

frase = "PythonEsAsombroso"
subcadena = frase[0:6]
print(subcadena)
# Imprime Python

texto = "Python"
# Acceso utilizando índices positivos
print("Índice 0:", texto[0]) # P
print("Índice 1:", texto[1]) # y


# Acceso utilizando índices negativos
print("Índice -1:", texto[-1]) # n
print("Índice -2:", texto[-2]) # o

frase = "Aprender Python es divertido"
# Subcadena desde el inicio hasta el índice 8 (sin incluirlo)
subcadena = frase[:8]
print("Subcadena desde el inicio hasta el índice 8:",
subcadena)
# Imprime Aprender
# Subcadena desde el índice 9 hasta el final
subcadena = frase[9:]
print("Subcadena desde el índice 9 hasta el final:",
subcadena)
# Imprime Python es divertido

texto = "Hola"
subcadena = texto[1:10]
print("Subcadena obtenida:", subcadena)
# Imprime ola

texto = "Talento Tech"
subcadena = texto[::2]
print("Subcadena obtenida:", subcadena)
# Imprime TlnoTc

print(not(5 > 3))