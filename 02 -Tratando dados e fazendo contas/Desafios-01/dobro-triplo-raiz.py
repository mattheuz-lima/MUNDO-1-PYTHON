# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = float(input('Digite um número:'))
dobro = numero * 2
tripulo = numero * 3
raiz = (numero ** (1/2)) #serve para calcular a raiz quadrada
print('Analisando o número {}, o seu drobro é {}, o se tripúlo é {} e a sua raiz quadrada é {:.3f}'.format(numero, dobro, tripulo, raiz)) 
#{:.3f} serve para deixar apenas 3 números apos a vírgula. 