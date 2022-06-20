#! python
# 0, 1, 1, 2, 3, 5, 8, 13, 21...


def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante: Condição de parada
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    #Listar os 20 primeiros números da sequência
    for fib in fibonacci(20):
        print(fib)
