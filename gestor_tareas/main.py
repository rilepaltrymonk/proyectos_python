from gestor import GestorTareas
from menu import *

ARCHIVO_TAREAS = 'tareas.json'

def main():

    gestor = GestorTareas(ARCHIVO_TAREAS)
    gestor.cargar()


    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            opcion_agregar(gestor)
        elif opcion == 2:
            opcion_modificar(gestor)
        elif opcion == 3:
            opcion_eliminar(gestor)
        elif opcion == 4:
            opcion_ver(gestor)
        elif opcion == 5:
            opcion_ordenadas(gestor)
        elif opcion == 6:
            opcion_mas_larga(gestor)
        elif opcion == 7:
            opcion_ver_p(gestor)
        elif opcion == 8:
            ver_resumen(gestor)
        elif opcion == 9:
            print('Gracias')
            break

if __name__ == '__main__':
    main()