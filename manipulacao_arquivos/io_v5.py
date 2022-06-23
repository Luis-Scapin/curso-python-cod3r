#! /usr/local/bin/python

with open('pessoas.csv', encoding='utf8') as arquivo:
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado!')
