#! /usr/local/bin/python

arquivo = open('pessoas.csv', encoding='utf8')

for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
