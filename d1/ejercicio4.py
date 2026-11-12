from datetime import date

nombre = input('Dame tu nombre: ')
anio_actual = date.today().year

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

        edad = anio_actual - anio

        if edad >= 18:
            print(f'Hola {nombre}, tu edad aproximada son {edad} años de edad y eres mayor de edad') 
        else:
            print(f'Hola {nombre}, tu edad aproximada son {edad} años de edad y eres menor de edad')

        break