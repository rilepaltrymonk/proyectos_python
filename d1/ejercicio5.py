from datetime import date

anio_actual = date.today().year

def pedir_anio():

    while True:

        try:        
            anio = int(input('Dame tu año de nacimiento: '))
            
        except ValueError:
            print('Debes de escribir un numero por ejemplo: 1994')

        else:        
            if anio<1900:
                print('El año es muy viejo')
                continue
    
            if anio > anio_actual:
                print('Ese año aun no ha llegado')
                continue
            return anio    

def calcular_edad(anio):
    return anio_actual-anio 


def es_mayor(edad):
    return edad>=18


nombre = input('Dame tu nombre: ')
anio = pedir_anio()
edad = calcular_edad(anio)

if es_mayor(edad):
    print(f'Hola {nombre}, tu edad aproximada es {edad} años, y eres mayor de edad')

else:
    print(f'Hola {nombre}, tu edad aproximada es {edad} años, y eres menor de edad')
 