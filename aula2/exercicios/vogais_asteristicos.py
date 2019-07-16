#!/usr/bin/python3

#SCRIP PARA TROCAR VOGAL DE UMA PALAVRA POR "*"

palavra = input('Digite a palavra: ')
vogais = 'AEIOUÃÕÁÉÍÓÚÀÈÌÒÙ1aeiouãõáéíóúàèèòù'

#FORMA 1 - CONTANENADO UMA NOVA STRING
troca = ''
for k in palavra:
	if k in vogais:
		troca += '*'
	else:
		troca += k

print(troca)

'''

#FORMA 2 - USANDO O REPALCE
for k in palavra:
	if k in vogais:
		palavra = palavra.replace(k, '*')

print(palavra)

'''