#! /usr/bin/python

import csv

with open('pessoas.csv', encoding='utf8') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))
