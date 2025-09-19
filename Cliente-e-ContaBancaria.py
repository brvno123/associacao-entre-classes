class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return self.nome


class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente

    def __str__(self):
        return f'Titular: {self.cliente}, Número da conta: {self.numero}'


cliente1 = Cliente("Ana Souza", "123.456.789-00")

conta1 = ContaBancaria("12345-6", cliente1)

print(conta1)
