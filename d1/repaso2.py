from datetime import date

anio_actual = date.today().year

def pedir_anio():
    while True:
        try:
            anio = int(input('Ingresa tu año de nacimiento: '))
        except ValueError:
            print('Estas escribiendo letras, ejemplo 1994')
        else:
            if anio > anio_actual:
                print('El año aun no llega')
                continue
            if anio < 1900:
                print('El año es muy viejo')
                continue
            return anio    

def calcular_edad(anio):
    return anio_actual - anio

def es_mayor(edad):
    return edad >= 18

nombre = input('Ingresa tu nombre: ')
anio = pedir_anio()
edad = calcular_edad(anio)
if es_mayor(edad):
    print(f'Hola {nombre}, tu edad aproximada es {edad} años, y eres mayor de edad')
else:
    print(f'Hola {nombre}, tu edad aproximada es {edad} años, y eres menor de edad') 