#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Qual o valor do ângulo:'))
seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} \nTem o seno de {:.2f}\nTem o cosseno de {:.2f}\nTem a tangente de {:.2f}'.format(ang,seno,cose,tan))

