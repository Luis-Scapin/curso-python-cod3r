#! python
# Implementação simplificada do map
def mapear(funcao, lista):
    return (funcao(item) for item in lista)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2, 3 ,4])
    print(list(resultado))
