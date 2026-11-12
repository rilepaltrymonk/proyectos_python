# gestor de tareas

import json

GESTOR_TAREAS = 'tareas.json'

def mostrar_menu ():
    while True:
        try: 
            opcion = int(input('Elige la opción deseada: \n'
                '1. Agregar \n'
                '2. Ver \n'
                '3. Completar \n'
                '4. Eliminar \n'
                '5. Salir \n'))

        except ValueError:
            print('Ingresa un numero no una letra')

        else:
            if 1 <= opcion <= 5:
                return opcion
            else:
                print('La opcion debe ser del 1 al 5')
        
def agregar_tarea(tareas):
    tarea = input('Ingresa un titulo: ').strip()
    if not tarea:
        print('El titulo no puede estar vacio')
        return
    tareas.append({'titulo': tarea, 'completada': False})
    guardar_tareas(tareas)

def ver_tareas(tareas):
    for i, tarea in enumerate(tareas, start=1):
        if tarea['completada'] :
            print(i, f"{tarea['titulo']}, completada")
        else:
            print(i, f"{tarea['titulo']}, pendiente")
    if len(tareas)==0:
        print('No hay tareas')

def completar_tarea(tareas):

    if len(tareas) == 0 :
        print('No hay tareas en la lista')
        return

    while True:
        try:
            tarea_completada = int(input('Ingresa la tarea que quieres completar: '))

        except ValueError:
            print('Debe ser un numero y no una letra')

        else:
            if tarea_completada <= 0 :
                print('El numero de la tarea seleccionada debe ser mayor a 0')
            elif tarea_completada>len(tareas):
                print('El numero de tarea no existe')
            else:
                tarea_completada = tarea_completada-1
                tareas[tarea_completada]['completada'] = True
                guardar_tareas(tareas)
                print('Tarea completada')
                break    

def eliminar_tarea(tareas):
    
    if len(tareas) == 0:
        print('No hay tareas en la lista')
        return
    
    while True:
        try:
            tarea_a_eliminar = int(input('Ingresa el numero de la tarea a eliminar: '))
            
        except ValueError:
            print('Debe ser un numero y no una letra')

        else: 
            if tarea_a_eliminar <= 0 :
                print('La tarea a eliminar tiene que ser mayor a 0')
            elif tarea_a_eliminar>len(tareas) :
                print('El numero de la tarea a eliminar no existe')
            else:
                tarea_a_eliminar = tarea_a_eliminar-1
                tareas.pop(tarea_a_eliminar)
                guardar_tareas(tareas)
                print('Tarea eliminada')
                break

def guardar_tareas(tareas):
    with open(GESTOR_TAREAS, 'w', encoding='UTF-8') as archivo:
        json.dump(tareas, archivo, ensure_ascii=False)    

def cargar_tareas():

    try:
    
        with open(GESTOR_TAREAS, 'r', encoding='UTF-8') as archivo:
            lista_tareas = json.load(archivo)    
    
    except (FileNotFoundError, json.JSONDecodeError):
        return []


    if not isinstance(lista_tareas, list):
        print('El archivo no tiene el formato esperado')
        return []
    
    return lista_tareas



tareas = cargar_tareas()

while True:
    opcion = mostrar_menu()


    if opcion == 1:
        agregar_tarea(tareas)

    elif opcion == 2:
        ver_tareas(tareas)

    elif opcion == 3:
        completar_tarea(tareas)
    
    elif opcion == 4:
        eliminar_tarea(tareas)

    elif opcion == 5:
        print('Gracias por usar el servicio')
        break