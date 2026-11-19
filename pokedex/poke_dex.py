import requests

def consultar_api(nombre):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre.strip().lower()}'
    try:
        respuesta = requests.get(url, timeout=10)
    except requests.exceptions.RequestException:
        return None
    if respuesta.status_code != 200:
        return None
    return respuesta.json()

def consultar_pokemon():
    nombre = input('Nombre del Pokémon: ')
    nombre = nombre.strip()
    if not nombre:
        print('El titulo no puede estar vacío')
        return
    datos = consultar_api(nombre)
    if datos is None:
        print('No se encontró el Pokémon escrito')
    else:
        print(datos['name'], datos['height'], datos['weight'], datos['types'][0]['type']['name'])

def opcion_menu():
    while True:
        try:
            opcion = int(input('Elige la opcion deseada: \n'
                            '1.Consultar tu pokemón \n'
                            '2.Salir \n'))
        except ValueError:
            print('Debe ser una opcion numerica')
        else:
            if 1 <= opcion <= 2:
                return opcion
            print('Tiene que ser un numero entre el 1 y el 2')


def main():

    while True:
        opcion = opcion_menu()

        if opcion == 1:
            consultar_pokemon()
        elif opcion == 2:
            print('Gracias por su consulta')
            break
        

if __name__ == '__main__':
    main()