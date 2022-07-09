#! python
from functools import reduce
from operator import add

valores = (30, 10, 25, 70, 100, 94)

print(sorted(valores))  # Função sorted NÃO altera a lista original
print(valores)

# valores.sort() -> .sort() altera a lista original
# print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(tuple(reversed(valores)))
print(valores)

# valores.reverse()  # .reverse() altera a lista original
# print(valores)
