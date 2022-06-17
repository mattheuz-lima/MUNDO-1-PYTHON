# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

variavel = input('Digite algo:')
print('O tipo primitivo desse dado é ',type(variavel))
print('Foi preenchida com espaço?' , variavel.isspace())
print('Esse dado é um número?', variavel.isnumeric())
print('Esse dado é alfabetico?' , variavel.isalpha())
print('Esse dado é alfanýmerico?' , variavel.isalnum())
