#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


import random

aluno1 = str(input('Primeiro aluno:'))
aluno2 = str(input('Segundo aluno:'))
aluno3 = str(input('Terceiro aluno:'))
aluno4 = str(input('Quarto aluno:'))
aluno5 = str(input('Quinto aluno:'))

lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
escolhido = random.choice(lista) #esse comando random.choice serve para sortear algo aleatório em uma lista
print('#################################################')
print('O GANHADOR FOI: {}'.format(escolhido))
print('#################################################')
