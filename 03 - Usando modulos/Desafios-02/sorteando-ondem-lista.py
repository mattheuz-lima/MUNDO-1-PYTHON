#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
nome1 = str(input('Cliente 1:'))
nome2 = str(input('Cliente 2:'))
nome3 = str(input('Cliente 3:'))
nome4 = str(input('Cliente 4:'))
nome5 = str(input('Cliente 5:'))
nome6 = str(input('Cliente 6:'))
lista = [nome1, nome2, nome3, nome4, nome5, nome6]
random.shuffle(lista) #A função random.shuffle() é utilizada para exibir o resultado de uma lista ou de uma tupla de forma embaralhada.
print('A ondem de apresentação será:')
print(lista)