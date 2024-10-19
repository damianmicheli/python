numero = 5
if numero > 0:
   print("El número es positivo.")
elif numero < 0:
    print("el numero es negativo")
else:
    print("el numero es cero")

edad = 18
tiene_licencia = False

if edad >= 18:
    if tiene_licencia: print("Podés conducir.")
    else: print("No podés conducir porque no tenés licencia.")
else: print("No tenés la edad suficiente para conducir.")

nota = 59
if nota >= 60:
    print("¡Aprobaste!")
    if nota >= 90: 
        print("¡Excelente calificación!")
    elif nota >= 75: 
        print("Muy buen trabajo.")
    else: 
        print("Buen esfuerzo, pero hay margen de mejora.")
else: 
    print("No alcanzaste la calificación mínima para aprobar.")