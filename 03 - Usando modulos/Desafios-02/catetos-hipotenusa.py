#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

'''Segundo o Teorema de Pitágoras, a soma dos quadrado dos catetos de um triângulo retângulo é igual ao quadrado de sua hipotenusa: h2 = ca2 + co2'''

cateto_oposto = float(input('Comprimento do cateto oposto:'))
cateto_adjacente = float(input('Comprimento do cateto adjacente:'))
hi = hypot(cateto_oposto, cateto_adjacente)
print('Calculando os valores dos catetos, o valor da hipotenusa é: {:.1f}'.format(hi)) 
