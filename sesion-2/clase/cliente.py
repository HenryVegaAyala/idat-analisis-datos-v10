class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def comprar(self, monto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            print(f"Compra realizada, saldo restante: {self.saldo}")
        else:
            print(f"Saldo insuficiente, no se puede realizar la compra."
                  f" Saldo actual: {self.saldo}, monto de la compra: {monto}")


cliente_1 = Cliente("Luis", 1000)
print(cliente_1.nombre)
cliente_1.comprar(500)  # Estoy comprando una laptop
print(cliente_1.saldo)
cliente_1.comprar(400)  # Estoy comprando un celular
print(cliente_1.saldo)

print("-" * 100)

cliente_2 = Cliente("Ana", 100)
print(cliente_2.nombre)
cliente_2.comprar(101)  # Estoy comprando un celular
