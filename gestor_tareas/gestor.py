import json

from tareas import Tarea

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
            raise ValueError(f'La tarea debe ser entre el 1 y el {len(self.tareas)}')     

    def agregar(self, titulo):
        titulo = titulo.strip()
        if not titulo:
            raise ValueError('El titulo no puede estar vacio')
        self.tareas.append(Tarea(titulo))
        self.guardar()

    def ver(self):
        return self.tareas
    
    
    def modificar(self, numero):
        self.validar_numero(numero)
        self.tareas[numero - 1].completar()
        self.guardar()
    
    def eliminar(self, numero):
        self.validar_numero(numero)
        self.tareas.pop(numero - 1)
        self.guardar()

    def ver_pendientes(self):
        return [t for t in self.tareas if not t.completada]
    
    def ver_completadas(self):
        return [t for t in self.tareas if t.completada]

    def contar_pendientes(self):
        return sum(1 for t in self.tareas if not t.completada)
    
    def contar_completadas(self):
        return sum(1 for t in self.tareas if t.completada)

    def mas_larga(self):
        return max(self.tareas, key=lambda t: len(t.titulo), default=None)

    def ordenar(self):
        return sorted(self.tareas, key=lambda t:t.titulo)

    def hay_pendientes(self):
        return any(not t.completada for t in self.tareas)

    def todas_completadas(self):
        return (len(self.tareas) > 0 and all(t.completada for t in self.tareas))
    
