
import json

# Constante: el nombre del archivo donde se guardan las tareas.
ARCHIVO_TAREAS = 'tareas.json'


# CLASE 1: Tarea  (el "molde" de una tarea individual)
class Tarea:
    # __init__ es el constructor: se ejecuta solo al hacer Tarea('algo').
    # 'self' es "este objeto". 'titulo' es el dato que pasamos al crearla.
    def __init__(self, titulo):
        self.titulo = titulo
        self.completada = False

    # Método: cambia el estado de ESTA tarea a completada.
    def completar(self):
        self.completada = True

    # Convierte el objeto en diccionario. JSON no sabe guardar objeto. Se usa al GUARDAR.
    def a_diccionario(self):
        return {'titulo': self.titulo, 'completada': self.completada}

    # Define cómo se ve la tarea al hacer print(tarea).
    # Debe DEVOLVER el texto con return, no imprimirlo.
    def __str__(self):
        if self.completada:
            return f'{self.titulo}, completada'
        else:
            return f'{self.titulo}, pendiente'

    # @classmethod: método que se llama desde la CLASE (Tarea.desde_diccionario)
    # y no desde un objeto. Sirve para CREAR objetos.
    # 'cls' es la clase misma, así que cls(...) equivale a Tarea(...).
    # Se usa al CARGAR (diccionario -> objeto).
    @classmethod
    def desde_diccionario(cls, datos):
        # Creamos la tarea con el título que venía en el diccionario.
        nueva = cls(datos['titulo'])
        # __init__ la deja en False, así que restauramos el estado guardado.
        nueva.completada = datos['completada']
        # Devolvemos el objeto ya armado.
        return nueva


# =====================================================================
# CLASE 2: GestorTareas  (maneja la lista de tareas y el archivo)
# =====================================================================
class GestorTareas:

    # Recibe el nombre del archivo y crea la lista vacía de tareas.
    def __init__(self, nombre_archivo):
        # Dato 1 del gestor: el nombre del archivo.
        self.nombre_archivo = nombre_archivo
        # Dato 2 del gestor: la lista de OBJETOS Tarea (empieza vacía).
        self.tareas = []

    # ----------------------------------------------------------------
    # GUARDAR: lista de objetos -> lista de diccionarios -> archivo
    # ----------------------------------------------------------------
    def guardar(self):
        # Paso 1: convertir cada objeto Tarea en diccionario.
        datos = []
        for tarea in self.tareas:
            # 'tarea' es un OBJETO, por eso usa su método con punto.
            datos.append(tarea.a_diccionario())

        # Paso 2: abrir el archivo en modo escritura ('w').
        # Si existe lo reemplaza; si no, lo crea.
        # 'with' lo cierra solo al terminar el bloque.
        # encoding='UTF-8' evita problemas con ñ y acentos.
        with open(self.nombre_archivo, 'w', encoding='UTF-8') as archivo:
            # Paso 3: escribir la lista de diccionarios en el archivo.
            # El segundo parámetro es 'archivo' (lo que va después de 'as').
            # ensure_ascii=False guarda la ñ como ñ y no como \u00f1.
            json.dump(datos, archivo, ensure_ascii=False)

    # ----------------------------------------------------------------
    # CARGAR: archivo -> lista de diccionarios -> lista de objetos
    # ----------------------------------------------------------------
    def cargar(self):
        # Paso 1: intentar leer el archivo.
        try:
            # 'r' = modo lectura.
            with open(self.nombre_archivo, 'r', encoding='UTF-8') as archivo:
                # json.load devuelve la lista de diccionarios.
                datos = json.load(archivo)
        # FileNotFoundError: el archivo no existe (primera ejecución).
        # json.JSONDecodeError: el archivo está dañado o vacío.
        except (FileNotFoundError, json.JSONDecodeError):
            self.tareas = []
            # return sin valor: termina el método aquí.
            return

        # Paso 2: el JSON puede ser válido pero no ser una lista (ej: 5).
        # isinstance(valor, list) responde True si es una lista.
        if not isinstance(datos, list):
            self.tareas = []
            return

        # Paso 3: convertir cada diccionario en objeto Tarea.
        # Empezamos con la lista vacía para no duplicar si se llama dos veces.
        self.tareas = []
        for d in datos:
            # Se llama desde la CLASE porque el objeto todavía no existe.
            self.tareas.append(Tarea.desde_diccionario(d))

    # ----------------------------------------------------------------
    # VALIDAR NÚMERO (método auxiliar para no repetir código)
    # ----------------------------------------------------------------
    # El usuario ve las tareas numeradas desde 1, pero la lista empieza en 0.
    # Aquí solo revisamos que el número sea válido; la resta de 1 se hace
    # en quien lo usa.
    def validar_numero(self, numero):
        if len(self.tareas) == 0:
            # raise lanza un error con mensaje; el método se detiene aquí.
            raise ValueError('No hay tareas en la lista')
        # Rango válido: de 1 a la cantidad de tareas.
        # Esto también rechaza 0 y negativos (que en listas son trampa).
        if not 1 <= numero <= len(self.tareas):
            raise ValueError(f'El número debe estar entre 1 y {len(self.tareas)}')

    # ----------------------------------------------------------------
    # AGREGAR
    # ----------------------------------------------------------------
    def agregar(self, titulo):
        # .strip() quita espacios sobrantes al inicio y al final.
        titulo = titulo.strip()
        # Un texto vacío cuenta como falso; 'not' lo invierte.
        if not titulo:
            raise ValueError('El título no puede estar vacío')
        # Creamos el objeto Tarea y lo metemos a la lista.
        self.tareas.append(Tarea(titulo))
        # self.guardar() llama otro método del MISMO objeto.
        self.guardar()

    # ----------------------------------------------------------------
    # COMPLETAR
    # ----------------------------------------------------------------
    def completar(self, numero):
        # Si el número es inválido, aquí mismo se lanza el error.
        self.validar_numero(numero)
        # Restamos 1: el usuario ve desde 1, la lista empieza en 0.
        # Luego llamamos al completar() de ESA tarea (de la clase Tarea).
        self.tareas[numero - 1].completar()
        self.guardar()

    # ----------------------------------------------------------------
    # ELIMINAR
    # ----------------------------------------------------------------
    def eliminar(self, numero):
        self.validar_numero(numero)
        # pop(indice) quita el elemento de esa posición.
        self.tareas.pop(numero - 1)
        self.guardar()

    # ----------------------------------------------------------------
    # VER: solo devuelve la lista; imprimir le toca al menú
    # ----------------------------------------------------------------
    def ver(self):
        return self.tareas


