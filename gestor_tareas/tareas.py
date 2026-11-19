class Tarea:

    def __init__(self, titulo):
        self.titulo = titulo
        self.completada =  False

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