# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Forneça o valor do produto para que haja o desconto:R$'))
novo = produto - (produto * 5/100)
print('O preço do produto custava {}, com o desconto o seu novo valor vai ser {:.2f}'.format(produto, novo))