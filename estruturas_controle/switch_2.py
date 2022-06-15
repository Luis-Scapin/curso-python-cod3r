import switch_1 as s1

def dia_semana_ou_fds(dia):
    dias = {
        1: 'fim de semana',
        2: 'semana',
        3: 'semana',
        4: 'semana',
        5: 'semana',
        6: 'semana',
        7: 'fim de semana',
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{s1.get_dias_semana(dia)} é dia de {dia_semana_ou_fds(dia)}!')
