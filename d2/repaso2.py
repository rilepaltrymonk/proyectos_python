# repaso


def aprobados(calificacion):
    return calificacion >= 70

def promedio_general(alumnos):
    suma=0
    for alumno in alumnos:
        suma += alumno['calificacion']
    return suma/len(alumnos)

def contar_aprobados(alumnos):
    num_aprobados = 0

    for alumno in alumnos:
        if aprobados(alumno['calificacion']):
            num_aprobados += 1

    return num_aprobados

def sacar_promedio_segundo(alumnos):
    promedio_segundo = 0
    cantidad = 0
    for alumno in alumnos:
        if alumno['semestre']==2:
            promedio_segundo += alumno['calificacion']
            cantidad +=1
    if(cantidad == 0):
        return 0
    return promedio_segundo/cantidad


alumnos = []

alumnos.append({'nombre':'Emilio', 'calificacion': 78, 'semestre': 2})
alumnos.append({'nombre':'Norma', 'calificacion': 86, 'semestre': 2})
alumnos.append({'nombre':'Sharon', 'calificacion': 75, 'semestre': 3})
alumnos.append({'nombre':'Luisito', 'calificacion': 64, 'semestre': 2})
alumnos.append({'nombre':'Luisito', 'calificacion': 64, 'semestre': 3})

print('')
print('Usanso enumerate')
print('')

for i, alumno in enumerate(alumnos, start=1):
    if aprobados(alumno['calificacion']):
        print(i, alumno['nombre'], alumno['calificacion'], alumno['semestre'], 'APPROVED')

    else: 
        print(i, alumno['nombre'], alumno['calificacion'], alumno['semestre'], 'DISSAPPROVED')

print('\n')

print(f'El promedio grupal es de: {promedio_general(alumnos)} \n')   

mejor_alumno = alumnos[0]

for alumno in alumnos:
    if alumno['calificacion']>mejor_alumno['calificacion']:
        mejor_alumno= alumno


print(f'La mejor alumna es: {mejor_alumno['nombre']} con la calificacion de {mejor_alumno['calificacion']}')


print(f'Numero de aprobados: {contar_aprobados(alumnos)}')

promedio2 = sacar_promedio_segundo(alumnos)

print(f'El promedio de segundo semestre es: {promedio2}')