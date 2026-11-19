import pytest

from tareas import Tarea
from gestor import GestorTareas
from menu import *
from main import *


def test_tarea_nueva_esta_pendiente():
    t = Tarea('Compra leche')
    assert t.completada == False

def test_completar_tarea():
    t = Tarea('Comprar leche')
    t.completar()
    assert t.completada == True

def test_a_diccionario():
    t = Tarea('Comprar leche')
    assert t.a_diccionario() == {'titulo': 'Comprar leche', 'completada': False}

def test_ida_y_vuelta():
    t = Tarea('Comprar leche')
    t.completar()
    copia = Tarea.desde_diccionario(t.a_diccionario())
    assert copia.titulo == 'Comprar leche'
    assert copia.completada == True

def test_agregar_tarea(tmp_path):
    gestor = GestorTareas(str(tmp_path/'tareas.json'))
    gestor.agregar('Comprar leche')
    assert len(gestor.ver()) == 1

def test_agregar_titulo_vacio_lanza_error(tmp_path):
    gestor = GestorTareas(str(tmp_path/'tareas.json'))
    with pytest.raises(ValueError):
        gestor.agregar(' ')

def test_tarea_fuera_de_rango(tmp_path):
    gestor = GestorTareas(str(tmp_path/'tareas.json'))
    gestor.agregar('Comprar leche')
    with pytest.raises(ValueError):
        gestor.modificar(0)
    with pytest.raises(ValueError):
        gestor.modificar(10)

def test_completar_tarea(tmp_path):
    gestor = GestorTareas(str(tmp_path/'tareas.json'))
    gestor.agregar('Comprar leche')
    gestor.modificar(1)
    tareas = gestor.ver()
    assert tareas[0].completada == True    

def test_eliminar_tareas(tmp_path):
    gestor = GestorTareas(str(tmp_path/'tareas.json'))
    gestor.agregar('Comprar leche')
    gestor.eliminar(1)
    tareas = gestor.ver()
    assert len(tareas) == 0

def test_guardar_y_cargar(tmp_path):
    ruta = str(tmp_path/'tareas.json')

    gestor1 = GestorTareas(ruta)
    gestor1.agregar('Comprar leche')
    gestor1.modificar(1)

    gestor2 = GestorTareas(ruta)
    assert len(gestor2.ver()) == 0     # todavía no leyó el archivo
    gestor2.cargar()
    assert len(gestor2.ver()) == 1     # ahora sí tiene la tarea
    tareas = gestor2.ver()
    assert tareas[0].titulo == 'Comprar leche'
    assert tareas[0].completada == True

def test_cargar_archivo_inexistente(tmp_path):
    gestor = GestorTareas(tmp_path/'no_existe.json')
    gestor.cargar()
    assert gestor.ver() == []

def test_cargar_archivo_dañado(tmp_path):
    archivo = tmp_path/'tareas.json'
    archivo.write_text('Hola', encoding = 'UTF-8')
    gestor = GestorTareas(tmp_path/'tareas.json')
    gestor.cargar()
    assert gestor.ver() == []

def test_cargar_no_es_una_lista(tmp_path):
    archivo = tmp_path/'tareas.json'
    archivo.write_text('5', encoding = 'UTF-8')
    gestor = GestorTareas(archivo)
    gestor.cargar()
    assert gestor.ver() == []
