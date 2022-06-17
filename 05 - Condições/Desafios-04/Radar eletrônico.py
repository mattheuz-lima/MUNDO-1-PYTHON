# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Velocidade do carro em Km/h é:'))
if velocidade > 80:
    print('Acima do limite permitido.')
    multa = (velocidade - 80) * 7

    print('Sua velocidade foi de {}, a multa vai custar R$7,00 por cada Km acima do limite.'.format(velocidade))
    print('Sua multa é de ${:.2f} reais'.format(multa))
else:
    print('Você passou com segurança!')
