
def aproved(calificacion):
    return calificacion >= 70 

# def sacar_promedio(suma):
#     return suma/len(alumnos)    

def sacar_promedio1(alumnos):
    suma1 = 0
    for alumno in alumnos:
        suma1 += alumno['calificacion']
    return suma1/len(alumnos)    

alumnos = []

alumnos.append({'nombre': 'Emilio', 'calificacion': 95, 'semestre': 3})
alumnos.append({'nombre': 'Sharon', 'calificacion': 59, 'semestre': 1})
alumnos.append({'nombre': 'Norma', 'calificacion': 92, 'semestre': 2})
alumnos.append({'nombre': 'Fabian', 'calificacion': 99, 'semestre': 2})

print('Lista usando una funcion')

for i, alumno in enumerate(alumnos,  start=1):

    if aproved(alumno['calificacion']): 
        print(i, alumno['nombre'], alumno['calificacion'], 'aprobado')
    else:
        print(i, alumno['nombre'], alumno['calificacion'], 'desaprobado')

print('Lista usando condicional directo')

for i, alumno in enumerate(alumnos, start=1):
    if alumno['calificacion']<70 :
        print(i, alumno['nombre'], alumno['calificacion'], 'desaprobado')
    else:
        print(i, alumno['nombre'], alumno['calificacion'], 'aprobado')

# suma=0

# for i, alumno in enumerate(alumnos, start=1):
#     promedio = alumno['calificacion']
#     suma=promedio+suma

# print(sacar_promedio(suma))
print(sacar_promedio1(alumnos))

print(alumnos[1]['calificacion'])

alumno_sobresaliente = alumnos[0]

for alumno in alumnos:
    if alumno['calificacion']>alumno_sobresaliente['calificacion']:
        alumno_sobresaliente=alumno


print(alumno_sobresaliente)