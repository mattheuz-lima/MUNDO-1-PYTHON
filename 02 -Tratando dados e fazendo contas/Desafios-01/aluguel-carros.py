# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Km_Percorridos = float(input('Quantos Km foi percorrido:'))
Qtd_dias = int(float(input('Por quantos dis o carro ficou alugado:')))
Valor_Pagar = Km_Percorridos * 0.15 + Qtd_dias * 60
print('O valor a ser pago pelo o aluguel é {}'.format(Valor_Pagar))