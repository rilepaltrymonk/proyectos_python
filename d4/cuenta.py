
# ejemplo_clases.py

# 'class' define el molde. Por convención, el nombre va en MayúsculaInicial.
class Cuenta:

    # __init__ es el constructor: se ejecuta solo al crear un objeto.
    # 'self' es "este objeto". Los demás parámetros son los datos que se piden.
    def __init__(self, titular, saldo_inicial):
        # Guardamos los datos DENTRO del objeto con self.
        # A estos se les llama "atributos".
        self.titular = titular
        self.saldo = saldo_inicial

    # Un método es una función dentro de la clase. Siempre lleva self primero.
    def depositar(self, monto):
        # Modifica el saldo de ESTE objeto en particular.
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print('Fondos insuficientes')
            return
        self.saldo -= monto

    # Un método que usa otro método de la misma clase: self.nombre_del_metodo()
    def tiene_fondos(self):
        return self.saldo > 0

    # __str__ define cómo se ve el objeto cuando haces print(objeto).
    # Debe DEVOLVER un texto, no imprimirlo.
    def __str__(self):
        return f'{self.titular}: ${self.saldo}'


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL: aquí usamos la clase
# ------------------------------------------------------------

# Crear objetos: se llama a la clase como si fuera una función.
# Python ejecuta __init__ y pasa self automáticamente.
cuenta1 = Cuenta('Ana', 1000)
cuenta2 = Cuenta('Luis', 50)

# Llamar métodos: objeto.metodo(datos). Sin pasar self.
cuenta1.depositar(500)
cuenta2.retirar(200)      # imprime 'Fondos insuficientes'

# Leer atributos: objeto.atributo (con punto, no con corchetes).
print(cuenta1.titular)    # Ana
print(cuenta1.saldo)      # 1500

# print directo del objeto usa __str__
print(cuenta1)            # Ana: $1500
print(cuenta2)            # Luis: $50

# Cada objeto tiene sus propios datos.
print(cuenta1.tiene_fondos())  # True

# Modificar un atributo desde afuera también se puede.
cuenta2.saldo = 0
print(cuenta2.tiene_fondos())  # False