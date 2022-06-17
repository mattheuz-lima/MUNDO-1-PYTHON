# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Analisador de triângulos')
# se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.
reta1 = float(input('Valor do primeiro segmento:'))
reta2 = float(input('Valor do aegundo segmento:'))
reta3 = float(input('Valor do terceiro segmento:'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM formar um triângulo!')









