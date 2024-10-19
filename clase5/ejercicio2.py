''' 
Sistema de calificaciones de una universidad.

Imagina que estás desarrollando un sistema que le ayude a un docente a clasificar a sus
estudiantes según sus calificaciones. El programa debe permitir ingresar la nota de un
estudiante y luego clasificarla según las siguientes categorías:

90 o más: "Excelente"
75 a 89: "Muy bueno"
60 a 74: "Bueno"
Menos de 60: "No aprobado"
'''

nota = float(input('Ingrese la nota: '))

if nota >= 90:
    print('Excelente')
elif nota >=75:
    print('muy bueno')
elif nota >= 60:
    print('bueno')
else:
    print('desaprobado')