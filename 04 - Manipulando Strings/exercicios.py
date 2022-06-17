

print('Seja bem vindo ao sistema de cadastro!')
nome = str(input('Infome o seu nome completo:'))
nome2 = nome.split()
print('O seu cadastro foi realizado, {}!'.format(nome2[0]))

texto = str(input('Digite o seu nome completo:')).strip().upper()
print ('O texto fornecido tem {} de caracteres.'.format(len(texto)))

#print('O seu nome em MAIÚSCULO é: {}'.format(texto.upper()))
#print('O seu nome é minúsculo é: {}'.format(texto.lower()))

print('O nome (Informação) aparece {} vezes.'.format(texto.count('INFORMAÇÃO')))
print(texto.find('INFORMAÇÃO'))

frase = str(input("Qual o seu nome?"))
print (frase.split("."))