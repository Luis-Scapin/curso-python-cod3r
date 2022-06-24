#! /usr/bin/python

import csv

with open('desafio-ibge.csv', encoding='latin1') as entrada:
    for cidade in csv.reader(entrada):
        if cidade[0] == 'FID':
            continue

        print('Nome: {8}, Cidade: {3}'.format(*cidade))
