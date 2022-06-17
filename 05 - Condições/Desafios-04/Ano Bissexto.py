# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Qual o ano que deseja analisar? Digite 0 para saber o ano atual:'))
if ano == 0:
    ano = date.today().year  # esse comando server para pegar o ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {}  NÃO É BISSEXTO.'.format(ano))
