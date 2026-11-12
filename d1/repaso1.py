from datetime import date

anio_actual = date.today().year

def pedir_añio ():
    
    while True:
        try:
            anio = int(input('Ingresa tu año de nacimieto'))
        
        except ValueError:
            print('Ese no es un año, ejemplo 1994')

        else:
            if anio <= 1900:
                print('Es un año muy viejo')
                continue
            
            if anio > anio_actual:
                print('Ese año aun no llega')
                continue
        
            return anio

def calcular_edad (anio):
    return anio_actual - anio

def es_mayor (edad):
    return edad >= 18

nombre = input('Escribe tu nombre')
anio = pedir_añio()
edad = calcular_edad(anio)

if es_mayor(edad):
    print(f'Hola {nombre}, tu edad aproximada es {edad} años, y eres mayor de edad')
else:
    print(f'Hola {nombre}, tu edad aproximada es {edad} años, y eres menor de edad')
