# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
valor = float(input('Qual o valor que você possui?'))
resultado = valor / 4.94
print('Analisando o valor fornecido ({}), é possível comprar {:.2f} dólares'.format(valor, resultado))