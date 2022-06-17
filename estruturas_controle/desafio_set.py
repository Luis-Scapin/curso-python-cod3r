import re

PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = [
    'João gosta de religião, futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    palavras_texto = [re.sub(r"[^\w\s]", '', palavra).lower()
                      for palavra in texto.split()]

    intercesao = list(PALAVRAS_PROIBIDAS.intersection(set(palavras_texto)))

    if intercesao:
        print(
            f'Texto possui palavras proibidas: {", ".join(intercesao[:-1])} e {intercesao[-1]}')
    else:
        print('Texto autorizado:', texto)
