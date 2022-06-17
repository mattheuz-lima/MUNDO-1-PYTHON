frase = 'CURSO EM VÍDEO PYTHON'
#FATIAMENTO
print(frase[9]) #vai indentificar dentro da cadeia de caracter apenas o valor 9

print(frase[9:14]) #vai selecionar os valores de 9 até 13, pois o 14 vai ser excluido (o ultimo valor não entra na contagem)

print(frase[9:21:2]) #começa no 9, vai até 20, pulando de 2 em 2

print(frase[:5]) #está sendo definido apenas onde o fatiamento termina

print(frase[15:]) #está sendo definido apenas onde o fatiamente começa

print(frase[9::3]) #está sendo definido o começo e que vai pular em 3 em 3 até o final

#ANÁLISE
#usando a função len() -- resolverá a expressão e retornará a quantidade de elementos contidos -> comprimento 
print(len(frase)) #21 letras

#A função count() retorna a quantidade de vezes que um mesmo elemento está contido numa lista/texto.
print(frase.count('O')) #3

#A função find() retorna onde o valor entre () começa na cadeia de caracteres 
print(frase.find('EM'))

print('CURSO' in frase) #serve para saber se tem o valor desejado dentro da cadeia de caractere

#TRANSFORMAÇÃO
#O replace() substitui cada ocorrência correspondente do caractere/texto antigo na string pelo novo caractere/texto.
print(frase.replace('CURSO','ATIVIDADE'))

#O upper() converte todos os caracteres minúsculos em uma string em caracteres maiúsculos e os retorna.
print(frase.upper())

#O lower() converte todos os caracteres maiúsculo em uma string em caracteres maiúsculos e os retorna.
print(frase.lower())

#O método capitalize() converte o primeiro caractere de uma string em letras maiúsculas e todos os outros caracteres em minúsculas, se houver.
print(frase.capitalize())

#O método title() retorna uma string com a primeira letra de cada palavra em maiúscula.
print(frase.title())

#O método strip serve para remover espaços que não fazem diferença ou que seja inúteis.
print(frase.strip())

    #frase.rstrip() -> remove os espaços apenas da direita
    #frase.lstrip() -> remove os espaços apenas da esquerda
    
#DIVISÃO
#O método split() divide uma string no separador especificado considerando os espaços e retorna uma lista de strings.
print(frase.split())

#JUNÇÃO
#O método join() é um método de string e retorna uma string na qual os elementos da sequência foram unidos por um separador str.
print(''.join(frase))