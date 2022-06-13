# Conceitos  Notas
# A         De 10 a 9.1
# A-        De 9 a 8.1
# B         De 8 a 7.1
# B-        De 7 a 6.1
# C         De 6 a 5.1
# C-        De 5 a 4.1
# D         De 4 a 3.1
# D-        De 3 a 2.1
# E         De 2 a 1.1
# E-        De 1 a 0

# *Para notas maiores que 10 e menores que 0 será impresso "Nota inválida"
#! python

import sys
import errno


class TerminalColor:
    ''' Cores do terminal '''
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def obter_conceito(nota):
    ''' Obter o conceito baseado na nota do aluno. '''

    if 0 > nota > 10:
        return None
    elif nota > 9:
        return "A"
    elif nota > 8:
        return "A-"
    elif nota > 7:
        return "B"
    elif nota > 6:
        return "B-"
    elif nota > 5:
        return "C"
    elif nota > 4:
        return "C-"
    elif nota > 3:
        return "D"
    elif nota > 2:
        return "D-"
    elif nota > 1:
        return "E"
    elif nota >= 0:
        return "E-"


def is_number(s):
    """ Returns True is string is a number. """
    return s.replace('.', '', 1).isdigit()


def ajuda(msg):
    ''' Mostrar mensagem de ajuda '''

    print(TerminalColor.ERRO)
    print(msg)
    print(f'\nSintaxe: {sys.argv[0]} <nota>')
    print(TerminalColor.NORMAL)


def run():
    ''' Executar o programa '''

    if len(sys.argv) < 2:
        ajuda('Argumento \'nota\' não informado!')
        sys.exit(errno.EPERM)

    if not is_number(sys.argv[1]):
        ajuda('Argumento inválido!\nInforme um valor numérico.')
        sys.exit(errno.EINVAL)

    conceito = obter_conceito(float(sys.argv[1]))

    if conceito is None:
        ajuda('Nota informada fora dos limites!\nInformar uma nota entre 0 e 10.')
        sys.exit(errno.EINVAL)

    print(f'O aluno obteve o conceito: {conceito}')


if __name__ == '__main__':
    run()
