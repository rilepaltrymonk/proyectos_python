import pytest, requests

from poke_dex import consultarpokemon

def test_pokemon_existente():
    datos = consultarpokemon('pikachu')
    assert datos['name'] == 'pikachu'    

def test_pokemon_inexistente():
    assert consultarpokemon('no_existe') is None

def test_consulta_exitosa():
    respuesta = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    assert respuesta.status_code == 200

def test_pokemon_exitoso():
    
    respuesta = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    datos = respuesta.json()
    assert datos['name'] == 'pikachu'
