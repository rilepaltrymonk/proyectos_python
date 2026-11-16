from practica import Tarea

def test_tarea_nueva_esta_pendiente():
    t = Tarea('Compra leche')
    assert t.completada == False

def test_completar_tarea():
    t = Tarea('Comprar leche')
    t.completar()
    assert t.completada == True