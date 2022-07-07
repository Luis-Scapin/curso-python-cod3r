#! python
def fatorial(n):
    return n * fatorial(n - 1) if n > 0 else 1


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')

    # Fatorial de 10 é igual a 6 semanas em segundos:
    print('6 semanas:', 6 * 7 * 24 * 60 * 60)
