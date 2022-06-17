#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc #esse comando serve pra importar a biblioteca com funcionalidade de matematica
num = float(input('Digite um número decimal:'))
print('O número {} tem a parte inteira {}'.format(num,trunc(num)))

