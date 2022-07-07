#! python
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias
meses = map(lambda mes, dias: (mes, dias), month_name, mdays)
meses_31 = filter(lambda mes: mes[1] == 31, meses)
resultado = reduce(
    lambda r, mes: f'{r}\n- {mes[0].capitalize()}', meses_31,
    'Lista de meses com 31 dias:')
print(resultado)
