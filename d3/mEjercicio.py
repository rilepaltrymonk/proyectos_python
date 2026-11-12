# prueba_json.py

import json  # Módulo que traduce entre listas/diccionarios de Python y texto JSON

# ---------------------------------------------------------
# PARTE 1: GUARDAR
# ---------------------------------------------------------

# Esta es una lista de diccionarios, igual que tu lista de tareas
tareas = [
    {'titulo': 'Comprar leche', 'completada': False},
    {'titulo': 'Comprar piñata', 'completada': True},
]

# open(...) abre (o crea) el archivo 'prueba.json'
#   'w'  -> modo escritura (si el archivo existe, lo reemplaza)
#   encoding='utf-8' -> para que las ñ y los acentos se guarden bien
# 'with' cierra el archivo solo al terminar el bloque
# 'as archivo' -> mientras estamos dentro, el archivo se llama "archivo"
with open('prueba.json', 'w', encoding='utf-8') as archivo:
    # json.dump(qué_guardar, dónde_guardarlo)
    json.dump(tareas, archivo, ensure_ascii=False)

print('Archivo guardado')

# ---------------------------------------------------------
# PARTE 2: LEER
# ---------------------------------------------------------

#   'r'  -> modo lectura
with open('prueba.json', 'r', encoding='utf-8') as archivo:
    # json.load(de_dónde_leer) devuelve la lista de Python ya lista para usar
    tareas_leidas = json.load(archivo)

print('Lo que leí del archivo:')
print(tareas_leidas)

# ---------------------------------------------------------
# PARTE 3: COMPROBAR QUE ES UNA LISTA NORMAL
# ---------------------------------------------------------

# Funciona igual que las listas que ya conoces
for tarea in tareas_leidas:
    print(tarea['titulo'], tarea['completada'])