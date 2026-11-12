import json

ARCHIVO_TAREAS = 'tareas.json'

class Tarea:

    def __init__(self, titulo):
        self.titulo = titulo
        self.completada = False

    def completar(self):
        self.completada = True

    def __str__(self):
        if self.completada:
            return f'{self.titulo}, completada'
        else:
            return f'{self.titulo}, pendiente'

    def a_diccionario(self):
        return {'titulo': self.titulo, 'completada': self.completada}

    @classmethod
    def desde_diccionario(cls, datos):
        nueva = cls(datos['titulo'])
        nueva.completada = datos['completada']
        return nueva

class GestorTareas:

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.tareas = []


    def guardar(self):
        datos = []

        for tarea in self.tareas:
            datos.append(tarea.a_diccionario())

        with open(self.nombre_archivo, 'w', encoding = 'UTF-8') as archivo:
            json.dump(datos, archivo, ensure_ascii = False)

    def cargar(self):
        try:
            with open(self.nombre_archivo, 'r', encoding = 'UTF-8') as archivo:
                datos = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tareas = []
            return
        if not isinstance(datos, list):
            self.tareas = []
            return
        self.tareas = [Tarea.desde_diccionario(d) for d in datos]

    def validar_numero(self, numero):
        if len(self.tareas) == 0:
            raise ValueError('No hay tareas en la lista')
        if not 1 <= numero <= len(self.tareas):
            raise ValueError(f'El numero debe ser entre el 1 y el {len(self.tareas)}')

    def agregar(self, titulo):
        titulo = titulo.strip()
        if not titulo:
            raise ValueError('El titulo no puede estar vacío')
        self.tareas.append(Tarea(titulo))
        self.guardar()

    def modificar(self, numero):
        self.validar_numero(numero)
        self.tareas[numero - 1].completar()
        self.guardar()
    
    def eliminar(self, numero):
        self.validar_numero(numero)
        self.tareas.pop(numero - 1)
        self.guardar()

    def ver(self):
        return self.tareas        

    def ver_pendientes(self):
        return [t for t in self.tareas if not t.completada]

    def ver_completadas(self):
        return [t for t in self.tareas if t.completada]

    def mas_larga(self):
        return max(self.tareas, key = lambda t:len(t.titulo), default = None)

    def contar_pendientes(self):
        return sum(1 for t in self.tareas if not t.completada)

    def hay_pendientes(self):
        return any(not t.completada for t in self.tareas)

    def todas_completadas(self):
        return (len(self.tareas) > 0 and all(t.completada for t in self.tareas))

def mostrar_menu():
    while True:
        try: 
            opcion = int(input('Opciones'))
        except ValueError:
            print('Tiene que ser un numero, no una letra')
        else:
            if 1 <= opcion <= 8:
                return opcion
            print('Tiene que ser un numero dentro del 1 al 5')

def pedir(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print('Debe ser un numero no una letra')

def opcion_agregar(gestor):
    titulo = input('Ingresa el titulo de la tarea')
    try:
        gestor.agregar(titulo)
        print('Tarea agregada')
    except ValueError as error:
        print(error) 


def opcion_modificar(gestor):
    numero = pedir('Ingresa el numero a modificar')
    if numero is None:
        print('No existe la tarea')
    try:
        gestor.modificar(numero)
        print('Tarea completada')
    except ValueError as error:
        print(error)

def opcion_eliminar(gestor):
    numero = pedir('Ingresa el numero a eliminar')
    if numero is None:
        print('No existe la tarea')
    try:
        gestor.eliminar(numero)
        print('Tarea eliminada')
    except ValueError as error:
        print(error)

def opcion_ver(gestor):
    tareas =  gestor.ver()
    if len(tareas) == 0:
        print('No hay tareas en la listass')

    for i, tarea in enumerate(tareas, start = 1):
        print(i, tarea)

def opcion_ver_pendientes(gestor):
    pendientes = gestor.ver_pendientes()
    if len(pendientes) == 0:
        print('No hay pendientes')
    for tarea in pendientes:
        print(tarea)

def opcion_tareas_larga(gestor):
    mas_larga = gestor.mas_larga()
    if mas_larga is None:
        print('No hay tareas en la lista')
        return
    print(mas_larga)

def ver_resumen(gestor):
    t_completas = gestor.todas_completadas()
    alguna_pendiente = gestor.hay_pendientes()
    if t_completas:
        print('Todas las tareas estan completas')
    if alguna_pendiente:
        n_pendientes = gestor.contar_pendientes()
        completadas = gestor.ver_completadas()
        pendientes = gestor.ver_pendientes()
        print(f'Pendientes: {n_pendientes}')
        for p in pendientes:
            print(p)
        for c in completadas:
            print(c)

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
        opcion_ver_pendientes(gestor)
    elif opcion == 6:
        opcion_tareas_larga(gestor)
    elif opcion == 7:
        ver_resumen(gestor)
    elif opcion == 8:
        print('Gracias')
        break
        
















