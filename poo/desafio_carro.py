class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade = 0

    def acelerar(self, delta=5):
        self.velocidade += delta if self.velocidade + \
            delta <= self.velocidade_maxima else self.velocidade_maxima - self.velocidade

        return self.velocidade

    def frear(self, delta=5):
        self.velocidade -= delta if self.velocidade - delta >= 0 else self.velocidade

        return self.velocidade


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(f'Acelerando: {c1.acelerar(8)}')

    for _ in range(10):
        print(f'Freando: {c1.frear(delta=20)}')
