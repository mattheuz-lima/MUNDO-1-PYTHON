# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""numero = int(input('Digite um número inteiro:'))
resultado = numero % 2

if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))"""

numero = int(input('Digite um número inteiro:'))
m = numero / 2
x = str(m)
if '.5' in x:
    print('NUMERO IMPAR')
else:
    print('Numero Par')
