

class Cuenta:
    def __init__(self, cliente, saldo_inicial):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if self.saldo < monto:
            print('saldo insuficiente')
            return
        self.saldo -= monto

    def consulta(self):
        return self.saldo
         
    def __str__(self):
        return f'Cliente: {self.cliente} - $: {self.saldo}'


cliente1 = Cuenta('Mauricio Castillo', 500)
cliente2 = Cuenta('Mauricio Perez', 600)
cliente3 = Cuenta('Mauricio Tortolo', 900)

cliente1.depositar(600)
cliente2.depositar(900)

print(cliente1)
print(cliente2) 
print(cliente3)