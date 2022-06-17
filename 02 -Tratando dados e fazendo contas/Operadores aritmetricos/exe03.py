n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2 
su = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
print('A soma é {}, a subtração é {}, a multiplicação é {:.3f}'.format(s,su,m), end='')
print('A divisão é {}, a potencia é {}'.format(d,p))

#end='' -> serve para não quebrar a linha de um print para outro
#:.3f -> serve para limitar quantas casas decimais o numero float vai ficar