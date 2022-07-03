class Pessoa:
    MAIOR_IDADE = 18

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        if not self.idade:
            return self.nome

        return f'{self.nome} ({self.idade} anos)'

    def is_adulto(self):
        return (self.idade or 0) >= Pessoa.MAIOR_IDADE


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario) -> None:
        super().__init__(nome, idade)
        self.salario = salario


class Cliente(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return None if not self.compras \
            else sorted(self.compras, key=lambda c: c.data)[-1].data

    def total_compras(self):
        return sum([compra.valor for compra in self.compras])


class Compra:
    def __init__(self, vendedor, data, valor) -> None:
        self.vendedor = vendedor
        self.data = data
        self.valor = valor
