nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
nota3 = float(input('Nota 3:'))
media = (nota1 + nota2 + nota3) / 3
print('Sua média final é: {:.2f}'.format(media))

if media >= 6.5:
    print('Você foi aprovado!')
elif media == 6:
    print('fazer trabalho de recuperação')
else:
    print('Reprovado')
    
    
    