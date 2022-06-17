"""Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""



nome = str(input('Digite o seu nome completo:')).strip() #está removendo espaços inuteis
print('O Seu nome com todas as letras maúsculas é: {}'.format(nome.upper()))
print('O seu nome com todas as letras minúsculas é: {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(" "))) #está contando quantas letras tem menos a quantidade de espaços

separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))



