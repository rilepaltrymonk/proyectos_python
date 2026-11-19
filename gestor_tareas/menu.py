

def mostrar_menu():
    while True:
        try:
            opcion = int(input('Elige la opción deseada:\n'
                               '1. Agregar tarea\n'
                               '2. Completar tarea\n'
                               '3. Eliminar tarea\n'
                               '4. Ver tareas\n'
                               '5. Ver tareas ordenadas\n' \
                               '6. Tarea mas larga al momento\n'
                               '7. Ver tareas pendientes\n' \
                               '8. Ver resumen' \
                               '9. Salir\n'))

        except ValueError:
            print('Debe ser una opcion numerica y no una letra')
        else:
            if 1 <= opcion <= 8:
                return opcion
            print('Debe ser una opcion entre 1 y el 8')

def pedir_numero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print('Debe ser un numero no una letra')

def opcion_agregar(gestor):
    titulo = input('Ingresa el titulo de la tarea: \n')
    try:
        gestor.agregar(titulo)
        print('Tarea agregada')
    except ValueError as error:
        print(error)

def opcion_modificar(gestor):
    numero = pedir_numero('Ingresa el numero a completar:\n')
    if numero is None:
        print('No hay tareas en la lista')
        return
    try:
        gestor.modificar(numero)
        print('Tarea completada')
    except ValueError as error:
        print(error)

def opcion_eliminar(gestor):
    numero = pedir_numero('Ingresa el numero a eliminar\n')
    if numero is None:
        print('No hay tareas en la lista')
        return
    try:
        gestor.eliminar(numero)
        print('Tarea eliminada')
    except ValueError as error:
        print(error)

def opcion_ver(gestor):
    tareas = gestor.ver()
    if len(tareas) == 0:
        print('No hay tareas en la lista')
        return
    for i, tarea in enumerate(tareas, start= 1):
        print(i, tarea)

def opcion_ordenadas(gestor):
    ordenadas = gestor.ordenar()
    if len(ordenadas) == 0:
        print('No hay tareas en la lista')
        return
    for o in ordenadas:
        print(o)    

def opcion_ver_p(gestor):
    pendientes = gestor.ver_pendientes()
    if len(pendientes) == 0:
        print('No hay pendientes')
        return
    for p in pendientes:
        print(p)
    print('\n')    

def opcion_ver_c(gestor):
    pendientes = gestor.ver_completadas()
    if len(pendientes) == 0:
        print('No hay pendientes')
        return
    for p in pendientes:
        print(p)
    print('\n')

def opcion_mas_larga(gestor):
    mas_larga = gestor.mas_larga()
    if mas_larga is None:
        print('No hay tareas en la lista')
        return
    print(mas_larga)

def ver_resumen(gestor):
    tcompletas = gestor.todas_completadas()
    hpendientes = gestor.hay_pendientes()
    tareas = gestor.ver()
    if len(tareas) == 0:
        print('No hay tareas en la lista')
    elif tcompletas:
        print('Todas las tareas han sido completadas, felicidades')
    elif hpendientes:

        print(f'Completadas: {gestor.contar_completadas()}')
        opcion_ver_c(gestor)
        print(f'Pendientes:{gestor.contar_pendientes()}')
        opcion_ver_p(gestor)

