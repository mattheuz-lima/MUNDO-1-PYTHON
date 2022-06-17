#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5   e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,5)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Vou pensar um número entre 0 e 5... Tente adivinhar!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

jogador = int(input('Qual número foi escolhido: '))
print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! O número escolhido foi {} e não {}'.format(computador,jogador))


