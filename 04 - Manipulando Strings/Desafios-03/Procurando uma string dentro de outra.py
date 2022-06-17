#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Nome completo:')).strip()
print('O seu nome tem Silva? {}'.format('SILVA' in nome.upper()))