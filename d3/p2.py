import json

lista = [
    {'Titulo': 'Salir a comer', 'status': False},
    {'Titulo': 'Salir a correr', 'status': True},
    {'Titulo': 'Pasear al perror', 'status': False},
]

with open('prueba2.json', 'w', encoding='UTF-8') as archivo:
    json.dump(lista, archivo, ensure_ascii=False)

print('Archivo Guardado')

with open('prueba2.json', 'r', encoding='UTF-8') as archivo:
    lista_leida = json.load(archivo)

print(lista_leida)

for elemento in lista:
    print(f'Titulo: {elemento['Titulo']}, status: {elemento['status']}')