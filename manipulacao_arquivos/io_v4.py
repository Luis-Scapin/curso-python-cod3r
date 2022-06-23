#! /usr/local/bin/python

try:
    arquivo = open('pessoas.csv', encoding='utf8')

    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado!')
