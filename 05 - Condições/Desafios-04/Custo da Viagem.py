# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual é a distância da viagem em Km?'))
if distancia <= 200:
    taxa = distancia * 0.5
else:
    taxa = distancia * 0.45
print('O valor a pagar pela a viagem é de $ {:.2f}'.format(taxa))
