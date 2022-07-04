#! python
class Humano:
    # atributo de classe - estático
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        # atributo de instância prevalece
        self.especie = 'Homo Neanderthalensis'
        return self  # fluent


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')
