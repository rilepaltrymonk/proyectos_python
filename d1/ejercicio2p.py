from datetime import date

nombre = input('Dame tu nombre: ')
anio = int(input('Dame tu año de nacimiento: '))
edad = date.today().year - anio

if(edad>18):
    print(f'Hola {nombre}, tu edad aproximada son {edad} años de edad y eres mayor de edad') 
else:
    print(f'Hola {nombre}, tu edad aproximada son {edad} años de edad y eres menor de edad')