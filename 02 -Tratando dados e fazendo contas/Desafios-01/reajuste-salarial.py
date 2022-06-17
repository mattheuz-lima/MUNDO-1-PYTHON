#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o seu sálario?'))
print('O seu novo sálario é:{}'.format(salario + (salario * 15/100)))