# =====================================================================
# FUNCIONES DEL MENÚ (aquí SÍ hay input y print)
# =====================================================================

# Muestra las opciones y devuelve la opción elegida (1 a 5), ya validada.
def mostrar_menu():
    while True:
        try:
            # int(input(...)): input por dentro, int por fuera.
            opcion = int(input('\nElige la opción deseada:\n'
                               '1. Agregar\n'
                               '2. Ver\n'
                               '3. Completar\n'
                               '4. Eliminar\n'
                               '5. Salir\n'))
        except ValueError:
            # Escribieron letras: avisamos y el ciclo repite.
            print('Ingresa un número, no una letra')
        else:
            # Solo se llega aquí si int() funcionó.
            if 1 <= opcion <= 5:
                return opcion
            print('La opción debe ser del 1 al 5')


# Pide un número al usuario. Devuelve el número, o None si escribió letras.
def pedir_numero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print('Debe ser un número, no una letra')
        return None


# Opción 1: pide el título y se lo pasa al gestor.
def opcion_agregar(gestor):
    titulo = input('Ingresa un título: ')
    try:
        gestor.agregar(titulo)
        print('Tarea agregada')
    except ValueError as error:
        # 'as error' guarda el error; print(error) muestra SU mensaje.
        print(error)


# Opción 2: recorre la lista del gestor e imprime cada tarea.
def opcion_ver(gestor):
    tareas = gestor.ver()
    if len(tareas) == 0:
        print('No hay tareas')
        return
    # enumerate(..., start=1) da el número (desde 1) y la tarea.
    for i, tarea in enumerate(tareas, start=1):
        # print(tarea) usa el __str__ de la clase Tarea.
        print(i, tarea)


# Opción 3: pide el número y se lo pasa al gestor.
def opcion_completar(gestor):
    numero = pedir_numero('Número de la tarea a completar: ')
    # None significa que escribió letras; ya se avisó, salimos.
    if numero is None:
        return
    try:
        gestor.completar(numero)
        print('Tarea completada')
    except ValueError as error:
        print(error)


# Opción 4: igual que completar, pero elimina.
def opcion_eliminar(gestor):
    numero = pedir_numero('Número de la tarea a eliminar: ')
    if numero is None:
        return
    try:
        gestor.eliminar(numero)
        print('Tarea eliminada')
    except ValueError as error:
        print(error)


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================

# Creamos el objeto gestor (se ejecuta su __init__).
gestor = GestorTareas(ARCHIVO_TAREAS)
# Leemos el archivo; si no existe, empieza vacío.
gestor.cargar()

# Ciclo infinito: muestra el menú hasta que elijan salir.
while True:
    opcion = mostrar_menu()

    if opcion == 1:
        opcion_agregar(gestor)
    elif opcion == 2:
        opcion_ver(gestor)
    elif opcion == 3:
        opcion_completar(gestor)
    elif opcion == 4:
        opcion_eliminar(gestor)
    elif opcion == 5:
        print('Gracias por usar el servicio')
        break