#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Em qual cidade você mora?')).strip()
print(cidade[:3].upper() == ('SÃO'))